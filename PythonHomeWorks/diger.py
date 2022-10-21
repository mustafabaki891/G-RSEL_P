tasks = open("todos.txt")

for todo in tasks:
    print(todo, end="")

tasks.close()