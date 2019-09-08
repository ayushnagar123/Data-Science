scrapy shell 'http://quotes.toscrape.com/page/1/'

2019-09-08 22:03:30 [scrapy.utils.log] INFO: Scrapy 1.7.3 started (bot: scrapybot)2019-09-08 22:03:30 [scrapy.utils.log] INFO: Versions: lxml 4.4.1.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 19.7.0, Python 3.6.8 (default, Jan 14 2019, 11:02:34) - [GCC 8.0.1 20180414 (experimental) [trunk revision 259383]], pyOpenSSL 19.0.0 (OpenSSL 1.1.1c  28 May 2019), cryptography 2.7, Platform Linux-4.15.0-29-generic-x86_64-with-Ubuntu-18.04-bionic
2019-09-08 22:03:30 [scrapy.crawler] INFO: Overridden settings: {'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter', 'LOGSTATS_INTERVAL': 0}
2019-09-08 22:03:30 [scrapy.extensions.telnet] INFO: Telnet Password: 7c718eae035cb548
2019-09-08 22:03:30 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage']
2019-09-08 22:03:30 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2019-09-08 22:03:30 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2019-09-08 22:03:30 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2019-09-08 22:03:30 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2019-09-08 22:03:30 [scrapy.core.engine] INFO: Spider opened
2019-09-08 22:03:31 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x7f1de607d828>
[s]   item       {}
[s]   request    <GET http://quotes.toscrape.com/page/1/>
[s]   response   <200 http://quotes.toscrape.com/page/1/>
[s]   settings   <scrapy.settings.Settings object at 0x7f1de49ee710>
[s]   spider     <DefaultSpider 'default' at 0x7f1de3f5e080>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser

In [1]: response
Out[1]: <200 http://quotes.toscrape.com/page/1/>

In [2]: response.css('title')
Out[2]: [<Selector xpath='descendant-or-self::ti
tle' data='<title>Quotes to Scrape</title>'>]

In [3]: response.css('title').getall()
Out[3]: ['<title>Quotes to Scrape</title>']

In [4]: response.css('title::text').getall()
Out[4]: ['Quotes to Scrape']

In [5]: response.css('title::text').get()
Out[5]: 'Quotes to Scrape'

In [6]: response.css('div.quote')
Out[6]: 
[<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>]

In [7]: response.css('div.quote').get()
Out[7]: '<div class="quote" itemscope itemtype="http://schema.org/CreativeWork">\n        <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>\n        <span>by <small class="author" itemprop="author">Albert Einstein</small>\n        <a href="/author/Albert-Einstein">(about)</a>\n        </span>\n        <div class="tags">\n            Tags:\n            <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world"> \n            \n            <a class="tag" href="/tag/change/page/1/">change</a>\n            \n            <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>\n            \n            <a class="tag" href="/tag/thinking/page/1/">thinking</a>\n            \n            <a class="tag" href="/tag/world/page/1/">world</a>\n            \n        </div>\n    </div>'

In [8]: quote = response.css('div.quote').get()

In [9]: title = quote.css("span.text")
------------------------------------------------
AttributeError Traceback (most recent call last)
<ipython-input-9-0c07112bf228> in <module>()
----> 1 title = quote.css("span.text")

AttributeError: 'str' object has no attribute 'css'

In [10]: quote = response.css('div.quote')[0]

In [11]: title = quote.css("span.text").get()

In [12]: print(title)
<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>

In [13]: author = quote.css('small.author::text'
    ...: ).get()

In [14]: print(author)
Albert Einstein

In [15]: tags = quote.css('a.tag::text').getall(
    ...: )

In [16]: print(tag)
------------------------------------------------
NameError      Traceback (most recent call last)
<ipython-input-16-ba3fa5a0bbfd> in <module>()
----> 1 print(tag)

NameError: name 'tag' is not defined

In [17]: print(tags)
['change', 'deep-thoughts', 'thinking', 'world']

In [18]: for q in response.css(div.quote):
    ...:     text = quote.css("span.text::text")
    ...: .get()
    ...: 
------------------------------------------------
NameError      Traceback (most recent call last)
<ipython-input-18-d60a7cfbaa4b> in <module>()
----> 1 for q in response.css(div.quote):
      2     text = quote.css("span.text::text").get()

NameError: name 'div' is not defined

In [19]: for q in response.css('div.quote'):
    ...:     text = quote.css("span.text::text")
    ...: .get()
    ...: 

In [20]: print(text)
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”

In [21]: for q in response.css('div.quote'):
    ...:     text = quote.css("span.text::text")
    ...: .get()
    ...:     print(text)
    ...: 
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”

In [22]: for q in response.css('div.quote'):
    ...:     text = q.css("span.text::text").get
    ...: ()
    ...:     print(text)
    ...: 
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“It is our choices, Harry, that show what we truly are, far more than our abilities.”
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
“Try not to become a man of success. Rather become a man of value.”
“It is better to be hated for what you are than to be loved for what you are not.”
“I have not failed. I've just found 10,000 ways that won't work.”
“A woman is like a tea bag; you never know how strong it is until it's in hot water.”
“A day without sunshine is like, you know, night.”

In [23]: 