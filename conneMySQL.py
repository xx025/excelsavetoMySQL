# @File    : conneMySQL.py
# https://blog.csdn.net/linshijun33/article/details/88677305
# 建库建表

import pymysql


class connect_mysql:
    def __init__(self, host="localhost", user="root", port=3306, password="root"):
        self.user = user
        self.port = port
        self.password = password
        self.host = host

    # 建立连接
    def con(self, *args):
        try:
            if args.__len__() > 0:
                self.db = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.password, database=args[0])
            else:
                self.db = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.password)

            self.cursor = self.db.cursor()
        except:
            print("建立连接失败！")

    # 关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()

    # 查询
    def qure(self, sql):
        result = tuple()
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except:
            print("查询失败！")
        finally:
            return result

    # 更新
    def update(self, sql):
        count = 0
        try:
            count = self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            print(sql)
            print("操作失败！")
            self.db.rollback()
        finally:
            return count


# connect = connect_mysql()

# connect.con()
#
# print(connect.qure("show databases"))#查询数据库
# connect.close()
#

# connect.con("db1")
# print(connect.qure("show tables"))  # 查询表格
# connect.close()

# connect.con("db1")
# print(connect.update("create table stuuu( id int)"))
# print(connect.qure("show tables"))  # 查询表格
# connect.close()
