import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='b23baoqiq6',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

sql = "select * from interest;"
cur.execute(sql)
one_row = cur.fetchone()
print(one_row)

cur.close()
db.close()