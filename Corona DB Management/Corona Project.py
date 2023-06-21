#corona Project
import csv
import matplotlib.pyplot as plt  
def addData():
  print("---Add New Data Here---")
  # country name , positive case, recovered cases and death cases

  f=open("corona.csv","a",newline="")
  obj=csv.writer(f)
  cn = input("Enter country name:")
  pc = input("Enter total positive case:")
  rc = input("Enter total recovered case:")
  dc = input("Enter total death case:")

  obj.writerow([cn,pc,rc,dc])
  f.close()
  print("--- Data Added Successfully ---")
def showData():
 print("---Display Data Here---")

 f=open("corona.csv")
 data = list(csv.reader(f))
 for i in data:
  print(i)
 print("-"*30)
 f.close()

def plotData():
  f=open("corona.csv")
  data = list(csv.reader(f))

  country_name =[]
  positive_cases=[]
  recoveryed_cases=[]
  for i in data:
    country_name.append(i[0])
    positive_cases.append(int(i[1]))
    recoveryed_cases.append(int(i[2]))
 # print(country_name)
 # print(positive_cases)
 # print(recoveryed_cases)

  plt.bar(country_name,positive_cases)
  plt.bar(country_name,recoveryed_cases)
  plt.xlabel("Country Name")
  plt.ylabel("Positive Cases/Recoveryed cases")
  plt.title("Corona Graph")
  plt.show()


while True:
  print("1.Add Data\n2. Show Data\n3. Plot Data\n4. Exit")
  ch = int(input("Enter Choice:"))

  if ch==1:
   addData()
  elif ch== 2:
   showData()
  elif ch==3:
   plotData()
  elif ch == 4:
    break
  else:
   print('--Invalid Choice---') 
