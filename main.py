import mysql.connector as mys
mydb = mys.connect(user='root',host='localhost',password='xz123456op',database='company')
while True:
    print("=========================")
    print("          MENU")
    print("=========================")
    print("1 > Show Tables")
    print("2 > Display Employee")
    print("3 > Insert New Record")
    print("4 > Update Record")
    print("5 > Search Employee")
    print("0 > Exit")
    print("=========================")
    cur = mydb.cursor()
    ch = int(input("Enter choice: "))
    if ch == 1:
        query = 'show tables'
        cur.execute(query)
        for data in cur:
            print(data)
        cur.close()
    elif ch==2:
        query='select * from employee'
        cur.execute(query)
        for data in cur:
            print(data)
        cur.close()
    elif ch==3:
        fn = input("Enter employee first name: ")
        ln = input("Enter employee last name: ")
        dep = input("Enter employee department: ")
        query = "insert into employee(name,surname,department) values('{}','{}','{}')".format(fn,ln,dep)
        cur.execute(query)
        mydb.commit()
        cur.close()
    elif ch==4:
        dep = input("enter department: ")
        ln = input("enter employee last name: ")
        query = "update employee set department = '{}' where surname='{}'".format(dep,ln)
        cur.execute(query)
        mydb.commit()
        cur.close()
    elif ch==5:
        fn = input("Enter employee first name: ")
        query = "select * from employee where='{}'".format(fn)
        cur.execute(query)
        for data in cur:
            print(data)
    elif ch==0:
        cur.close()
        mydb.close()
        exit()
    else:
        print("invalid input")


