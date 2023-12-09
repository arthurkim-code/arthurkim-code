# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:27:17 2020

@author: kkim
"""
import pandas as pd

excel_url = '/Users/kkim/PycharmProjects/code_storage/ex_test.xlsx' #Input ex files
excel_url1 = '/Users/kkim/PycharmProjects/code_storage/ims_test.xlsx' #Input ims files
excel_export = '/Users/kkim/PycharmProjects/code_storage/ex_test_id_2.csv' #Export to csv of ex
excel_export1 = '/Users/kkim/PycharmProjects/code_storage/ims_test_id_1.csv'#Export to csv of ims

df1 = pd.read_excel(excel_url, sheet_name = 'Prospection Janssen Exfactory_F')  # read ex sheet
df10 = pd.read_excel(excel_url1, sheet_name = 'NU23 - eUnits')  # read ims each sheet
df11 = pd.read_excel(excel_url1, sheet_name = 'NU23 - Units')  # read ims each sheet
df12 = pd.read_excel(excel_url1, sheet_name = 'NU23 - Price')  # read ims each sheet
df13 = pd.read_excel(excel_url1, sheet_name = 'NU23- Patients')  # read ims each sheet
df14 = pd.read_excel(excel_url1, sheet_name = 'NU23 - Value')  # read ims each sheet

concatted_df = pd.concat([df10,df11,df12,df13,df14],ignore_index=True) # merge ims each sheet as one sheet

df2 = pd.melt(df1, id_vars=df1.columns[:6], value_vars=df1.columns[6:],var_name='Date', value_name='Amount') #unpivot ex
df20 = pd.melt(concatted_df , id_vars=concatted_df.columns[:6], value_vars=concatted_df.columns[6:],var_name='Date', value_name='Amount') #unpivot ims

df3=df2.iloc[6:].round(0) # ex round up

col_list = list(df20.columns) #add column name for Col 5
col_list[5] = 'Criteria'
df20.columns = col_list

df20['Date']= pd.to_datetime(df20["Date"]) #ims date field to change the date format
df20['Date']=df20['Date'].dt.strftime("%Y%m")

df30=df20.iloc[8:].round(0) #ims round up

df3.to_csv(excel_export, index=False) #export ex to csv
df30.to_csv(excel_export1, index=False) #export ims to csv

#Metl for date format vertical to horizontality

