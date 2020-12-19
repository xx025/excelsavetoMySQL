# @File    : creat.py
from conneMySQL import connect_mysql
from readExcel import readexcel

list=readexcel("18.xls")
con=connect_mysql()
con.con("ldu_student_information")
print(con.qure("show tables"))
for rol in list[1:]:
    sql='''insert into informationof18thgrade
            values {} '''.format(tuple( str(i)for i in rol))
    con.update(sql)
con.close()