# @File    : create.py
import numpy as np
from xpinyin import Pinyin

from src.conneMySQL import connect_mysql
from src.newcolname import Columnlabel

p = Pinyin()


class createTable:
    '''
    # list[] 将表列表
    # list[0] 一般意义上的表头，例如['名字','性别','年龄']
    # zip("表头信息","每一列数据(str)的最大宽度")
    '''

    @staticmethod
    def create(list):
        def colname(list):
            '''
            根据表格的列名生成数据库表中的列名
            规则是：面向中文表头将汉字转换为拼音并依据excel列在开头加上英文字母
            如：c_xingming 表示 姓名这一列
            在前面加上英文字母可以方便的避免列名的重复
            '''
            return [str(Columnlabel(len(list[0]))[k] + "_" + p.get_pinyin(list[0][k], "")) for k in range(len(list[0]))]

        def colmaxlen(list):
            '''
            返回列的最大数据长度
            '''
            return np.max(np.array([[len(str(k)) for k in i] for i in list[1:]]), axis=0)

        def Amplification(dic):
            '''
            扩增一下，不满5进5,满5进位
            '''
            for i, j in dic.items():
                dic[i] = (j // 5 + 1) * 5
            return dic

        return Amplification(dict(zip(colname(list), colmaxlen(list))))

    @staticmethod
    def getSQl(tablename, list):
        '''
        最大长度小于64字符的用varchar()
        大于64的用text       
        '''
        liss = []
        for i in createTable.create(list).items():
            colname = str(i[0])
            type = "varchar({})".format(i[1]) if i[1] < 64 else "text"
            liss.append("{}\t{}".format(colname, type))
        sql = "create table\t{}\n({}\n)".format(tablename, ",\n\t".join(liss))
        print(sql)
        return sql


def maincreate(table_name, list):
    sql = createTable.getSQl(table_name, list)
    con = connect_mysql()
    con.con("ldu_student_information")
    con.update(sql)
