import scrapy
from demo.items import DemoItem


class DomzSpider(scrapy.Spider):
    name = 'linuxdown'
    allow_domains = ["linuxdown.net"]
    start_urls = [
        "http://www.linuxdown.net/soft/"
    ]

    def parse(self, response):
        with open('st.txt', 'a') as f:
            for info in response.xpath("//div[@class='listbox']/ul//li"):
                item = DemoItem()
                names = info.xpath("a[@class='title']/text()").extract()
                if not  names:
                    continue
                item['name'] = names[0]
                item['link'] = info.xpath("a[@class='title']/@href").extract()[0]
                item['img'] = info.xpath("a[@class='preview']/img/@src").extract()[0]
                item['update_date'] = info.xpath("span/text()").extract()[1].strip()
                item['hot'] = info.xpath("span/text()").extract()[2].strip()
                yield item
                f.write(item['name']+'\n')

        page_info = response.xpath("//ul[@class='pagelist']")
        page_sum = page_info.xpath("li/span[@class='pageinfo']/strong[1]/text()").extract()[0]
        this_page = page_info.xpath("li[@class='thisclass']/text()").extract()[0]
        if int(this_page) == int(page_sum):
            return 0
        next_page = page_info.xpath(".//li/a")[-2].xpath('./@href').extract()
        next_page_url = self.start_urls[0]+next_page[0]
        yield scrapy.Request(next_page_url, self.parse)
