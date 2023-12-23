import json
import pandas as pd

def extract_urls():
    df = pd.read_csv('company_details.csv').fillna(-1)

    company_id_list = [str(int(BSE)) if BSE != -1 else NSE for BSE,NSE in zip(df['BSE Code'],df['NSE Code'])]

    num_company = len(company_id_list)

    print(num_company)

    base_url = 'https://www.screener.in/company/'
    company_url_data = {}

    for company_name,company_id in zip(df['Name'],company_id_list):
        company_url_data[company_name] = base_url + company_id + '/'

    with open('company_url.json','w') as f:
        json.dump(company_url_data,f)

    print(num_company == len(company_url_data))