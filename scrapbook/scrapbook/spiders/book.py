import scrapy

books=[]
class BooksSpider(scrapy.Spider):
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
            # image = scrapy.Request(url=image_url)
            image_title = q.css('h3 a::attr(title)').get()
            filename = '%s.jpg' % image_title.replace(' ','_')
            title = q.css('h3 a::attr(title)').get()
            price = q.css('div.product_price p.price_color::text').get()

            # with open('images/'+filename, 'wb') as f:
            #     f.write(image)
            # self.log('Saved file %s' % filename)

            books.append({
                'image_url':image_url,
                'title':title,
                'price':price,
            })
        next_page = response.css('li.next a::attr(href)').get()
        if(next_page is not None):
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
        
        column_title = ""
        for i,prod in enumerate(books):
            if(i==0):
                for j,title in  enumerate(prod.keys()):
                    if(j<len(prod.keys())-1):
                        if(',' in title):
                            title='"'+title+"'"
                            column_title+=title+','
                    else:
                        if(',' in title):
                            title="'"+title+"'"
                        column_title+=title
                        break

        with open('book.csv','w') as f:
            f.write(column_title+'\n')
            for i,prod in enumerate(books):
                values=""
                for i,val in enumerate(prod.values()):
                    if(i<len(prod.values())-1):
                        if(',' in val):
                            val='\"'+val+'"'
                        values+=val+','
                    else:
                        if(',' in val):
                            val='\"'+val+'"'
                        values+=val
                        break
                f.write(values+'\n')