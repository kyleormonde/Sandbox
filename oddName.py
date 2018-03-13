"""Kyle Alexander Ormonde"""
name = str(input("Name: "))
while not name:
    print("Name cannot be blank.")
    name = str(input("Name: "))
for i in range(0, len(name), 2):
    print(name[i])
