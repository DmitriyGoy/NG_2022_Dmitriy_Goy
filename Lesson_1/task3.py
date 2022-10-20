finish = ("")
while finish != "exit":
    sec_user = int(input("Enter the number of seconds: "))

    sec = sec_user % (24 * 3600)
    min = sec_user // 60
    sec %= 60
    hours = min // 60
    min %= 60
    days = hours // 24
    hours %= 24
    print(f"Days: {days};\nHours: {hours};\nMinutes: {min};\nSeconds: {sec}.")

    finish = input("Type 'exit' to finish: ")


