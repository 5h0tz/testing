import time
import asyncio
import httpx
from bs4 import BeautifulSoup as bs

urls = [
    f"https://books.toscrape.com/catalogue/page-{i}.html" for i in range(1, 50)
]


async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True)
    soup = bs(response.text, "lxml")
    links = [link.find('a')['href'] for link in soup.findAll(
        'article', {'class': 'product_pod'})]
    return links


async def get_results():
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    all_links = [link for sublist in results for link in sublist]
    print(all_links)

start = time.perf_counter()
asyncio.run(get_results())
end = time.perf_counter()
print(end - start)
