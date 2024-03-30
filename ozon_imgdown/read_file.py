# encoding='utf-8

# @Time: 2024-03-30
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import pandas as pd
from openpyxl import load_workbook, Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.drawing.image import Image as OpenpyxlImage
from openpyxl.utils import get_column_letter



class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path
        # self.save_path = save_path
        self.df = pd.read_excel(self.file_path)
        self.wb = Workbook()
        self.ws = self.wb.active
        for r in dataframe_to_rows(self.df, index=False, header=True):
            self.ws.append(r)


