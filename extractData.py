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
    urls = [
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=61.154052734375%2C-149.7342224121094&latlng=61.154052734375%2C-149.7342224121094&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals",
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=64.83741760253906%2C-147.7051696777344&latlng=64.83741760253906%2C-147.7051696777344&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals",
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=60.92319869995117%2C-148.9273071289062&latlng=60.92319869995117%2C-148.9273071289062&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals",
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=58.35790634155273%2C-134.4804382324219&latlng=58.35790634155273%2C-134.4804382324219&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals",
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=60.52611541748047%2C-150.5313262939453&latlng=60.52611541748047%2C-150.5313262939453&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals",
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=55.58583831787109%2C-130.9355163574219&latlng=55.58583831787109%2C-130.9355163574219&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals",
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=61.57063674926758%2C-149.4447784423828&latlng=61.57063674926758%2C-149.4447784423828&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals",
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=56.98958206176758%2C-135.0790252685547&latlng=56.98958206176758%2C-135.0790252685547&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals",
"https://api-g.weedmaps.com/discovery/v2/listings?sort_by=position_distance&filter%5Bany_retailer_services%5D%5B%5D=storefront&filter%5Bbounding_radius%5D=75mi&filter%5Bbounding_latlng%5D=61.09523010253906%2C-146.3056182861328&latlng=61.09523010253906%2C-146.3056182861328&page_size=100&page=1&include%5B%5D=facets.has_curbside_pickup&include%5B%5D=facets.retailer_services&include%5B%5D=listings.top_deals"]


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
    final_df.to_csv('result.csv', index=False, single_file=True, mode='a')

if __name__ == '__main__':
    main()