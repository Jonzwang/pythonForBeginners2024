# Initialize an empty list to store tasks
todo_list = []

# Start the while loop
while True:
    # Ask the user for a task
    task = input("Enter a TODO task (or 'quit' to exit): ")

    # Check if the user wants to quit
    if task.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered

    # Add the task to the todo_list
    todo_list.append(task)

# Print out the tasks
print("\nYour TODO list:")
for index, task in enumerate(todo_list, start=1):
    print(f"{index}. {task}")