import mysql.connector
db=mysql.connector.connect(
    host='localhost',user='root',password='vicky444',database='results')
def insert(rollno,name,mark,result):
    cursor=db.cursor()
    sql="insert into users (rollno,name,mark,result) values(%s,%s,%s,%s)"
    user=(rollno,name,mark,result)
    cursor.execute(sql,user)
    db.commit()
    print("***DATA INSERTED SUCESSFULLY***")
def delete(rollno):
    cursor=db.cursor()
    sql="delete from users where rollno=%s"
    user=(rollno,)
    cursor.execute(sql,user)
    db.commit()
    print("***DATA DELETED SUCESSFULLY***")
def all():
    cursor=db.cursor()
    sql="SELECT ROLLNO,NAME,MARK,RESULT from users"
    cursor.execute(sql)
    key=cursor.fetchall()
    print(key)
while True:
    print("1.INSERT DATA")
    print("2.DELETE DATA")
    print("3.ALL DATA")
    print("4.EXIT")
    choice=int(input("ENTER YOUR CHOICE  :"))
    if choice==1:
        rollno=int(input('enter rollno: '))
        name=input('enter name: ')
        mark=input('enter mark: ')
        result=input('enter result: ')
        insert(rollno,name,mark,result)
    elif choice==2:
        rollno=input("ENTER THE ROLLNO TO DELETE  :")
        delete(rollno)
    elif choice==3:
        all()
    elif choice==4:
        quit()
    else:
        print("invalid selection ,please try again !!!")
        




    
