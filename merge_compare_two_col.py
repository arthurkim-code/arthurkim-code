import pandas as pd

excel_url = '/users/kkim/PycharmProjects/arthurkim-code/merge_v1.xlsx' #Input ex files
excel_url1 = '/users/kkim/PycharmProjects/arthurkim-code/merge_v1.1.xlsx' #Input ex files
excel_export = '/users/kkim/PycharmProjects/arthurkim-code/merge_export.csv' #Input ex files

# excel_url1 = '/Users/kkim/PycharmProjects/code_storage/ims_test.xlsx' #Input ims files

df1 = pd.read_excel(excel_url)  # read ex sheet
df2 = pd.read_excel(excel_url1)  # read ex sheet

df3 = pd.merge(df1, df2, on='hcp', how='outer', indicator=True)
# df4 = df3['jims_hco'].isin(df3['ic_hco']).to_list()
# df3 = df3.drop_duplicates()
# df4 = df3[['hcp','ic_hco']]

# df5 = df3.compare(df4, align_axis=0)
# print(df3)
# print(df1, df2, df3)

df3['compare_result'] = df3['jims_hco'] == df3['ic_hco']

# 결과 출력
df4=df3[['hcp', 'jims_hco', 'ic_hco', 'compare_result']]

df4.to_csv(excel_export, index=False) #export ex to csv
# df30.to_csv(excel_export1, index=False) #export ims to csv