import json
import pandas as pd
import requests
from io import StringIO
import os
from time import sleep

def add_to_excel(df_list,sheet,file_name,spaces):
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')
    col = 0
    for dataframe in df_list:
        dataframe.rename(columns={'Unnamed: 0':''},inplace=True)
        dataframe_to_insert = dataframe.iloc[[2]]
        dataframe_to_insert.to_excel(writer,sheet_name=sheet,startcol=col, startrow=0, index=False)   
        col = col + len(dataframe.columns) + spaces + 1
    writer.close()


def download_data_from_urls():
    with open('company_url.json','r') as f:
        company_url = json.load(f)

    if not os.path.exists('./company_database'):
        os.mkdir('./company_database')

    for company_name,url in company_url.items():
        html = requests.get(url).text
        tables = pd.read_html(StringIO(html))[:2]
        path = './company_database/'+company_name.replace(' ','_').replace('.','')+'.xlsx'
        add_to_excel(tables,'Operating Profits',path,1)
        print(f"Company {company_name}'s operating profit is added to the database")
        sleep(2)