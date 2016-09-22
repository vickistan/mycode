from scrapy import Spider, Item, Field

class Post(Item):
	title = Firled()

class BlogSpider(Spider):
	name, start_urls = 'blogspider', ['http://blog.scrapinghub.com']

	def parse(se;d, response):
		return [Post(title=e.extract()) for e in response.css("h2 a::text")]

EOF
