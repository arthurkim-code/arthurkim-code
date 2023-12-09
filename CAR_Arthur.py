# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:11:42 2020

@author: kkim
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:26:12 2020

@author: kkim
"""

import pandas as pd
#import numpy as np

excel_url = 'C:/Users/kkim/Documents/1110_Fulldata_v1.xlsx'
#excel_url1 = 'C:/Users/kkim/Documents/old_action_novo.xlsx'

df1 = pd.read_excel(excel_url, sheet_name='Sheet6')

#df1 = df1['Territory'].drop_duplicates(keep='first')

df1['Territories'] = df1.groupby(['Account ID '])['Territories'].transform(lambda x : ';'.join(x)) 

df1 = df1.drop_duplicates(keep='first') 

#for i in df1['Account ID']
#df2 = pd.read_excel(excel_url1)
#df1['Team_worker'] = df1['TEAM'].map(str) + '-'+ df1['DISPLAY_NAME'].map(str)
print(df1)
#print(df2)

#df1 = df1[df1["Territory"] =='KR1121A']
#df2 = df2[df2["Territory"] =='KR1121A']

#df1.drop_duplicates(subset=['IDs', 'Territories'])
#df1['Territories'] = df1.groupby(['IDs'])['Territories'].transform(lambda x : ';'.join(x)) 
  
#df1['IDs'] = df1['IDs'].drop_duplicates()
# drop duplicate data 
#df1['Territories'].drop_duplicates() 
#df1.duplicated('IDs', keep='first')
#df1 = df1[['IDs', 'Territories']]
#df1 = df1.drop_duplicates(keep='first') 

#print(df1)
#df1.to_excel('C:/Users/kkim/Documents/1116_goal.xlsx', index=False)