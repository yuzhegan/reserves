# encoding='utf-8
# @Time: 2024-01-04
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import polars as pl
# 读取文件


def read_file(filename):
    # 读取文件
    if filename.endswith('xlsx'):
        df = pl.read_excel(filename)
    elif filename.endswith('csv'):
        df = pl.read_csv(filename)
    # 将id, sex phone 转换为字符串
    df = df.with_columns([pl.col('id').cast(pl.Utf8),
                          pl.col('sex').cast(pl.Utf8),
                          pl.col('phone').cast(pl.Utf8),
                          ])
    # 取出空行
    df = df.filter(pl.col("name").is_not_null()).sort(["week",'pmAm'], descending=True)
    # 筛选出“选票”列中的“是”
    df = df.filter(pl.col('starts') == "YES")
    # ic(df)
    return df
# 创建随行成人


def create_flower_data(yupiao, df, week):
    # 表示有多少个余票, 最多只能选3个随行 + 1个本人, 最多只能选4个
    # 选出星期几 上午还是下午的票
    df = df.filter((pl.col('week') == week))
    if 1 < yupiao:
        # 选出df中的数据
        flower_df = df[0:yupiao]
        if len(flower_df) > 4:
            flower_df = flower_df[0:4]
    elif yupiao == 1:
        flower_df = df[0:1]
    else:
        flower_df = df[0:0]
    ic(flower_df)
    return flower_df


def get_buji(df, df2):
    return df.join(df2, on=["name", "id"],  how="anti")


# if __name__ == '__main__':
#     df = read_file('./tianwentai/setttings.xlsx')
#     ic(df)
#     flowered_df = read_file('./tianwentai/flowered.csv')
#     ic(flowered_df)
#     # flower_df = create_flower_data(2, df, '星期日')
#     # df  flower_df 的差集
#     # 使用 anti join 来获取 df1 中独有的行
#     df = get_buji(df, flowered_df)
#     ic(df)
#     # pandas_df = flower_df.to_pandas()
#     # pandas_df.to_csv("./tianwentai/flowered.csv", mode='a', header=False, index=False)
#     # 转换 DataFrame 为 CSV 字符串
