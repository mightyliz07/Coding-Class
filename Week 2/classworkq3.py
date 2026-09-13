attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == "Secure99":
        print("Access Granted")
        break
    else:
        attempts = attempts + 1

if attempts == 3:
    print("Account Locked")                                                                                                                            