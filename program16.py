import mysql.connector as sql
dbcon = sql.connect(host = "localhost",user="root",password="bbit@123",database="sourangshu")
cur = dbcon.cursor()
cur.execute("select * from employee")
data = cur.fetchall()
for i in data:
    for j in i:
        print(j,end=" ")
    print()
dbcon.commit()
dbcon.close()