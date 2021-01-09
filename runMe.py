# @File    : runMe.py
import os

from createTable import maincreate
from src.readExcel import readexcel
from wirteTable import writetable


def main(database):
    while True:
        filepath = input("请输入文件路径：")
        if os.path.exists(filepath):
            list = readexcel(filepath)
            while True:
                jal = input("是否创建新的表(是：Y 否：N)：")
                if jal.lower() == "y":
                    table_name = input("输入新的表格名：")
                    maincreate(table_name,list)
                elif jal.lower() == "n":
                    table_name = input("输入要写入表格名：")
                else:
                    print("输入错误")
                    continue
                while True:
                    jal = input("是否将数据写入表格(是：Y 否：N)：")
                    if jal.lower() == "y":
                        writetable(list, table_name, database)
                        break
                    elif jal.lower() == "n":
                        print("结束")
                    else:
                        print("输入错误")
                        continue

        else:
            print("文件不存在")
            return False


if __name__ == '__main__':
    main("ldu_student_information")