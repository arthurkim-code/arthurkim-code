import pandas as pd

excel_url = '/users/kkim/PycharmProjects/arthurkim-code/ic_account.xlsx' #Input ex files
excel_url1 = '/users/kkim/PycharmProjects/arthurkim-code/sf_account.xlsx' #Input ex files
excel_export = '/users/kkim/PycharmProjects/arthurkim-code/merge_export.xlsx' #Input ex files

# excel_url1 = '/Users/kkim/PycharmProjects/code_storage/ims_test.xlsx' #Input ims files

df1 = pd.read_excel(excel_url)  # read ex sheet
df2 = pd.read_excel(excel_url1)  # read ex sheet

df3 = pd.merge(df2, df1, on='id', how='left', indicator=True)
# df4 = df3['jims_hco'].isin(df3['ic_hco']).to_list()
# df3 = df3.drop_duplicates()
# df4 = df3[['hcp','ic_hco']]

# df5 = df3.compare(df4, align_axis=0)
# print(df3)
# print(df1, df2)

df3['compare_result'] = df3['JJ_IMS_WKP_NUMBER__c'] == df3['jj_ims_wkp_number__c1'] #check the parent account is matched between two apps

# 결과 출력
# df4=df3[['hcp', 'jims_hco', 'ic_hco', 'compare_result']]

df3.to_excel(excel_export, index=False) #export ex to csv
# df30.to_csv(excel_export1, index=False) #export ims to csv