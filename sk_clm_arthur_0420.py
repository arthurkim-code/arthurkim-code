# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:00:46 2020

@author: kkim
"""
from datetime import date
import pandas as pd

today = date.today()
d1 = today.strftime("%m%d%Y")

excel_url = 'C:/Users/kkim/Documents/Python/TEST/copytest_0421.xlsx'

df1 = pd.read_excel(excel_url, sheet_name ='p1')
df2 = pd.read_excel(excel_url, sheet_name ='s1')
df3 = pd.read_excel(excel_url, sheet_name ='a1')

df4 = pd.read_excel(excel_url, sheet_name ='present')
df5 =  pd.read_excel(excel_url, sheet_name ='sequence')
df6 =  pd.read_excel(excel_url, sheet_name ='approved')
df7 = pd.read_excel(excel_url, sheet_name ='user')

writer = pd.ExcelWriter('C:/Users/kkim/Documents/Python/TEST/sk_clm27042021.xlsx', engine='xlsxwriter')

df1['ParentId'] = df4['Id']
df1['AccessLevel'] = 'Edit'
df1['RowCause'] = 'Manual'

df2['ParentId'] = df5['OCE__Sequence__r.Id']
df2['AccessLevel'] = 'Edit'
df2['RowCause'] = 'Manual'

df3['ParentId'] = df6['Id']
df3['AccessLevel'] = 'Edit'
df3['RowCause'] = 'Manual'

for i in range(len(df7)):
 #   for j in range(len(df1)):
    #df1.iloc[0:,0] = df5.iloc[i, 1]
    df1['User_p' + str(i)] = df7.iloc[i, 1]
    df2['User_s' + str(i)] = df7.iloc[i, 1]
    df3['User_a' + str(i)] = df7.iloc[i, 1]

# df1['UserOrGroupId'].append(df1.iloc[:,4+i:])
   # df1['UserOrGroupId'] = pd.concat(df1['UserOrGroupId'], df5.iloc[i, 1])
 # Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='Sheet1', index=False)
df2.to_excel(writer, sheet_name='Sheet2', index=False)
df3.to_excel(writer, sheet_name='Sheet3', index=False)

writer.save()

#df3.to_excel('C:/Users/kkim/Documents/Python/TEST/sk_clm' + d1 + '.xlsx', index=False)



