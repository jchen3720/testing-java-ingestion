import random

while True:
    try:
        num = float(input("Enter a positive number (or a negative number to exit): "))
        if num < 0:
            print("Exiting program.")
            break
        elif num == 0:
            print("Please enter a number greater than zero.")
            continue
        random_num = random.uniform(0, num)
        print(f"Random number between 0 and {num}: {random_num}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
