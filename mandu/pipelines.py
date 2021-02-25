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

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item


    def storeInDb(self,item):
        #각아이템을 table에 저장
        sql = ''' 
        INSERT INTO stock_info(cur_time, dealing, price, max_price, min_price,num) VALUES(%s,%s,%s,%s,%s,%s)
        '''
        self.cur.execute(sql,(\
            item.get('time'),
            item.get('dealing'),
            item.get('price'),
            item.get('max_price'),
            item.get('min_price'),
            item.get('num'),
            ))
        print('Data stored in DB')
        self.conn.commit()
        

        
    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1',user='root',password='123',db='mydb',charset='utf8')
        self.cur = self.conn.cursor()

        print("DB Connected")

    def createTable(self):
        self.cur.execute("DROP TABLE IF EXISTS stock_info")

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS stock_info(
            id INT AUTO_INCREMENT PRIMARY KEY,
            cur_time VARCHAR(40),
            dealing VARCHAR(40),
            price VARCHAR(40),
            max_price VARCHAR(40),
            min_price VARCHAR(40),
            num varchar(40)

            )''')