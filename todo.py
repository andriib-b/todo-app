# Simple To-Do List App

tasks = []

def show_tasks():
    if not tasks:
        print("✅ No tasks yet")
    else:
        print("\n📋 To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"➕ Task added: {task}")

def remove_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"❌ Task removed: {removed}")
    except IndexError:
        print("⚠️ Invalid task number")

if __name__ == "__main__":
    while True:
        print("\nOptions: [1] Show tasks  [2] Add task  [3] Remove task  [4] Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            index = int(input("Enter task number to remove: "))
            remove_task(index)
        elif choice == "4":
            break
        else:
            print("⚠️ Invalid option")
