import time
import requests
from bs4 import BeautifulSoup as bs

urls = [
    f"https://books.toscrape.com/catalogue/page-{i}.html" for i in range(1, 50)
]


def fetch_url(url):
    response = requests.get(url)
    soup = bs(response.text, "lxml")
    links = [link.find('a')['href'] for link in soup.findAll(
        'article', {'class': 'product_pod'})]
    return links


def get_results():
    all_links = []
    for url in urls:
        all_links.extend(fetch_url(url))
    print(all_links)


start = time.perf_counter()
get_results()
end = time.perf_counter()
print(end-start)
