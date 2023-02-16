import pandas as pd
import dask.dataframe as dd
import requests
from tqdm import tqdm

def get_json_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    return json_data

def main():
    urls = []
    headers = ["name", "state", "city", "email"]
    final_data = []
    for url in tqdm(urls, desc="Processing links", unit="link"):
        for page in tqdm(range(0,7), desc="Processing pages", total=6, leave=False):
            url_page = url + str(page)
            json_data = get_json_data(url_page)
            for listing in json_data["data"]["listings"]:
                data = {k: listing[k] for k in headers}
                final_data.append(data)
    final_df = dd.from_pandas(pd.DataFrame(final_data, columns=headers), npartitions=1)
    final_df.to_csv('result.csv', index=False, single_file=True, mode='w')

if __name__ == '__main__':
    main()
