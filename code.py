tasks = []

def addTask():
  task = input("Enter Task Here!: ")
  tasks.append(task)
  print(f"✅ Task '{task}' added to the list.") #Code Change Emojis invite a visual appeal/warmth towards the app, also adjusted input


def listTasks():
  if not tasks:
    print("✨ You currently have no tasks! 🎉") #Code change Emojis invite a visual appeal/warmth towards the app,also adjusted input
else:
        print("\n📝 Current Tasks:") 
        for index, task in enumerate(tasks):
            print(f"  {index + 1}. {task}")  # Code Change:Number Adjustment
        print("\n")

def deleteTask():
  listTasks()
  try:
    taskToDelete = int(input("Enter the # to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task #{taskToDelete} was not found.")
  except:
    print("Invalid input.")


if __name__ == "__main__":
  ### Create a loop to run the app
  print("Welcome in! Let's see what we gotta do!:)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      listTasks()
    elif (choice == "4"):
      break
    else:
      print("Invalid input. Let's Try That Again!")

  print("See you later👋! Make sure you continue to stay LockedIn🔒")
