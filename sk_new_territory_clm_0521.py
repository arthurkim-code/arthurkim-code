# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:00:46 2020

@author: kkim
"""
from datetime import date
import pandas as pd
import numpy as np

today = date.today()
d1 = today.strftime("%m%d%Y")

excel_url = 'C:/Users/kkim/Documents/Python/TEST/sk_data_align.xlsx'

df_p = pd.read_excel(excel_url, sheet_name ='P')
df_user = pd.read_excel(excel_url, sheet_name ='User')
df_s = pd.read_excel(excel_url, sheet_name ='S')
df_e = pd.read_excel(excel_url, sheet_name ='E')


#print(df_final_p.iloc[1:57,0])

'''
for i in range(len(df_final_p.columns)):
    #df_p = df_p.append(df_p)
    #df_p['UserOrGroupId'] =
    df_p['UserOrGroupId'] = df_final_p.iloc[i,1:57]
    df_p.append(df_p)
    '''

N=131
df_final_p =df_p.reindex(df_p.index.repeat(N)).reset_index(drop=True)
df_final_s =df_s.reindex(df_s.index.repeat(N)).reset_index(drop=True)
df_final_e =df_e.reindex(df_e.index.repeat(N)).reset_index(drop=True)

#df_final_p.dropna(axis=1)
#df_final_p.iloc[:,0] = df_final_p.iloc[:,0].append(df_user.iloc[1])
df_final_p.iloc[:,0] = ""
df_final_s.iloc[:,0] = ""
df_final_e.iloc[:,0] = ""


df5 = df_user.iloc[1,:]
df_p1 = df5.iloc[np.tile(np.arange(len(df5)), 56)] #copy the user by order
df_s1 = df5.iloc[np.tile(np.arange(len(df5)), 289)] #copy the user by order
df_e1 = df5.iloc[np.tile(np.arange(len(df5)), 11)] #copy the user by order

df_p1 = df_p1.reset_index(drop=True)
df_s1 = df_s1.reset_index(drop=True)
df_e1 = df_e1.reset_index(drop=True)

df_final_p.iloc[:,0] = df_p1
df_final_s.iloc[:,0] = df_s1
df_final_e.iloc[:,0] = df_e1
#df5 = df5.reset_index(drop=True)
#n=10
#df_p1 = pd.concat([df5,df5.loc[df5.index.repeat(n)]])


#df_final_p.iloc[:,0] = df_user.iloc[1,:]


#print(df_user.iloc[1,:])
#print(a)
#print(df_final_p)

#print(df_p1.head())

df_final_p.to_excel('C:/Users/kkim/Documents/Python/TEST/new_sk_clm' + d1 + '.xlsx', index=False)
df_final_s.to_excel('C:/Users/kkim/Documents/Python/TEST/new_sk_seq' + d1 + '.xlsx', index=False)
df_final_e.to_excel('C:/Users/kkim/Documents/Python/TEST/new_sk_email' + d1 + '.xlsx', index=False)

#print(df_p.head())

#df_final_p = df_p [[]]

#df_p = df_p.append(df_final_p)




#writer = pd.ExcelWriter('C:/Users/kkim/Documents/Python/TEST/sk_clm27042021.xlsx', engine='xlsxwriter')

'''
for i in range(len(df7)):
 #   for j in range(len(df_p)):
    #df_p.iloc[0:,0] = df5.iloc[i, 1]
    df_p['User_p' + str(i)] = df7.iloc[i, 1]
    df_final_p['User_s' + str(i)] = df7.iloc[i, 1]
    df_user['User_a' + str(i)] = df7.iloc[i, 1]
'''
# df_p['UserOrGroupId'].append(df_p.iloc[:,4+i:])
   # df_p['UserOrGroupId'] = pd.concat(df_p['UserOrGroupId'], df5.iloc[i, 1])
 # Write each dataframe to a different worksheet.
#df_p.to_excel(writer, sheet_name='Sheet1', index=False)

#writer.save()

#df_user.to_excel('C:/Users/kkim/Documents/Python/TEST/sk_clm' + d1 + '.xlsx', index=False)



