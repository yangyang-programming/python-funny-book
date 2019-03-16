
f=open('Drawsquare.py','r',encoding='UTF-8')
a=f.readlines()
m=1
for i in a:
    print(str(m)+'   '+i.strip('\r\n'))
    m+=1
