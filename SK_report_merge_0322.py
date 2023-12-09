# -*- coding: utf-8 -*-
"""
Created on 3/22

@author: kkim
"""
from datetime import date
import pandas as pd

today = date.today()
d1 = today.strftime("%d%m%Y")

excel_url = 'C:/Users/kkim/Documents/Python/TEST/Report_dictionary.xlsx'

df1 = pd.read_excel(excel_url, sheet_name = None)

df2 = pd.concat(df1, ignore_index=True)
#print(df2.head())

df2.to_excel('C:/Users/kkim/Documents/Python/TEST/SK_report_' + d1 + '.xlsx', index=False)

