# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:00:46 2020

@author: kkim
"""
from datetime import date
import pandas as pd


excel_url = 'C:/Users/kkim/Documents/Python/TEST/SK_brick_0209.xlsx'
excel_url1 = 'C:/Users/kkim/Documents/Python/TEST/car0209.xlsx'

df1 = pd.read_excel(excel_url, sheet_name = 'Sheet2')
df2 = pd.read_excel(excel_url1, sheet_name = 'Sheet1')
df_master = pd.read_excel(excel_url, sheet_name = 'Sheet3')
#df_drop = pd.read_excel(excel_url, sheet_name = 'Drop')


df3 = pd.merge(df2, df1[['SK_BrickCode2','User','User1']], on='SK_BrickCode2', how='left')
df3 = df3.drop_duplicates(subset='Customer Alignment Rule ID', keep='first')


#df4 = pd.merge(df3, df_master[['User','Territory','Manager']], on='User', how='left')
#df4['Drop_territory1'] = ';' + df4['Territory'] + ';' + df4['Manager'] + ';'

#df5 = pd.merge(df4, df_master[['User1','Territory','Manager']], on='User1', how='left')
#df5['Add_territory1'] = ';' + df5['Territory_y'] + ';' + df5['Manager_y'] + ';'

#df5['Added Territories'] = df5['Add_territory1']
#df5['Dropped Territories'] = df5['Drop_territory1']
#df5 = df5[['Customer Alignment Rule ID'	,'Account Name','OneKeyId',	'SK_Onekey_Status',	'SK_BrickCode2',	'Added Territories'	,'Dropped Territories'	,'Territories']]

df3.to_excel('C:/Users/kkim/Documents/Python/TEST/team_sk_final_0209.xlsx', index=False)


#df3.to_excel('C:/Users/kkim/Documents/Python/TEST/brick_change_0209.xlsx', index=False)