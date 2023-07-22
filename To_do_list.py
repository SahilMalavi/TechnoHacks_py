import pandas as pd

# Create a new to-do list
to_do_list = pd.DataFrame(columns=["Task", "Due-Date", "Completed"])


# Add a new task to the to-do list
def add_task(task, due_date):
    try:
        to_do_list.loc[len(to_do_list)] = [task, due_date, False]
        print("\n• Task Added Successfully")
    except ValueError:
        print("Invalid task or due date.")
    except TypeError:
        print("Task or due date must be a string.")


# Mark a task as completed
def mark_task_completed():
    if len(to_do_list) != 0:
        try:
            task_index = int(input("\nEnter the task index (from above):"))

            to_do_list.loc[task_index, "Completed"] = True
            print("\n•Done..!")
        except IndexError:
            print("Task index is out of range.")
    else:
        print("\n• Add at least one task")


# Get all tasks that are not completed
def get_uncompleted_tasks():
    return to_do_list[to_do_list["Completed"] == False]


# Print the to-do list
def print_to_do_list():
    print(to_do_list)


while True:

    print("\n---------------------------------\n1. Add a task")
    print("2. Mark a task as completed")
    print("3. Display all uncompleted tasks")
    print("4. Print the to-do list")
    print("5. Quit")
    print("\nEnter your choice: ", end=" ")
    choice = input()
    print()
    try:
        if choice == "1":
            task = input("Enter the task:")
            due_date = input("Enter the due date (YYYY-MM-DD):")
            add_task(task, due_date)
        elif choice == "2":
            print_to_do_list()
            mark_task_completed()
        elif choice == "3":
            print(get_uncompleted_tasks())
        elif choice == "4":
            print_to_do_list()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
