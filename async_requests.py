import time
import asyncio
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


async def get_results():
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(None, fetch_url, url) for url in urls]
    all_links = await asyncio.gather(*futures)
    print(all_links)

start = time.perf_counter()
asyncio.run(get_results())
end = time.perf_counter()
print(end - start)
