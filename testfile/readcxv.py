# @File    : readcxv.py
import pylightxl as xl
db = xl.readcsv(fn='sc.csv', delimiter='/', ws='sh2')

print(type(db))
for i in db:
    print(i)