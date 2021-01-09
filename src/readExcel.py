# @File    : readExcel.py
import csv

import pylightxl
import xlrd

'''
读取xls、xlsx、csv文件
暂时只考虑读取xls表格的sheet1

self.filepath = filepath     #文件路径
self.list = []               #返回结果
        
'''
import xlrd
from xlrd import xldate_as_tuple
import datetime
'''
xlrd中单元格的数据类型
数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换
成我们想要的数据类型
0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
'''
def vover(cellcol):
    liss=[]
    for j in cellcol:
        c_cell=j.value
        c_type=j.ctype
        if c_type ==1:
            #单元格类型为：text
            c_cell=c_cell.replace("\n","")
        if c_type == 2 and c_cell % 1 == 0:  # 如果是整形
            #单元格类型为number
            c_cell = int(c_cell)
        elif c_type == 3:
            # 单元格类型为：datetime
            date = datetime.datetime(*xldate_as_tuple(c_cell,0))
            c_cell = date.strftime('%Y/%d/%m')#年-月-日
        elif c_type == 4:
            #单元格类型为:booble
            c_cell = True if c_cell == 1 else False
        liss.append(c_cell)
    return liss




'''
open_xlsx(self)、open_xls(self)都还有一些格式上的优化
'''


class read_excel:
    def __init__(self, filepath):
        self.fp = filepath  # 文件路径
        self.reList = []  # 返回结果
        if filepath.endswith('.csv'):
            self.open_csv()  # csv格式
        elif filepath.endswith('.xlsx'):
            self.open_xlsx()  # xlsx格式
        elif filepath.endswith('.xls'):
            self.open_xls()  # xls格式
        else:
            print("不支持格式")

    def open_xls(self):
        try:
            book = xlrd.open_workbook(self.fp)
            sh = book.sheet_by_index(0)  # 选择工作薄第一个表
            self.reList = [vover(sh.row(rx)) for rx in range(sh.nrows)]
        except:
            print("读取文件出错:" + self.fp)

    def open_csv(self):
        try:
            self.reList = list(csv.reader(open(self.fp)))
        except:
            print("读取文件出错:" + self.fp)

    def open_xlsx(self):
        try:
            db = pylightxl.readxl(self.fp)
            self.reList = [row for row in db.ws(ws=db.ws_names[0]).rows]
        except:
            print("读取文件出错:" + self.fp)

    def result(self):
        return self.reList


def readexcel(filepath):
    return read_excel(filepath).result()





# print(readexcel("testfile\sdfs.xls"))