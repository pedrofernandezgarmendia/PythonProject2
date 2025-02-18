def get_multiple_6():
    """
    Returns a multiple of 6 that was entered by the user
    :return: int - a number that is a multiple of 6.
    """
    while True:
        try:
            n = int(input("Please give me a multiple of 6: "))
            # how to check if it is a multiple of 6
            if n % 6 == 0:
                return n
            else:
                print("that is not a multiple of 6. Try again")
        except ValueError:
            print("you have not entered a number. Try again")

print(get_multiple_6())
