from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookItem

def write_to_file(self, book_item):
    with open('payload.txt', 'w') as payload:
        payload.write(book_item["title"])
        payload.write(book_item["price"])
    return payload


class BookScraper(CrawlSpider):
    name = "bookscraper"
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_book")
    )

    def parse_book(self, response):
        book_item = BookItem()

        with open('payload.txt','w') as payload:

            book_item["image_url"] = response.urljoin(response.css(".item.active > img::attr(src)").get())
            book_item["title"] = response.css(".col-sm-6.product_main > h1::text").get()
            book_item["price"] = response.css(".price_color::text").get()
            book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
            book_item["url"] = response.url

            payload.write(book_item['title'] + '\n')
            payload.write(book_item['price'] + '\n')
            payload.write(book_item['upc'] + '\n')
            
            return book_item


