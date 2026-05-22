while True:
    # Input phase
    hours = input("How many hours of sleep did you get last night? ")

    # Error handling phase
    try:
        hours = float(hours)
    except ValueError:
        print("Incorrect input! Please only enter a NUMBER for hours!")
        continue

    # Processing phase
    if hours >= 8:
        message = "Great job! You got enough sleep!"
    else:
        message = "You should try to get more sleep tonight."

    # Output phase
    print(message)
    choice = input("Type any key to continue\nOR press ENTER to quit.")
    if choice == "":
        break

input("Press ENTER to exit...")