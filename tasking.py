def task():
    tasks = []
    print("--- Welcome to the Task Management App ---")
    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    print(f"Today's tasks are:\n{tasks}")
    
    while True:
        operation = int(input("Enter an option:\n1 - Add Task\n2 - Update Task\n3 - Delete Task\n4 - View Tasks\n5 - Exit\nYour choice: "))
        
        if operation == 1:  # Add Task
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")
        
        elif operation == 2:  # Update Task
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task has been updated to: '{up}'.")
            else:
                print("Task not found!")
        
        elif operation == 3:  # Delete Task
            delete_task = input("Enter the task you want to delete: ")
            if delete_task in tasks:
                tasks.remove(delete_task)
                print(f"Task '{delete_task}' has been successfully deleted.")
            else:
                print("Task not found!")
        
        elif operation == 4:  # View Tasks
            print(f"Current tasks:\n{tasks}")
        
        elif operation == 5:  # Exit
            print("Exiting Task Management App. Goodbye!")
            break
        
        else:
            print("Invalid operation. Please try again.")

# Run the task function
if __name__ == "__main__":
    task()