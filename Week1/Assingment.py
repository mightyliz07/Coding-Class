# bootcamp_validatro.py
# Program to collect, validate, and summarize user registration details for a robotics bootcamp.

def main():
    print("=== Weekend Robotics Bootcamp Registration ===\n")
    # 1. First Name - Validation : Prsence check to ensure field is not empty
    while True:
        first_name = input("Enter your first name: ").strip()
        if first_name != "":
            break
        print("Error: First name cannot be left blank. please try again.")
    # 2. Age - Validation: Uses try-except to catch non-integer inputs without crashing
    while True:
        try:
            user_age_input = input("Enter your age.")
            user_age = int(user_age_input)
            break
        except ValueError:
            print("Invalid input. Please enetr a whole number for age.")
    # 3. Distance - Validation: Uses try-expect to handle flot conversion errors
    while True:
        try:
            user_distance_input = input("Enter distance from Tech Hub in km (e,g., 5.5):")
            user_distance = float(user_distance_input)
            break
        except ValueError:
            print("Invalid input. Please enetr a valid decimal munber for destance. ")
    # 4. Hardware Required - Validation: Maps "yes"/"No" text inputs to Boolean True/False
    while True:
        hardware_input = input("Do you require hardware? (Yes/No): ").strip().lower()
        if hardware_input in ["yes", "y"]:
            hardware_required = True
            break
        elif hardware_input in ["no", "n"]:
            hardware_required = False
            break
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")
    # Main 
main()