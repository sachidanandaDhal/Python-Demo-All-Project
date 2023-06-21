# Employee Database


name = []
phone = []
address = []
list1 = []

while True:
    print ("1. Add Data\n2. Search Data\n3. Delete Data\n4. Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        n = input("Enter name:")
        name.append(n)
        p = input ("Enter phone number:")
        phone.append(p)
        a = input ("Enter address:")
        address.append(a)

        print ("--- Data Added Successfully ----")

    elif ch == 2:
        n = input("Enter Your name to search details:")
        if n in name:
            print("--- Data Found --- ")
            index_num = name.index(n)
            print("Name: ",name[index_num])
            print("Phone number: ", phone[index_num])
            print("Address: ",address[index_num])
            print("-"*30)
        else:
            print("---- DATA NOT FOUND ---")
            
    elif ch == 3:
            n = input("Enter your name to delete your details:")
            if n in name:
                print("--- Data Found ---")
                index_num = name.index(n)
                name.pop(index_num)
                phone.pop(index_num)
                address.pop(index_num)
                print("-- Data Deleted Successfully --")
                print("-"*30)
            else:
                print("--- Data Not Found ---")
                
    elif ch == 4:
        print("--- Bye ---")
        break
    
    else:
        print("--- Invalid Choice----")

print(list1)
            
