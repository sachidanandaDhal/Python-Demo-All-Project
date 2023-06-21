import sqlite3
import csv
import smtplib
from email.mime.text import MIMEText


#create a DB
db = sqlite3.connect("DB_Proj.sqlite")

# create a Table
try:
    db.execute('''create table student(
                    Roll Integer,
                    Name text,
                    Email text,
                    Math Integer,
                    Science Integer,
                    Computer Integer)''')
except:
    pass

def addStudent():
    print("----- Create a new Student Profile ----")

   #Data = ["Roll No","Name","Email ID","Enter marks in Maths","Enter marks in science","Enter marks in computer"]
    Data = []

#Roll    
    roll = input("Enter Roll No: ")
    while roll.isdigit() != True:
        print("Invalid name! Please try again")
        roll = input("Enter Roll No: ")
    Data.append(roll)
    
#name
    name= input("Enter name: ")
    Data.append(name)
    
#Email
    email = input("Enter Your Email ID: ")
    Data.append(email)
    
#Math    
    math = int(input("Enter marks in maths:"))
    Data.append(math)
    
#Science    
    sc = int(input("Enter makrs in Science: "))
    Data.append(sc)
    
#Computer    
    cp = int(input("Enter marks in Computer: "))
    Data.append(cp)
    

    db.execute("insert into student values(?,?,?,?,?,?)",Data)
    db.commit()
    print("-*---- Student Addedd Successfully ----*-")

def checkResult():
    print("------ Check Your Result Here ------")
    cursor = db.cursor()
    r = int(input("Enter your roll number to check your result:"))
    cursor.execute("Select * from student where roll =?",[r])
    var = cursor.fetchall()
    print(var)
    print(">>>>>>>>>>>>>>>>>>ALL DETAILS<<<<<<<<<<<<<<<<<<<<<<")     
    print("Roll Number:",var[0][0])
    print("Name:",var[0][1])
    print("Email Id:",var[0][2])
    print("Math:",var[0][3])
    print("Science:",var[0][4])
    print("Computer:",var[0][5])

    perc = (var[0][3]+var[0][4]+var[0][5])/3
    print("Percentage: %.2f"%perc)
    print("-"*30)
    return perc

def genReport():
    cursor = db.cursor()
    cursor.execute("select * from student")
    var = cursor.fetchall()
    print(var)

    #writing this data into a CSV file

    f = open("report.csv","w",newline="")
    obj = csv.writer(f)
    obj.writerow(["Roll No.","Student Name","Email Id","Maths","Science","Computer","Percentage","Status"])
    

    for i in var:
        perc = "%.2f" %((i[-1]+i[-2]+i[-3])/3)
        if i[-1]>35 and i[-2]>35 and i[-3]>35:
            status = "PASS"
        else:
            status = "FAIL"

        list2 = list(i)
        list2.append(perc)
        list2.append(status)

        obj.writerow(list2)

    f.close()
    print("---- Report Generated Successfully ----")

def sendReport():
    # server address, port number
    server = smtplib.SMTP("smtp.gmail.com","587")
    # to make a secure connection
    server.starttls()    
    print("--- Connected with the server ---")

    #sender mail
    username = "dhal.sachidananda1@gmail.com"
    sender=username
    pwd = "trieigrgsfjfhfdw"
    server.login(username,pwd)
    print("---- Login Successful -----")
    cursor = db.cursor()
    tup=cursor.execute("select * from student")

    #receiver mail info

    for k in tup:
        receiver =k[2]
        perc = (k[-3]+k[-2]+k[-1])/3
        msg = f"""From:HALF YEARLY EXAM
Subject: Result of Half-Yearly Exam 2022
Student Name={k[1]}
Computer= {k[-1]}
Math = {k[-3]}
Science = {k[-2]}
Percentage scored = {perc}"""
    server.sendmail(sender,receiver,msg)
    print("-- Mail Sent Succcessfully --")
    
    
    
while True:
    print("....>*>*>*>*>*>* MAIN MENU *<*<*<*<*<*<....")
    print("1. Add a Student")
    print("2. Check Percentage")
    print("3. Convert into CSV file")
    print("4. Mail Report ")
    print("5. Exit")
    ch = int(input("Enter your Choice:"))
    if ch == 1:
        addStudent()
    elif ch == 2:
        checkResult()
    elif ch == 3:
        genReport()
    elif ch == 4:
        sendReport()
    elif ch == 5:
        print("--- Successfully Done ---")
        break
    else:
        print("--- Input the correct values ---")
