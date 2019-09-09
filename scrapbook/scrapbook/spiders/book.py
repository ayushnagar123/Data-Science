import scrapy


class QuotesSpider(scrapy.Spider):
    name = "book"

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        for q in response.css('section div ol.row li article.product_pod'):
            image_url = q.css('a img::attr(src)').get()
            image_title = q.css('h3 a::attr(title)').get()
            filename = '%s.jpeg' % image_title
            title = q.css('h3 a::text').get()
            price = q.css('div.product_price p.price_color::text').get()

            with open('images/'+filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)

            yield{
                'image_url':image_url,
                'title':title,
                'price':price,
            }
        
        next_page = response.css('li.next a::attr(href)').get()
        if(next_page is not None):
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
        
        # with open('book.json','r'):

        