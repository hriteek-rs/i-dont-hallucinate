# Problem: 46. To-do list app: read tasks from tasks.txt on startup, let the user add/complete/delete tasks, write changes back so the list persists across runs. (Loops + file handling + functions)

#this function below reads tasks from the file named "tasks.txt" when the program is started

def read_task():
 with open("tasks.txt",'r') as file:
    read=file.read()
    print(read)
read_task()

#the app lets u add more tasks
def new_task():
  with open("tasks.txt",'a+') as file:
    add=input("add more task:")
    file.write(add+"\n")
new_task()    

