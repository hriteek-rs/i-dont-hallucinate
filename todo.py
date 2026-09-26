# Problem: 46. To-do list app: read tasks from tasks.txt on startup, let the user add/complete/delete tasks, write changes back so the list persists across runs. (Loops + file handling + functions)

#this function below reads tasks from the file named "tasks.txt" when the program is started

def read_task():
 with open("tasks.txt",'r') as file:
    read=file.read()
    print(read)
read_task()

# add more tasks
def new_task():
  with open("tasks.txt",'a+') as file:
    add=input("add more task:")
    file.write(add+"\n")
    user=input("Would u like to add more tasks (y/n)?")
    while user.lower()=="y":
      task = input("add task:")
      user = input("would u like to add more tasks(y/n)")
new_task()    

#complete task
def complete_task():

  task={
    "id":1,
    "title":"python tasks",
    "completed":True
}

