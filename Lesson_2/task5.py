list = input("Enter list items: ").split(",")
print("===========================================================================================")

list_int = []
for num in range(len(list)):
    list_int.insert(num, int(list[num]))

maximum = list_int.pop(list_int.index(max(list_int)))
minimum = list_int.pop(list_int.index(min(list_int)))

print(f"The largest element from the list: {maximum};")
print(f"The smallest element from the list: {minimum};")

print(f"\nSum of all other elements: {sum(list_int)}.")