import os
import platform
import mysql.connector
#import pandas as pd 
#from pandas import DataFrame 
 

db = mysql.connector.connect(user='root', password='#mrverma1489', host='localhost',database='school')
cursor = db.cursor()
def selection():               
               print(" WELCOME TO SCHOOL MANAGEMENT SYSTEM ")
               print("1.STUDENT MANAGEMENT")
               print("2.EMPLOYEE MANAGEMENT")
               print("3.FEE MANAGEMENT")
               print("4.EXAM MANAGEMENT")
               ch=int(input("\nEnter ur choice (1-4) : "))
               if ch==1:
                              print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
                              print('a.NEW ADMISSION')
                              print('b.UPDATE STUDENT DETAILS')
                              print('c.ISSUE TC')
                              c=input("Enter ur choice (a-c) : ")
                              print('\nInitially the details are..\n')
                              if c=='a':
                                             insert1()
                                             print('\nModified details are..\n')
                                             display1()
                              elif c=='b':
                                             update1()
                                             print('\nModified details are..\n')
                                             display1()
                              elif c=='c':
                                             delete1()
                                             print('\nModified details are..\n')
                                             display1()
                              else:
                                             print('Enter correct choice...!!')
               elif ch==2:
                              print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
                              print('a.NEW EMPLOYEE')
                              print('b.DELETE EMPLOYEE')
                              c=input("Enter ur choice : ")
                              if c=='a':
                                             insert2()
                                             print('\nModified details are..\n')
                                             display2()
                              elif c=='b':
                                             delete2()
                                             print('\nModified details are..\n')
                                             display2()
                              else:
                                             print('Enter correct choice...!!')
               elif ch==3:
                              print('WELCOME TO FEE MANAGEMENT SYSTEM')
                              print('a.NEW FEE')
                              print('b.UPDATE FEE')
                              print('c.EXEMPT FEE')
                              c=input("Enter ur choice : ")
                              if c=='a':
                                             insert3()
                              elif c=='b':
                                             update3()
                              elif c=='c':
                                             delete3()
                                             print('\nModified details are..\n')
                                             display3()
                              else:
                                             print('Enter correct choice...!!')
               elif ch==4:
                              print('WELCOME TO EXAM MANAGEMENT SYSTEM')
                              print('a.EXAM DETAILS')
                              print('b.UPDATE DETAILS ')
                              print('c.DELETE DETAILS')
                              c=input("Enter ur choice : ")
                              if c=='a':
                                             insert4()
                              elif c=='b':
                                             update4()
                              elif c=='c':
                                             delete4()
                              else:
                                             print('Enter correct choice...!!')
               else:
                              print('Enter correct choice..!!')

def insert1():
               l=[]
               sname=input("Enter Student Name : ")
               l.append(sname)
               admno=int(input("Enter Admission No : "))
               l.append(admno)
               dob=input("Enter Date of Birth(yyyy-mm-dd): ")
               l.append(dob)
               cls=input("Enter class for admission: ")
               l.append(cls)
               cty=input("Enter City : ")
               l.append(cty)
               stud=(l)
               sql="INSERT INTO student(sname,admno,dob,cls,cty) VALUES ( %s ,%s,%s,%s,%s)" 
               cursor.execute(sql,stud)
               db.commit()

def display1():
               sql = "SELECT * FROM student"
               cursor.execute(sql)
               results = cursor.fetchall()
               print("Entered Details are:")
               print("S_Name,AdmNo.,DOB,Class,City")
               for x in results:
                              print(x)

                             

def update1():
               try:
                              sql = "SELECT * FROM student"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                             print(c)
               except:
                              print ("Error: unable to fetch data")
                              print()
               tempst=int(input("Enter Admission No : "))
               temp=input("Enter new class  : ")
               try:
                              sql = "Update student set cls=%s where admno='%d'" % (temp,tempst)
                              cursor.execute(sql)
                              db.commit()
               except Exception as e:
                              print (e)
                              db.close()

def delete1():
               try:
                              sql = "SELECT * FROM student"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                             print(c)  
               except:
                              print ("Error: unable to fetch data")
               temp=int(input("\nEnter adm no to be deleted : "))
               try:
                              sql = "delete from student where admno='%d'" % (temp)
                              ans=input("Are you sure you want to delete the record(y/n) : ")
                              if ans=='y' or ans=='Y':
                                             cursor.execute(sql)
                                             db.commit()
               except Exception as e:
                              print (e)
                              db.close()

def insert2():
               l=[]
               ename=input("Enter Employee Name : ")
               l.append(ename)
               empno=int(input("Enter Employee No : "))
               l.append(empno)
               job=input("Enter Designation: ")
               l.append(job)
               hiredate=input("Enter date of joining: ")
               l.append(hiredate)
               stud=(l)
               sql="INSERT INTO emp(ename,empno,job,hiredate) VALUES (%s ,%s,%s,%s)"
               cursor.execute(sql,stud)
               db.commit()

def display2():
               try:
                              sql = "SELECT * FROM emp"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                                            print(c)
               except:
                              print ("Error: unable to fetch data")
                              db.close()

def update2():
               try:
                              sql = "SELECT * FROM emp"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                              print(c)
                                              
               except:
                              print ("Error: unable to fetch data")
                              print()
               tempst=input("Enter Employee No : ")
               temp=input("Enter new designation  : ")
               try:
                              sql = "Update emp set job=%s where empno='%s'" % (temp,tempst)
                              cursor.execute(sql)
                              db.commit()
               except Exception as e:
                              print (e)
                              db.close()

def delete2():
               try:
                              sql = "SELECT * FROM emp"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                             print(c)
               except:
                              print ("Error: unable to fetch data")
               temp=int(input("\nEnter emp no to be deleted : "))
               try:
                              sql = "delete from emp where empno='%d'" % (temp)
                              ans=input("Are you sure you want to delete the record(y/n) : ")
                              if ans=='y' or ans=='Y':
                                             cursor.execute(sql)
                                             db.commit()
               except Exception as e:
                              print (e)
                              db.close()
def insert3():
               admno=int(input("Enter adm no: "))
               fee=float(input("Enter fee amount : "))
               month=input("Enter Month: ")
               sql="INSERT INTO fee(admno,fee,month) VALUES ( '%d','%d','%s')"%(admno,fee,month)
               try:
                              cursor.execute(sql)
                              db.commit()
               except:
                              db.rollback()
                              db.close()

def display3():
               try:
                               
                              sql = "SELECT * FROM fee"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                             print(c)
                              print ("(admno=%d,fee=%s,month=%s)" % (admno,fee,month))
               except:
                              print ("Error: unable to fetch data")
                              db.close()

def update3():
               try:
                              sql = "SELECT * FROM fee"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                             print(c)
               except:
                              print ("Error: unable to fetch data")
                              print()
               tempst=int(input("Enter Admission No : "))
               temp=input("Enter Month : ")
               sql = "Update fee set month=%s where admno='%d'"  
               cursor.execute(sql)
               db.commit()
                

def delete3():
               try:
                              sql = "SELECT * FROM fee"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                             print(c)
               except:
                              print ("Error: unable to fetch data")

               temp=int(input("\nEnter adm no to be deleted : "))
               try:
                              sql = "delete from student where admno='%d'" % (temp)
                              ans=input("Are you sure you want to delete the record(y/n) : ")
                              if ans=='y' or ans=='Y':
                                             cursor.execute(sql)
                                             db.commit()
               except Exception as e:
                              print (e)
                              db.close()

def insert4():
               sname=input("Enter Student Name : ")
               admno=int(input("Enter Admission No : "))
               per=float(input("Enter percentage : "))
               res=input("Enter result: ")
               sql="INSERT INTO exam(sname,admno,per,res) VALUES ( '%s' ,'%d','%s','%s')"%(sname,admno,per,res)
               try:
                              cursor.execute(sql)
                              db.commit()
               except:
                              db.rollback()
                              db.close()

def display4():
               try:
                              sql = "SELECT * FROM exam"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                             print(c)
                              print ("(sname,admno,per,res)"%(sname,admno,per,res) )
               except:
                              print ("Error: unable to fetch data")
                              db.close()

def update4():
               try:
                              sql = "SELECT * FROM exam"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                             print(c)                  
               except:
                              print ("Error: unable to fetch data")
                              print()
               tempst=int(input("Enter Admission No : "))
               temp=input("Enter new result  : ")
               try:
                              sql = "Update exam set res=%s where admno='%d'" % (temp,tempst)
                              cursor.execute(sql)
                              db.commit()
               except Exception as e:
                              print (e)
                              db.close()

def delete4():
               try:
                              sql = "SELECT * FROM exam"
                              cursor.execute(sql)
                              results = cursor.fetchall()
                              for c in results:
                                              print(c)

               except:
                              print ("Error: unable to fetch data")
               temp=int(input("\nEnter adm no to be deleted : "))
               try:
                              sql = "delete from exam where admno='%d'" % (temp)
                              ans=input("Are you sure you want to delete the record(y/n) : ")
                              if ans=='y' or ans=='Y':
                                             cursor.execute(sql)
                                             db.commit()
               except Exception as e:
                              print (e)
                              db.close()
def runAgain():
               print(' WELCOME TO SCHOOL MANAGEMENT SYSTEM')
               print("1.STUDENT MANAGEMENT")
               print("2.EMPLOYEE MANAGEMENT")
               print("3.FEE MANAGEMENT")
               print("4.EXAM MANAGEMENT")
               ch=int(input("\nEnter ur choice (1-4) : "))
               if ch==1:
                              print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
                              print('a.NEW ADMISSION')
                              print('b.UPDATE STUDENT DETAILS')
                              print('c.ISSUE TC')
                              c=input("Enter ur choice (a-c) : ")
                              print('\nInitially the details are..\n')
                              if c=='a':
                                             insert1()
                                             print('\nModified details are..\n')
                                             display1()
                              elif c=='b':
                                             update1()
                                             print('\nModified details are..\n')
                                             display1()
                              elif c=='c':
                                             delete1()
                                             print('\nModified details are..\n')
                                             display1()
                              else:
                                             print('Enter correct choice...!!')
               elif ch==2:
                              print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
                              print('a.NEW EMPLOYEE')
                              print('b.UPDATE STAFF DETAILS')
                              print('c.DELETE EMPLOYEE')
                              c=input("Enter ur choice : ")
                              if c=='a':
                                             insert2()
                                             print('\nModified details are..\n')
                                             display2()
                              elif c=='b':
                                             update2()
                                             print('\nModified details are..\n')
                                             display2()
                              elif c=='c':
                                             delete2()
                                             print('\nModified details are..\n')
                                             display2()
                              else:
                                             print('Enter correct choice...!!')
               elif ch==3:
                              print('WELCOME TO FEE MANAGEMENT SYSTEM')
                              print('a.NEW FEE')
                              print('b.UPDATE FEE')
                              print('c.EXEMPT FEE')
                              c=input("Enter ur choice : ")
                              if c=='a':
                                             insert3()
                              elif c=='b':
                                             update3()
                              elif c=='c':
                                             delete3()
                              else:
                                             print('Enter correct choice...!!')
               elif ch==4:
                              print('WELCOME TO EXAM MANAGEMENT SYSTEM')
                              print('a.EXAM DETAILS')
                              print('b.UPDATE DETAILS ')
                              print('c.DELETE DETAILS')
                              c=input("Enter ur choice : ")
                              if c=='a':
                                             insert4()
                              elif c=='b':
                                             update4()
                              elif c=='c':
                                             delete4()
                              else:
                                             print('Enter correct choice...!!')
               else:
                              print('Enter correct choice..!!')
                

 
runAgain()
selection() 
