import pymysql


class Login:
    def __init__(self,
                 database='stu',
                 host='localhost',
                 user='root',
                 password='b23baoqiq6',
                 port=3306,
                 charset='utf8',
                 table='user'):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        self.table = table

        self.connect_db()
        self.db = None
        self.cur = None

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.password,
                                  database=self.database,
                                  charset=self.charset)
        self.cur = self.db.cursor()

    def close_db(self):
        self.cur.close()
        self.db.close()

    def register(self, username, password):
        sql = "select * from %s where username='%s' and password='%s'" % (self.table, username, password)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return False

        sql = "insert into %s(username,password) values('%s','%s');" % (self.table, username, password)
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
            return False

        return True

    def login(self, username, password):
        sql = "select * from %s where username='%s' and password='%s'" % (self.table, username, password)
        try:
            self.cur.execute(sql)
            self.db.commit()
            if self.cur.fetchone():
                return True
            else:
                return False
        except Exception as e:
            self.db.rollback()
            print(e)
            return False
