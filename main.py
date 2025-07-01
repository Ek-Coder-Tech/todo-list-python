from colorama import init, Fore, Style
init(autoreset=True)

import os

tasks = []

# Load tasks from file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                title, done = line.strip().split("|")
                tasks.append({"title": title, "done": done == "True"})


# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['title']}|{task['done']}\n")


# Show all tasks
def show_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks):
        if task["done"]:
            status = Fore.GREEN + "✓"
        else:
            status = Fore.RED + "✗"

        print(f"{i + 1}. {task['title']} [{status}]")


# Add a new task
def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print(Fore.GREEN + "Task added.")


# Mark a task as done
def mark_done():
    show_tasks()
    index = int(input("Enter task number to mark done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(Fore.GREEN + "Task marked as done.")


# Delete a task
def delete_task():
    show_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print(Fore.YELLOW + "Task deleted.")


# Main function
def main():
    load_tasks()
    print(Fore.CYAN + "\n=== WELCOME TO YOUR TO-DO LIST APP ===\n")

    while True:
        print(
            "\n1. Add Task\n2. View Tasks\n3. Mark Done\n4. Delete Task\n5. Clear All Tasks\n6. Exit"
        )

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            confirm = input(
                "Are you sure you want to clear all tasks? (yes/no): ")
            if confirm.lower() == "yes":
                tasks.clear()
                print(Fore.YELLOW + "All tasks cleared.")


        elif choice == "6":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Try again.")



# Call the main function to start the app
main()
