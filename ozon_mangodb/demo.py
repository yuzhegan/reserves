# encoding='utf-8

# @Time: 2024-04-08
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import polars as pl
import pandas as pd
import math

# 1. 读取数据
path = ('./ozon_mangodb/ozon_test.xlsx')
df = pl.from_pandas(pd.read_excel(path, engine="openpyxl"))
# df = pl.read_excel(path, sheet_name='Sheet1',
#                    read_csv_options={'ignore_errors': True, 'skip_rows': 0, 'dtypes': {}})
print(df.schema)
df = df.with_columns([(pl.col('28日销售额')/pl.col('28日订单均价')).alias('28日销量'),
                      (pl.lit(10)).alias('越库费'),
                      ((pl.col('28日订单均价')*0.17).map_elements(lambda x: math.ceil(x), return_dtype=pl.Float64)
                       ).alias('类目佣金'),  # 向上取整
                      ((pl.col('28日订单均价')*0.01).map_elements(lambda x: math.ceil(x), return_dtype=pl.Float64)
                       ).alias('平台收单费'),  # 向上取整
                      (pl.lit(32).alias('物流')),
                      ((pl.col('28日订单均价')*0.055).map_elements(lambda x: math.ceil(x), return_dtype=pl.Float64)
                       ).alias('最后一公里'),

                      ])
df = df.with_columns([
    (pl.col('28日订单均价') - pl.col('越库费') - pl.col('类目佣金') - pl.col('平台收单费') - pl.col('物流') - pl.col('最后一公里')).alias('毛利润')
])

# 第二步：使用已经存在的"毛利润"列计算"毛利润率"
df = df.with_columns([
    (pl.col('毛利润') / pl.col('28日订单均价')).alias('毛利润率')
])

df.write_excel('./ozon_mangodb/ozon_test_output.xlsx')
# exit()
# 透视表
plvt = df.group_by(['二级分类', '三级分类', '四级分类']).agg([pl.col('商品链接').count().alias('类目产品数量'),
                                                 pl.col('28日销量').sum().alias(
    '28日销量'),
    pl.col('28日销售额').sum().alias(
    '28日销售额'),
    pl.col('28日订单均价').mean().alias(
    '28日订单均价'),
    pl.col('发货仓库数量（个）').max().alias(
    '仓库数量'),
    pl.col('交货时间（天）').mean().alias(
    '交货天数'),
    pl.col('广告费用占比 (%)').mean().alias(
    '广告费'),
    pl.col('因缺货而错过的订单金额（₽）').sum().alias(
    '缺货错失销售额')
]).sort(by='28日销售额', descending=True)


plvt.write_excel('./ozon_mangodb/pivot.xlsx')
