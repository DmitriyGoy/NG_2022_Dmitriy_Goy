list = [  ]

list_user = input("Enter list items: ").split(",")
list.extend(list_user)

print(set(list))