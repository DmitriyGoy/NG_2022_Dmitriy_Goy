def number_of_letters():
    if element != " ":
        amount = string.count(element)
        print(f"{element} - {amount}; ", end = "")
#function to display letters and their number in a string.

string = input("Enter the string: ").lower()

print("All characters in a string: ", end = "")
for element in set(string):
    number_of_letters()

print("\n==================================================================================")

print("All sorting characters in a string: ", end = "")
for element in sorted(set(string)):
    number_of_letters()