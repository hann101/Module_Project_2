# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class ManduPipeline:
    def __init__(self):
        self.setupDBConnect()
        #인스턴스가 만들어 질때 
        self.createTable()



    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1',user='root',password='123',db='mydb',charset='utf8')
        self.cur = self.conn.cursor()
        print("DB Connected")




    def createTable(self):
        # self.cur.execute("DROP TABLE IF EXISTS stock_info")
        # 이걸 주석처리 안해서 db에 저장이 안되었음.
        # 지우고 만들고 반복했기 때문임.

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS stock_info(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name varchar(100),
            num varchar(100),
            price VARCHAR(100),
            lowest_price VARCHAR(100),
            highest_price VARCHAR(100),
            volume VARCHAR(100),
            created_at DATETIME DEFAULT NOW()
            )''')

        



    def process_item(self, item, spider):
        self.storeInDb(item)
        return item



    def storeInDb(self,item):
        #각아이템을 table에 저장
        sql = ''' 
        INSERT INTO stock_info(name, num, price, lowest_price, highest_price, volume) VALUES(%s,%s,%s,%s,%s,%s)
        '''
        self.cur.execute(sql,(\

            item.get('name','').strip(),
            item.get('num','').strip(),

            item.get('price','').strip(),
            item.get('lowest_price','').strip(),
            item.get('highet_price','').strip(),
            item.get('volume','').strip()
            ))
        print('Data stored in DB')
        self.conn.commit()
        


