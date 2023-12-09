# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:27:17 2020

@author: kkim
"""
import pandas as pd

excel_url = 'C:/Users/kkim/Documents/Python/TEST/book3.xlsx' #read master file

df1 = pd.read_excel(excel_url, sheet_name = 'Universe')  # read each sheet
df2 = pd.read_excel(excel_url, sheet_name = 'Sheet4')

df1['First'] = df1['Dropped Territories'].str.replace(";"," ") # first user's territory extraction in drop list

##if there are parent territory, it will be used by the below code

#df1['First'] = df1['Dropped Territories'].str.split(';').str[0] # first user extraction in drop list
#df1['Second'] = df1['Dropped Territories'].str.split(';').str[1] # second user extraction in drop list

df1['Dropped Territories'] = df1['Dropped Territories'].str.replace(";"," ") #  remove ; in drop list
df1['Added Territories'] = df1['Added Territories'].str.replace(";"," ") #  remove ; in add list
df1['Territories'] = df1['Territories'].str.replace(";"," ") #  remove ;  in current territory
#df1['Cleanup'] = df1.Territories.str.replace('|'.join(str(df1.First))," ") # first user remove
#drop_user = 'Stealth팀_박수현'

df1['Cleanup'] = df1['Territories'].replace(df1['First'],' ', regex=True) # Remove first(drop) user's territory

#df1['Cleanup1'] = df1.Cleanup.str.replace('|'.join(str(df1.Second)),'') # Remove second(parent) user's territory
df1['Territory_check'] = df1['Cleanup'] + df1['Added Territories'] # after removing the drop user and add the user in add list.
df1['Territory_check'] = df1['Territory_check'].str.replace(" ",";")
df1['ADD'] = df1['Added Territories'].str.strip()

df3 = pd.merge(df2, df1[['Customer Alignment Rule ID','ADD','First','Territory_check']], on='Customer Alignment Rule ID', how='left')
#Merge between former CAR and current CAR to verify the result

df3['ADD_check'] = df3.apply(lambda row : str(row['ADD']) in str(row['Territories']), axis=1) #Verify that ADD territory is exist
df3['Drop_check'] = df3.apply(lambda row : str(row['First']) not in str(row['Territories']), axis=1) #Verify that Drop territory is dropped

df3.to_excel('C:/Users/kkim/Documents/Python/TEST/book0108.xlsx', index=False)
# to excel the comparison excel

