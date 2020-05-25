# Exercise 1
def readposint():
    int_number = -1
    while int_number < 0:
        user_input = input("Please provide a number above 0")
        try:
            int_number = int(user_input)
            if int_number < 0:
                print("You did not enter a positive number")
        except ValueError:
            print("You did not enter a number")

    return print("The square root of your number is", int_number ** 0.5)


readposint()
