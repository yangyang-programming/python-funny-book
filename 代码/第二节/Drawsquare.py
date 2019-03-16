#Drawsquare.py  
'''
画个正方形，并填充红色
'''
import turtle as td
td.color('red','red')
td.begin_fill()
for i in range(4):
    td.fd(200)
    td.right(90)
td.end_fill()

