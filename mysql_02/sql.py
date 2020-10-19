import pymysql

# db = pymysql.connect('localhost', 3306, 'root', 'b23baoqiq6', 'stu', 'utf8')

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='b23baoqiq6',
                     database='stu',
                     charset='utf8')

c = db.cursor()

while True:
    name = input('name:')
    age = input('age：')
    sex = input('sex：')
    score = input('score：')

    # sql = "insert into class_1 (name, age, sex, score) values ('%s', %d, '%s', %f);" % (name, age, sex, score)
    sql = "insert into class_1 (name, age, sex, score) values (%s, %s, %s, %s);"
    try:
        # 自动识别类型
        c.execute(sql, [name, age, sex, score])
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

c.close()
db.close()
