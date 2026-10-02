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

add_task()



        
