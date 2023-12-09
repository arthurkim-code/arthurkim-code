# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:00:46 2020

@author: kkim
"""
from datetime import date
import pandas as pd

today = date.today()
d1 = today.strftime("%d%m%Y")

excel_url = 'C:/Users/kkim/Documents/Python/TEST/book101.xlsx'

df1 = pd.read_excel(excel_url, sheet_name = 'Brick')
df2 = pd.read_excel(excel_url, sheet_name = 'CAR')
df_master = pd.read_excel(excel_url, sheet_name = 'master')
#df_drop = pd.read_excel(excel_url, sheet_name = 'Drop')

df3 = pd.merge(df2, df1[['SKB_ParentAccountBrickCode','User','User1']], on='SKB_ParentAccountBrickCode', how='left')
df3 = df3.drop_duplicates()

df4 = pd.merge(df3, df_master[['User','Territory','Manager']], on='User', how='left')
df4['Drop_territory1'] = ';' + df4['Territory'] + ';' + df4['Manager'] + ';'

df5 = pd.merge(df4, df_master[['User1','Territory','Manager']], on='User1', how='left')
df5['Add_territory1'] = ';' + df5['Territory_y'] + ';' + df5['Manager_y'] + ';'

df5['Added Territories'] = df5['Add_territory1']
df5['Dropped Territories'] = df5['Drop_territory1']
df5 = df5[['Customer Alignment Rule ID'	,'Account Name','OneKeyId',	'SK_Onekey_Status',	'SKB_ParentAccountBrickCode',	'Added Territories'	,'Dropped Territories'	,'Territories']]

df5.to_excel('C:/Users/kkim/Documents/Python/TEST/team_' + d1 + '.xlsx', index=False)

