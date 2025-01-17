# To - Do App

task = []

def showTask():
    print("*************************")
    for var in task:
        print(var)

def addTask():
    newTask = input("Enter your task: ")
    task.append(newTask)

def updateTask():
    updatedVal = input("Enter a task name you want to update: ")
    if updatedVal in task:
        newVal = input("Enter new task: ")
        ind = task.index(updatedVal)
        task[ind] = newVal
        print(f"Updated task: {newVal}")

def deleteTask():
    deleteTask = input("Enter a task you want to delete: ")
    if deleteTask in task:
        ind = task.index(deleteTask)
        del task[ind]
        print(f"Task '{deleteTask}' has been deleted!")

while True:
    print("**************************")
    print("Welcome to the 'TO-DO App'")
    print("**************************")
    print("1.Show Tasks\n2.Add new Task\n3.Update existing Task\n4.Delete Task\n5.Quite")
    

    userChoice = input("Enter your choice between (1 - 5): ")
    print("**************************")
    
    if userChoice == "1":
        showTask()
    elif userChoice == "2":
        addTask()
    elif userChoice == "3":
        updateTask()
    elif userChoice == "4":
        deleteTask()
    elif userChoice == "5":
        print("Closing the program...")
        break
    else:
        print("Please select valid choice!")