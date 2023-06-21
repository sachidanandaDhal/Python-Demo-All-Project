# Supermarket DB Mgnt

#1 Extract data -> regex

#2 Generate report in csv
# profit = (sp-cp)*quan
'''
Prod      Quan     CP     SP      Profit
m          20      13     15        40
k          8       90     100       80
                          Total     120
'''

#3 Plot graph



import re,csv
import os

path ="C:\\Users\\Sachidananda.dhal\\OneDrive - OneWorkplace\\Documents\\class9-python\\regex_proj" 
var=os.listdir(path)
#print(var)

list_files = []
daily_profit = []

for i in var:
    if i.endswith(".txt"):
        list_files.append(i)

##print(list_files)

for item in list_files:
    
    txt = open(item).read()

    
    pat1 = "Product:\s(\w+)"
    prod = re.findall(pat1,txt)
#    print(prod)

    pat2 = "Quantity:\s(\w+)"
    quan = re.findall(pat2,txt)
#    print(quan)

    pat3 = "CP:\s(\w+)"
    cp = re.findall(pat3,txt)
#    print(cp)

    pat4 = "SP:\s(\w+)"
    sp = re.findall(pat4,txt)
#    print(sp)

    # Generate report in CSV
    filename = item.rstrip(".txt") + ".csv"
    f = open(filename,"w",newline="")
    obj = csv.writer(f)
    obj.writerow(["Product","Quantity","CP","SP","Profit"])
    total=0
    for i in range(len(prod)):
        profit = (int(sp[i])-int(cp[i])) * int(quan[i])
        total = total+profit
        obj.writerow([prod[i],quan[i],cp[i],sp[i],profit])
        
    obj.writerow(["","","","Total",total])
    daily_profit.append(total)
    f.close()

print(list_files)
print(daily_profit)


# plot the graph
import matplotlib.pyplot as plt

plt.bar(list_files,daily_profit)
plt.title("December Report")
plt.xlabel("Dates")
plt.ylabel("Profit")
plt.show()
    





