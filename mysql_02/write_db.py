import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='b23baoqiq6',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

try:
    # 插入
    # sql = "insert into interest values(2,'Abby','sing,dance','S',998,'Good...');"
    # cur.execute(sql)

    # 修改
    sql = "update interest set price=666 where name='Abby';"
    cur.execute(sql)

    db.commit()
except Exception as e:
    db.rollback()
    print(e)


cur.close()
db.close()
