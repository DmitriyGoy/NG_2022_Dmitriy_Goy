list = input("Enter list items: ").split(",")
print("===========================================================================================")

list_int = []
for elem in range(len(list)):
    list_int.insert(elem, int(list[elem]))

maximum = max(list_int)
minimum = min(list_int)

print(f"The largest element from the list: {maximum};")
print(f"The smallest element from the list: {minimum};")

for number in list_int:
    if number == maximum:
        list_int.remove(number)
        
for number in list_int:
    if number == minimum:
        list_int.remove(number)

print(f"\nSum of all other elements: {sum(list_int)}.")