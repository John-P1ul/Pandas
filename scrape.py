import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import time

base_url = 
 

def scrape_page(url):
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page, status code: {response.status_code}")
        return []
    

    products = []
    content = BeautifulSoup(response.text, 'html.parser')
    
    for x in content.find_all("li", {"class": "s-item s-item__pl-on-bottom"}):
        check = x.find("span", {"role": "heading"})
        name = check.text.strip()
        y = x.find("span", {"class": "s-item__price"})
        price = y.text.strip()
        link = x.find('a')
        if link:
            y =  link.get('href')
        
            
            product = {
                'Title': name,
                'Price': price,
                'Link': link,
            }
            
            products.append(product)
            
            print(f"Scraped product: {name} | Price: {price} | Url: {link}")
        
    
    

def scrape_multiple_pages(base_url, num_pages=6):
    all_products = []
    
    for page_number in range(1, num_pages + 1):
        url = f"{base_url}?page={page_number}#catalog-listing"
        products = scrape_page(url)
        all_products.extend(products)
        time.sleep(1) 
    
    return all_products

products = scrape_multiple_pages(base_url, num_pages=10)

df = pd.DataFrame(products)
df
df.to_csv('iphone.csv')
df.to_excel('iphone.xlsx')