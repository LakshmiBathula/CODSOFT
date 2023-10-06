tasks=[]

def addt(task):
    tasks.append(task)
    print(f"added task:{task}")

def removet(ind,d_task):
   if 0<=ind<=len(tasks):
        d_task=tasks.pop(ind)
        print(f"{d_task} remove successfully") 
   else: 
       print("task not found")  

def showt():
    print("TO-DO LIST")
    for i,task in enumerate(tasks):
        print(f"{i}.{task}")  

def updatet(ind1):
    if 0<=ind1<=len(tasks):
        tasks[ind1]=(input("enter  task for update:\t"))
        print(f"task{ind1} updated succefully")        

while True:
    print("\n......TO-DO LIST......\n")   
    print("1.ADD TASK") 
    print("2.REMOVE TASK")
    print("3.SHOW TASKS")  
    print("4.UPDATE  TASK") 
    print("5.EXIT")
    choice=input("enter your choice:\t")  
    if choice=="1":
        task=input("enter new task:\t")
        addt(task)      
    elif choice=="2":
        ind=int(input("enter index of task to remove:\t")) 
        removet(ind,task)
    elif choice=="3":
        showt() 
    elif choice=="4":
        ind1=int(input("enter index of task for update:\t"))
        updatet(ind1)  
    elif choice=="5":
        exit()