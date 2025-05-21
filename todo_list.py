#The application will allow to add, a todo to a list.
#After each addition it will print the list of todos.

todo_list = []

while True:    
    todo_description = input("Enter a todo description: ")
    todo_date = input("Enter a todo date (YYYY-MM-DD): ")

    todo = {
        "description": todo_description,
        "date": todo_date
    }
    
    todo_list.append(todo)
    print("Todo list:")
    for todo in todo_list:
        print(f"Description: {todo['description']}, Date: {todo['date']},")