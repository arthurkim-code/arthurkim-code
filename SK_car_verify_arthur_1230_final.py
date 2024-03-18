# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:27:17 2020

@author: kkim
"""
import pandas as pd

excel_url = 'C:/Users/kkim/Documents/Python/TEST/book2.xlsx'

df1 = pd.read_excel(excel_url, sheet_name = 'Universe')  # read each sheet
df2 = pd.read_excel(excel_url, sheet_name = 'Sheet4')

df1['First'] = df1['Dropped Territories'].str.split(';').str[0] # first user extraction in drop list
df1['Second'] = df1['Dropped Territories'].str.split(';').str[1] # second user extraction in drop list

df1['Dropped Territories'] = df1['Dropped Territories'].str.replace(";"," ") # ; remove in drop list
df1['Added Territories'] = df1['Added Territories'].str.replace(";"," ") # ; remove in add list
df1['Territories'] = df1['Territories'].str.replace(";"," ") # ; remove in current territory
df1['Cleanup'] = df1.Territories.str.replace('|'.join(str(df1.First)),'') # first user remove
df1['Cleanup1'] = df1.Cleanup.str.replace('|'.join(str(df1.Second)),'') # second user remove
df1['Final'] = df1['Cleanup1'] + df1['Added Territories'] # after removing the drop user and add the user in add list.
df1['Final'] = ";" + df1['Final'].str.replace(" ",";") + ";"

df3 = pd.merge(df2, df1[['Customer Alignment Rule ID','Final']], on='Customer Alignment Rule ID', how='left')

# current CAR and compare with the final list after dropping and adding users

df3.to_excel('C:/Users/kkim/Documents/Python/TEST/book100.xlsx', index=False)

# to excel the comparison excel
