# --- Part 2: The Brute-Forcer (For Loop) ---
secret_pin = 8421

#Loop through all possible 4-digit PINs from 0 to 9999
for current_guess in range(10000):
    # Print every 1000th attempt to show progress
    if current_guess % 1000 == 0:

    # Check if the guess mathces the secret PIN
     if current_guess == secret_pin:
        print("PIN Crscked! The number was:", current_guess)
        break