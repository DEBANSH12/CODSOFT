tasks = []

def addTasks():
    task = input("Enter today's Task: ")
    tasks.append(task)
    print(f"Task '{task}' has been entered successfully")

def delTasks():
    listTasks()
    try:
        tasksToDelete = int(input("Enter the # number of tasks you want to delete: "))
        if 0 <= tasksToDelete < len(tasks):
            tasks.pop(tasksToDelete)
            print("The item has been deleted")
        else:
            print(f"The task #{tasksToDelete} to be deleted was not found")
    except ValueError:
        print("Invalid Input: Please enter a valid task number.")

def listTasks():
    if not tasks:
        print("There are no tasks listed currently")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

if __name__ == "__main__":
    print("WELCOME TO MY NEW TO DO APP :)")
    while True:
        print("\nPlease select one of the following options:")
        print("*****************************************")
        print("1. ADD A NEW TASK")
        print("2. DELETE THE TASK OF YOUR CHOICE")
        print("3. LIST ALL THE TASKS")
        print("4. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTasks()
        elif choice == "2":
            delTasks()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            print("Thanks for using my app!")
            break
        else:
            print("Invalid Input: Please enter a number between 1 and 4.")



            



    
    

    

  
