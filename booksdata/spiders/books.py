import scrapy
from pathlib import Path

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]
    
    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2].split("_")[0]  # Fix the typo here
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
