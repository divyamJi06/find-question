from pymysql import *
empl = [
    [ {'ID':5},{'Name':'Sam'},{'Designation':'Manager'},{'Age':22}],
    [ {'ID':4},{'Name':'Ram'},{'Designation':'Designer'},{'Age':30}],
    [ {'ID':2},{'Name':'Sara'},{'Designation':'Vice President'},{'Age':42}],
    [ {'ID':1},{'Name':'Vinay'},{'Designation':'Manager'},{'Age':22}]
    ]

db = connect('localhost','root','ayush2002','prac')
cur = db.cursor()
cur.execute("drop table if exists emp")
cur.execute(f"create table emp(ID int(4) primary key, Name varchar(40), Designation varchar(40),Age int(3))")
'''=
for i in empl:
    for j in i:
        for k in j.values():
            val.append(k)
    val =tuple(val)
    cur.execute(f"insert into emp values {val}")
    db.commit()
    val =[]
'''

l = [9,'name','class',3]
cur.execute(f"insert into emp values ({l})")
db.commit()