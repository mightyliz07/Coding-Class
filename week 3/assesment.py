# --- Part 1: Secure Login ---
correct_password = "Liz"
attempts = 0

# Loop up to 3 times for password entry
while attempts < 3:
    user_input = input("Enter password: ")
    attempts = attempts + 1

    if user_input == correct_password:
        print ("Access Granted")
        break
    else:
        print ("Wrong password, try again.")
    if attempts == 3:
        print ("system lock")   
        #Exits program if login fails exits()

 
        

