from selectorlib import Extractor
import requests 
import csv
from time import sleep

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('search_results.yml')

def scrape(url):  
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s" % url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (url, r.status_code))
        return None
    # Pass the HTML of the page and create
    return e.extract(r.text)

def generate_urls(product_name, num_pages):
    base_url = "https://www.amazon.com/s?k="
    urls = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}{product_name}&page={page}"
        urls.append(url)
    return urls

def main():
    product_name = input("Enter the product name: ").replace(" ", "+")
    num_pages = int(input("Enter the number of pages to scrape: "))
    
    urls = generate_urls(product_name, num_pages)

    # Open the CSV file for writing
    with open('search_results_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'url', 'rating', 'price', 'search_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Process each URL
        for url in urls:
            data = scrape(url)
            if data and 'products' in data:
                for product in data['products']:
                    product['search_url'] = url
                    print("Saving Product: %s" % product['title'])
                    # Remove reviews field if it exists
                    product.pop('reviews', None)
                    # Write the product data to the CSV file
                    writer.writerow(product)
                    # sleep(5)
            else:
                print(f"No data found for {url}")

if __name__ == "__main__":
    main()
