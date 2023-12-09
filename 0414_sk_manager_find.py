# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:00:46 2020

@author: kkim
"""
from datetime import date
import pandas as pd

today = date.today()
d1 = today.strftime("%d%m%Y")

excel_url = 'C:/Users/kkim/Documents/Python/TEST/0414_sk.xlsx'

df1 = pd.read_excel(excel_url, sheet_name = 'Sheet7')
df2 = pd.read_excel(excel_url, sheet_name = 'Sheet4')


#df3 = df2.loc[(df2['Territories'].str.contains(df1['Team']))]
#df2['check'] = df2.apply(lambda row : str(row['ADD']) in str(row['Territories']), axis=1) #Verify that ADD territory is exist

df3 = df1.loc[(df1['Team_check'].str.contains("Yes")
             & (df1['Manager_check'].str.contains("No")))]

df3['First'] = df3['Territories'].str.replace(";","")

df3['Team'] = df3['First'].str.split('_').str[0]

df4 = pd.merge(df3, df2[['Team','Manager']], on='Team', how='left')

#print(df4.head())

df3['Added Territories'] = ';' + df4['Manager'] + ';'
#df3['manager_check'] = df3.apply(lambda row : str(df2['Team']) in str(row['Territories']), axis=1)

#print(df3.head())


#df_master = pd.read_excel(excel_url, sheet_name = 'master')
#df_drop = pd.read_excel(excel_url, sheet_name = 'Drop')


#df3 = pd.merge(df2, df1[['SKB_ParentAccountBrickCode','User','User1']], on='SKB_ParentAccountBrickCode', how='left')
#df3 = df3.drop_duplicates()

#df4 = pd.merge(df3, df_master[['User','Territory','Manager']], on='User', how='left')
#df4['Drop_territory1'] = ';' + df4['Territory'] + ';' + df4['Manager'] + ';'

#df5 = pd.merge(df4, df_master[['User1','Territory','Manager']], on='User1', how='left')
#df5['Add_territory1'] = ';' + df5['Territory_y'] + ';' + df5['Manager_y'] + ';'

#df5['Added Territories'] = df5['Add_territory1']
#df5['Dropped Territories'] = df5['Drop_territory1']
#df5 = df5[['Customer Alignment Rule ID'	,'Account Name','OneKeyId',	'SK_Onekey_Status',	'SKB_ParentAccountBrickCode',	'Added Territories'	,'Dropped Territories'	,'Territories']]

df3.to_excel('C:/Users/kkim/Documents/Python/TEST/sk_findmanager_' + d1 + '.xlsx', index=False)

