def number_of_letters(element, string):
    if element != " ":
        amount = string.count(element)
        print(f"{element} - {amount}; ", end = "")
        return 0
#function to display letters and their number in a string.

string = input("Enter the string: ").lower()

print("All characters in a string: ", end = "")
for element in set(string):
    number_of_letters(element, string)

print("\n==================================================================================")

print("All sorting characters in a string: ", end = "")
for element in sorted(set(string)):
    number_of_letters(element, string)