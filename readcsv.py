#coding=utf-8
#这是一个用python读excel 的csv文件的
import csv
x = open('123.csv')
print x
for p in x:
    print p
with open ('123.csv','rb') as f:
    reader = csv.reader(f)
    for i in reader:
        print i