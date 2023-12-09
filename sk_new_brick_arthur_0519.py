
# -*- coding: utf-8 -*-
"""
Created on Wed May  19
@author: kkim
"""

import pandas as pd
import numpy as np
from datetime import date

today = date.today()

d1 = today.strftime("%d%m%Y")

excel_url = 'C:/Users/kkim/Documents/Python/TEST/sk_brick_new.xlsx'


writer = pd.ExcelWriter('C:/Users/kkim/Documents/Python/TEST/NewBrick_Label.xlsx', engine='xlsxwriter')


df1 = pd.read_excel(excel_url, sheet_name ='Sheet1') #read each sheet

df1 = df1.drop_duplicates(subset=['BrickID'], keep='first')

#df1.to_excel('C:/Users/kkim/Documents/Python/TEST/test_' + d1 + '.xlsx', index=False)


df2 = df1[['SKB_SKBrickMaster ID','SKB_BrickAlignment ID','SKB_BrickAlignment','Label','BrickID','BrickID1','Team', 'Employee Number', 'User: Full Name']]
df3 = df1[['SKB_SKBrickMaster ID','SKB_BrickAlignment ID','SKB_BrickAlignment','Label','BrickID','BrickID1','Team', 'Employee Number', 'User: Full Name']]
df4 = df1[['SKB_SKBrickMaster ID','SKB_BrickAlignment ID','SKB_BrickAlignment','Label','BrickID','BrickID1','Team', 'Employee Number', 'User: Full Name']]
df5 = df1[['SKB_SKBrickMaster ID','SKB_BrickAlignment ID','SKB_BrickAlignment','Label','BrickID','BrickID1','Team', 'Employee Number', 'User: Full Name']]
df6 = df1[['SKB_SKBrickMaster ID','SKB_BrickAlignment ID','SKB_BrickAlignment','Label','BrickID','BrickID1','Team', 'Employee Number', 'User: Full Name']]

#print(df2)

#df2.columns = ['BrickID']

df1['BrickID'] = df1['BrickID'].apply(str)
df2['BrickID'] = df2['BrickID'].apply(str)
df3['BrickID'] = df3['BrickID'].apply(str)
df4['BrickID'] = df4['BrickID'].apply(str)
df5['BrickID'] = df5['BrickID'].apply(str)
df6['BrickID'] = df6['BrickID'].apply(str)


df2['BrickID'] = df1['BrickID'].str[0:8] + '00'
df2['NewBrick_Label'] = df2['Label'] + '_' + '의원'
df3['BrickID'] = df1['BrickID'].str[0:8] + '01'
df3['NewBrick_Label'] = df3['Label'] + "_" + "병원"
df4['BrickID'] = df1['BrickID'].str[0:8] + '02'
df4['NewBrick_Label'] = df4['Label'] + "_" + "종합병원"
df5['BrickID'] = df1['BrickID'].str[0:8] + '03'
df5['NewBrick_Label'] = df6['Label'] + "_" + "요양병원"
df6['BrickID'] = df1['BrickID'].str[0:8] + '04'
df6['NewBrick_Label'] = df6['Label'] + "_" + "보건소"

df2 = df2.drop_duplicates()
df3 = df3.drop_duplicates()
df4 = df4.drop_duplicates()
df5 = df5.drop_duplicates()
df6 = df6.drop_duplicates()

#df2 = df2.append(df2[['Label','Team', 'Employee Number','User: Full Name']], ignore_index=True)
#df2 = df2.append(df2[['Label','Team', 'Employee Number','User: Full Name']], ignore_index=True)
#df2 = df2.append(df2[['Label','Team', 'Employee Number','User: Full Name']], ignore_index=True)
#df2 = df2.append(df2[['Label','Team', 'Employee Number','User: Full Name']], ignore_index=True)

#df2 = df2.append(df2)

#df7 = pd.concat([df2, df3, df4, df5, df6], join='outer')

#df7.to_excel(writer, sheet_name='Sheet1', index=False)
df2.to_excel(writer, sheet_name='Sheet1', index=False)
df3.to_excel(writer, sheet_name='Sheet2', index=False)
df4.to_excel(writer, sheet_name='Sheet3', index=False)
df5.to_excel(writer, sheet_name='Sheet4', index=False)
df6.to_excel(writer, sheet_name='Sheet5', index=False)
writer.save()


#print(df4[['BrickID','Name']])

#df3 = df2


#df2['BrickID'] = df2['BrickID'].replace('NaN', df2['BrickID'].iloc[0:4].str[0:8] + '10', inplace=True)


#con= [(df2['BrickID'].str[8:10] == '00'), (df2['BrickID'].str[8:10] == '10')]
#result = [df2['Label']+'_'+'의원', '병원']

#df2['Flag'] = np.select(con, result)

#df2.to_excel('C:/Users/kkim/Documents/Python/TEST/NewBrick_Label_' + d1 + '.xlsx', index=False)

#df2['BrickID'].iloc[4:8] = df2['BrickID'].iloc[0:4].str[0:8] + '10'
#df2['BrickID1'] = df2['BrickID1'].append(df2['BrickID1'].str[0:8] + '20', ignore_index=True)
#df2['BrickID1'] = df1['BrickID'].str[0:8] + '30', ignore_index=True)
#df2['BrickID1'] = df1['BrickID'].str[0:8] + '40', ignore_index=True)

#df2['TEST'] = df2.append(df1['BrickID'].str[0:8] + '30')
#df2['TEST'] = df2.append(df1['BrickID'].str[0:8] + '40', ignore_index=True)


#print(df2)

#df2['Brick1'] = df2['BrickID'].append(df3, ignore_index=True)

#df2.columns = ['BrickID']



#con= [(df2.str[8:10] == '00'), (df2.str[8:10] == '10')]
#result = ['의원', '병원']

#df2['Flag'] = np.select(con, result)



#df3.columns = ['BrickID']


#df6.apply(lambda x: any(df6(x).str[8:10].contains('00')))



#df6.loc[df6[df6.str[8:10].contains('00'), 'Activity_2']]= 'email'
#df6.loc[df6['Activity'].str.contains('conference'), 'Activity_2'] = 'conference'
#df6.loc[df6['Activity'].str.contains('call'), 'Activity_2'] = 'call'



#df6['new'] = pd.np.where(df6.str[8:10].contains("00"), "의원",
#                   pd.np.where(df6.str[8:10].contains("10"), "병원",
#                   pd.np.where(df6.str[8:10].contains("20"), "보건소")))





