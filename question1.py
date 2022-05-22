arraysnames = []

count = 0
i = []

for count in range(4):
    username = str(input("\n"))
    arraysnames.append(username)

    i = arraysnames.index(username)
    print(f"Nome = {username}", "\n",  "Posição =", i)