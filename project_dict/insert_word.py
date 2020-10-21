import pymysql
import re

f = open('dict.txt', 'r')
db = pymysql.connect('localhost', 'root', 'b23baoqiq6', 'stu')
cur = db.cursor()

sql = 'insert into dict_t (word, mean) values("%s", "%s");'
for line in f:
    tup = re.findall(r'(\w+)\s+(.*)', line)[0]

    try:
        cur.execute(sql, tup)
        db.commit()
    except Exception:
        db.rollback()

f.close()
cur.close()
db.close()
