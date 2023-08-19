# Web Scraping Performance Comparison

This repository aims to compare the performance of various web scraping methods. Web scraping can be achieved through numerous approaches, each having its own advantages and pitfalls. The goal here is to provide a clear, side-by-side comparison of the execution time, simplicity, and readability of the following methods:

1. Asynchronous using `httpx`
2. Asynchronous adaptation of `requests`
3. Synchronous (normal) using `requests`
4. Multi-threaded using `requests` 

## Setup

Before running the scripts, make sure you have the required packages installed. 
```
pip install requests httpx beautifulsoup4
```

## Scripts

### 1. `async_httpx.py`

This script utilizes the `httpx` library, which supports asynchronous HTTP requests out of the box. This is beneficial for I/O bound tasks like web scraping, as it allows other tasks to run concurrently during waiting times.

### 2. `async_requests.py`

Though `requests` is inherently synchronous, this script demonstrates how you can integrate `requests` within an asyncio loop using executors. This might be handy if you have an existing `requests` based solution and want to add some concurrency without switching to another library.

### 3. `normal_requests.py`

This script provides a straightforward, synchronous approach to web scraping using the popular `requests` library. It's simple and often readable, but can be slower than concurrent methods for fetching multiple URLs.

### 4. `threading_requests.py`

Leveraging Python's threading capabilities, this script spins up multiple threads to scrape web pages concurrently. This method can yield a significant speedup for I/O bound tasks, like fetching web pages, as it allows multiple requests to be made simultaneously.

## Performance Results

To get a quick comparison of the performance of these methods:
```
4.056387099999999s python async_httpx.py
4.1512801999999995s python async_requests.py
26.6382653s python normal_requests.py
4.365902s python threading_requests.py
```

Remember, the actual times can vary based on network speed, server response time, and other external factors. However, this comparison should provide a general idea of the efficiency of each method.

## Conclusions

- **Asynchronous methods** (`async_httpx.py` and `async_requests.py`) generally provide good performance improvements, especially when there's a need to fetch multiple URLs or wait for responses.
  
- **Synchronous method** (`normal_requests.py`) is the most straightforward and can be the easiest to read and write, but may not be the most efficient for scraping large amounts of data.

- **Threading** (`threading_requests.py`) is a powerful way to add concurrency to the scraping process and can yield good performance improvements. However, it comes with its own set of challenges, like managing shared resources and potential race conditions.

Choose the method that best fits your specific use-case and infrastructure!
