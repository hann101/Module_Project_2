import scrapy
from mandu.items import ManduItem


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.yahoo.com/quote/005930.KS']
# https://finance.daum.net/quotes/A032640?period=day#home

    start_urls = ['https://finance.yahoo.com/quote/005930.KS']
# https://finance.yahoo.com/quote/005930.KS    

    def parse(self, response):
        print('#'*13)
        time = response.xpath('//*[@id="quote-market-notice"]/span/text()').extract()
        dealing = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/span/text()').extract()
        price = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()').extract()
        
        max_price = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]/text()').extract()
        
        # min_price = response.xpath('//*[@id="boxSummary"]/div/span[2]/ul/li[5]/p/text()').extract()
        num = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1/text()').extract()
      
        items = []
        for idx in range(len(num)):
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
            item = ManduItem()
            item['time'] = time[idx].replace("As of","").replace("KST. Market open.","")
            item['dealing'] = dealing[idx]
            item['price'] = price[idx]
            # ready = max_price[idx].split("-")
            # print(ready)
            item['max_price'] = max_price[idx].split("-")[1]
            item['min_price'] = max_price[idx].split("-")[0]
            item['num'] = num[idx].replace("Samsung Electronics Co., Ltd.","").replace("(","").replace(")","")
            items.append(item)

        return items

#########################################
# def remove(content):
#     result=[]
#     for num in range(len(content)):
#         if len(content[num].strip())>0:
#             result.append(content[num].strip())
#     return result

"""
class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = refer('1')
    #start_urls = ['https://movie.naver.com/movie/point/af/list.nhn?&page=1']
    start_urls = refer('2')
    # 동작은 함수 안에 적어야 해. 여기서 action을 선언하면 구조상 오류가 됨.

    
    def parse(self, response):

        print('#'*13)
        title = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        star = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
        date = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()
        writer = response.css('.author::text').extract()
        content = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/text()').extract()
            
        content = remove(content)

        items = []
        for idx in range(len(title)):
            item = MyscraperItem()
            item['title'] = title[idx]
            item['star'] = star[idx]
            item['date'] = date[idx]
            item['writer'] = writer[idx]
            item['content'] = content[idx]
            items.append(item)

                    

        return items
        # 제목, 평점, 날짜 작성자 내용
"""

## 강사님 코드 보기 (깃허브)