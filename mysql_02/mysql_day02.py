import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='b23baoqiq6',
                     database='stu',
                     charset='utf8')
# 获取游标
cur = db.cursor()
# 数据库操作
# cur.execute("select * from class_1;")
cur.execute("insert into class_1 \
            values (3,'Tim', 28, 91, 'm');")

# 提交到数据库执行
db.commit()

# 关闭游标和数据库连接
cur.close()
db.close()