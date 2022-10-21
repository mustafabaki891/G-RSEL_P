todos = open("todos.txt", "a")

print("ekmek al", file = todos)
print("python al", file = todos)
print("ev ödevi", file = todos)

todos.close()