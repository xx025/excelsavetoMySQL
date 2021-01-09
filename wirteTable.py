# @File    : creat.py
from src.conneMySQL import connect_mysql


def writetable(list, table_name, *database):
    con = connect_mysql()
    con.con(database[0])
    print(con.qure("show tables"))
    for rol in list[1:]:
        sql = '''insert into\t {}\t values {} '''.format(table_name, tuple(str(i) for i in rol))
        con.update(sql)
    con.close()
