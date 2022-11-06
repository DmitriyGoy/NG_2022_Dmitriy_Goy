list = []

items = input("Enter list items: ").split(",")
list.extend(items)
print("===========================================================================================")

max = list[0]
min = list[0]
for elem in range(1, len(list)):
    if int(list[elem]) > int(max):
        max = list[elem]
    elif int(list[elem]) < int(min):
        min = list[elem]

for elem in list:
    if elem == max or min:
        list.remove(elem)
    continue

sum = 0
for elem in list:
    sum += int(elem)


print(f"The largest element from the list: {max};")
print(f"The smallest element from the list: {min};")
print(f"\nSum of all other elements: {sum}")