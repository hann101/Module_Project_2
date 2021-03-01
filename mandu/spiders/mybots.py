import scrapy
from mandu.items import ManduItem


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    custom_settings = {'JOBDIR': 'crawl_mybots1'}
    allowed_domains = ['finance.yahoo.com/quote/005930.KS']
# https://finance.daum.net/quotes/A032640?period=day#home

    start_urls = ['https://finance.yahoo.com/quote/005930.KS']
# https://finance.yahoo.com/quote/005930.KS    

    def parse(self, response):
        
        title = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1/text()').extract()
        price = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()').extract()
        day_range = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]/text()').extract()
        volume = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/span/text()').extract()
        # 각각의 파싱된 값을 단일 리스트로 대입
        #['82,000.00 - 83,400.00']
        #['Samsung Electronics Co., Ltd. (005930.KS)']

        # name = title[0].split(",")[0]
        # num = title[0].split(",")[1]
        # num = num.replace(' Ltd. (','')
        # num = num.replace(')','')
        # # 주식명 / 코드번호 전처리
        # lowest_price = day_range[0].split(' - ')[0]
        # highest_price = day_range[0].split(' - ')[1]
        # # 최고가 / 최저가 전처리

      
        items = []
        for idx in zip(title,price,day_range,volume):
            item = ManduItem()
            #아이템 인스턴스화 items.py에 있는 item들을 가져와 사용하는 것.
            item['name'] = idx[0].split(' Ltd. (')[0]
            item['num'] = idx[0].split(' Ltd. (')[1].replace(')',"")
            #idx[0]에는  ['Samsung Electronics Co., Ltd. (005930.KS)']값이 들어 있음.
            #item['title']에 대입을 하게 되면 {'title':'Samsung Electronics Co., Ltd. (005930.KS)'}형태의 dict 타입으로 저장됨 -> zip사용법
            # ex) zip('title','Samsung Electronic')이라고 입력하면 {'title':'Samsung Electronic'}이라는 dict 타입으로 저장 -> 반드시 리스트나 튜플에 대입해야함.
            item['price'] = idx[1]
            item['lowest_price'] = idx[2].split(' - ')[0]
            item['highet_price'] = idx[2].split(' - ')[1]
            item['volume'] = idx[3]


        items.append(item)
        #items라는 리스트에 item 리스트들을 추가한다.
        print("-------------------------")
        print(items)
        print("-------------------------")
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