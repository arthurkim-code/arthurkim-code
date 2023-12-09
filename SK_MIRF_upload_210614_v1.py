import os, csv
from datetime import date
import pandas as pd

today = date.today()
d1 = today.strftime("%d%m%Y")
excel_url = 'C:/Users/kkim/Documents/Python/TEST/a_모더나코비드-19백신주_202106.xlsx' #excel upload_file from SK
excel_url1 = 'C:/Users/kkim/Documents/Python/TEST/b_코로나19_202106.xlsx' #excel upload_file from SK
#excel_url2 = 'C:/Users/kkim/Documents/Python/TEST/a_모더나코비드-19백신주_202106.xlsx' #excel upload_file from SK
#excel_url3 = 'C:/Users/kkim/Documents/Python/TEST/a_모더나코비드-19백신주_202106.xlsx' #excel upload_file from SK

#excel_template = 'C:/Users/kkim/Documents/Python/TEST/Medical Inquiry Data Template_v1.xlsx' #excel template for merging

writer = pd.ExcelWriter('C:/Users/kkim/Documents/Python/TEST/Medical Inquiry Data Template_v1.xlsx', engine='xlsxwriter')

file_excel = 'C:/Users/kkim/Documents/Python/TEST/Medical Inquiry Data Template_v1.xlsx'
#file_url = 'C:/Users/kkim/Documents/SK_MIRF_test/MIRF_attachments_v1.csv' #file rename template
#file_url1 = 'C:/Users/kkim/Documents/SK_MIRF_test/' #file path for chaning the file name

df100 = pd.read_excel(file_excel, sheet_name = '메디컬문의 파일업로드 템플릿')
#df2 = pd.read_excel(excel_template, sheet_name = '메디컬문의 파일업로드 템플릿')
df_a = pd.read_excel(excel_url, sheet_name = '메디컬문의 업로드템플릿') #업로드 내용
df_a1 = pd.read_excel(excel_url, sheet_name = '메디컬문의 파일업로드 템플릿') # 파일 업로드 내용
df_b = pd.read_excel(excel_url1, sheet_name = '메디컬문의 업로드템플릿')
df_b1 = pd.read_excel(excel_url1, sheet_name = '메디컬문의 파일업로드 템플릿')

df1 = pd.concat([df_a, df_b]) # 업로드 내용 합치기
df2 = pd.concat([df_a1, df_b1]) # 파일 업로드 내용 합치기

df1['질문'] = '[' + df1['제품'] + ']' + df1['질문'] # 질문에 제품명 더하기

#df1.to_excel('C:/Users/kkim/Documents/Python/TEST/MIRF_' + d1 + '.xlsx', index=False)

df_rename = df2['ParentId'] + df2["Body"].str[-7:]

df2['Rename'] = df_rename
df2['Renamepath'] = './' + df_rename

df1.to_excel(writer, sheet_name='메디컬문의 업로드템플릿', index=False)
df2.to_excel(writer, sheet_name='메디컬문의 파일업로드 템플릿', index=False)
#df5.to_excel(writer, sheet_name='Sheet4', index=False)
#df6.to_excel(writer, sheet_name='Sheet5', index=False)
writer.save()

df100.to_csv('C:/Users/kkim/Documents/Python/TEST/Medical Inquiry Data Template_v1.csv', encoding='utf_8_sig') #file rename 위한 csv 변경

file_url = 'C:/Users/kkim/Documents/Python/TEST/Medical Inquiry Data Template_v1.csv' #rename template
file_url1 = 'C:/Users/kkim/Documents/SK_MIRF_test/attach/' #파일 변경할 directory

#파일 이름 Rename
with open(file_url, encoding='utf_8_sig', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        src_file_name = file_url1 + row['Name']
        dst = file_url1 + row['Rename']
        os.rename(src_file_name, dst) #rename