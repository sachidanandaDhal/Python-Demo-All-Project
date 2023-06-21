# Bank Appliaction Project
# Dictionary data type

# {101:{name:sam,age:25,amount:10000}}


import json

def writeData(newDict):
    try:
        f = open("bank.txt","r")
        var = json.load(f)
        var.update(newDict)
        f.close()

        f = open("bank.txt","w")
        json.dump(var,f,indent=4)
        f.close()
        print("---- Account created ----")

    except FileNotFoundError:
        f = open("bank.txt","w")
        json.dump(newDict,f,indent=4)
        f.close()
        print("---- Account created ----")
        
def newAccount():
    bank = {}  # Empty dictionary
    
    print("----- Create A New Account Here -----")

    acc = input("Enter new account number:") # key
    # value
    list1 = ["Name","Age","Address","Phone","Amount"]
    list2 = []
    n = input("Enter name:")
    while n.isalpha() == False:
        print("Invalid name ! Please try again")
        n = input("Enter name:")
    list2.append(n)
    
    age = input("Enter age:")
    while age.isdigit() != True:
        print("Invalid age ! Please try again")
        age = input("Enter age:")
    list2.append(age)
    
    add = input("Enter address:")
    list2.append(add)
    ph = input("Enter phone number:")
    list2.append(ph)
    amt = int(input("Enter amount:"))
    list2.append(amt)

    # Store data into dictionary
    bank[acc] = dict(zip(list1,list2))
    
    # will store this dictionary to the json file
    writeData(bank)  # function call

def existingCust():
    print("---- For Existing Customer ----")
    acc = input("Enter your account number to fetch your details:")
    f = open("bank.txt","r")
    var = json.load(f)
    f.close()

    if acc in var:
        print("---- Data Found ----")
        while True:
            print("1. Check Balance\n2. Withdraw\n3. Deposite\n4. Main Menu")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                print("-"*30)
                print("Available Balance:",var[acc]["Amount"])
                print("-"*30)
            elif ch == 2:
                amt_w=int(input("Enter amount to withdraw:"))
                if amt_w<var[acc]['Amount']:
                    var[acc]['Amount'] = var[acc]['Amount']-amt_w
                    print("-"*30)
                    print("Remaining Balance :",var[acc]['Amount'])
                    print("-"*30)
                    writeData(var)
                else:
                    print("--- Insufficient Balance ---")
            elif ch == 3:
                amt_w=int(input("Enter amount to deposite:"))
                var[acc]['Amount'] = var[acc]['Amount']+amt_w
                print("-"*30)
                print("Deposite Successfull ! Available Balance :",var[acc]['Amount'])
                print("-"*30)
            elif ch == 4:
                break               
    else:
        print("---- Data Not Found ----")

def updateDetails():
    print('---- for updating customer details----')
    acc = input('enter account number to fetch your details:')
    f = open("bank.txt","r")
    var = json.dump(f)
    f.close()

    if acc in var:
        print('---data found----')
        print('1. update phone\n2. update address:')
        ch = int(input('enter your choice:'))
        if ch== 1:
            a=input('enter your old phone number')
            if a == var[acc]['phone']:
                var
                [acc]['phone']=input('enter your new phone number')
                print('phone number updated')
            else:
                print('old number does not matches')

        elif ch == 2:
            a=input('enter your old address')
            if a in var[acc]['address']:
                var[acc]['address']=input('enter your new address')
                print('new address has been updated')
                
            else:
                print('old address does not matches')
    else:
        print('---data not found----')

while True:
    print("****** MAIN MENU ******")
    print("1. Create A New Account")
    print("2. For Existing Customer")
    print("3. Update Details")
    print("4. Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        newAccount()  # function call
    elif ch == 2:
        existingCust()  # function call
    elif ch == 3:
        updateDetails()   # function call        
    elif ch == 4:
        print("--- Thank You ! Please visit again ---")
        break
    else:
        print("--- Invalid Choice ---")

