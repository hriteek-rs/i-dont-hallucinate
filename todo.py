tasks =[]

def menu():
    print("TO-DO LIST")
    print("1.Add new task")
    print("2.View Task")
    print("3.Task Completed")
    print("4.Delete Task")
    print("5.Exit")

def add_task():
        new_task=input("Add new task:")
        tasks.append({"task":new_task, "done":False})
        print(f"Task: '{new_task}' added!")



def view_task():
    if not tasks:
         print("There is no task added yet!")
         return
    print("\n Your Tasks:")
    for index, task in enumerate(tasks, start=1):
         status= "✅" if task["done"] else "❌"
         print(f"{index} {task['task']} [{status}]")

def complete_task():
     view_task()
     if not tasks:
          return
     try:
          index=int(input("Enter task number to mark completed: "))-1 #that -1 is for balancing the numberig as the indexig stasrts form 0 in python 
          if 0<= index<len(tasks):
               tasks[index]["done"]=True
               print("Marked as dine!")
          else:
               print("Invalid number")
     except ValueError:
          print("Your given input was not a valid number. Kindly enter a valid number to see the results u are expecting to ;)")

def delete_task():
     view_task()
     if not tasks:
          return
     try:
          index = int(input("Enter task number to remove:"))-1
          if 0<=index < len(tasks)  :
               deleted=tasks.pop(index)      
               print(f"Task Removed:{deleted['task']}")
          else:
               print("Invalid number!") 
     except ValueError:
        print("enter a valid number:")    

while True:
    menu()
    choice = input("Choose an option (1-5): ")

    
    match choice:
        case '1': add_task()
        case '2': view_task()
        case '3': complete_task()
        case '4': delete_task()
        case '5':
            print("Goodbye!")
            break
        case _:  
            print("Invalid choice.")
