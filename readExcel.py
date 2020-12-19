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
            self.reList = [sh.row_values(rx) for rx in range(sh.nrows)]
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
