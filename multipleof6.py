def get_multiple_6():
    """
    Returns a multiple of 6 that was entered by the user
    :return: int a number
    """
    while True:
        try:
            n = input("Please give me a multiple of 6: ")
            n = input(n) # convert to int
            # how to check if it is a multiple of 6
            if n / 6 == n // 6:
                return n
            else:
            print("that is not a multiple of 6")
    except ValueError:
        print("you have not entered a number")

print(get_multiple_6())
