tasks = []

def add_task():
    task = input("Enter Task Here!: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added to the list.")  # Code Change Emojis invite a visual appeal/warmth towards the app, also adjusted input


def list_tasks():
    if not tasks:
        print("✨ You currently have no tasks! 🎉")  # Code Change Emojis invite a visual appeal/warmth towards the app, also adjusted input
    else:
        print("\n📝 Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"  {index + 1}. {task}")  # Code Change:Number Adjustment
        print("\n")


def delete_task():
    list_tasks()
    if tasks:  # Code Change: Double checking tasks before deletion
        try:
            task_to_delete = int(input("Enter the number of the task to delete: ")) - 1  # Code Change: 1-based indexing
            if 0 <= task_to_delete < len(tasks):
                removed_task = tasks.pop(task_to_delete)
                print(f"❌ Task '{removed_task}' removed from the list.\n")  # Code Change: Task Removed
            else:
                print("⚠️ Invalid task number. Please try again.\n")  # Code Change: Invalid input
        except ValueError:
            print("⚠️ Please enter a valid number!\n")


def show_menu():
    print("\n")
    print("🔒 Locked-In: Task Management App")
    print("---------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")


if __name__ == "__main__":
    print("Let's get Ready to Locked-In! Let's manage your tasks.\n")
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()  # Code Change: Added `.strip()` to handle extra spaces

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            # Code Change: Exit message with motivational tone!
            print("👋 Goodbye! Stay Locked-In and complete those tasks! 🔒")
            break
        else:
            print("⚠️ Invalid input. Please choose a valid option.\n")
