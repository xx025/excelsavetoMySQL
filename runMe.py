# @File    : runMe.py
import os

from createTable import maincreate
from src.conneMySQL import connect_mysql
from src.readExcel import readexcel
from wirteTable import writetable


def inputfipath():
    filepath = input("请输入文件路径：")
    if filepath[0] == "\"" and filepath[-1] == "\"":
        filepath = filepath[1:-1]
        print(filepath)
    return filepath


def main(database):
    while True:
        flag_wt = True
        filepath = inputfipath()

        if os.path.exists(filepath):
            list = readexcel(filepath)
            while flag_wt:
                jal = input("是否创建新的表(是：Y 否：N)：")
                if jal.lower() == "y":
                    table_name = input("输入新的表格名：")
                    maincreate(table_name, list, database)
                    con = connect_mysql()
                    con.con(database)

                    if table_name in con.qure("show tables")[0]:
                        print('\033[0;32m{}\033[0m'.format("创建成功"))
                    else:
                        return False
                    con.close()


                elif jal.lower() == "n":
                    table_name = input("输入要写入表格名：")
                else:
                    print("输入错误")
                    continue
                while True:
                    jal = input("是否将数据写入表格(是：Y 否：N)：")
                    if jal.lower() == "y":
                        writetable(list, table_name, database)
                        flag_wt = False

                        print("写入结束\n\n")
                        break
                    elif jal.lower() == "n":
                        print("结束")
                    else:
                        print("输入错误")
                        continue

        else:
            print("文件不存在")
            continue


if __name__ == '__main__':
    main("test_as")
