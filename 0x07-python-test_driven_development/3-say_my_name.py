def say_my_name(first_name, last_name=""):
    first_name = str(input("enter your first name: "))
    last_name = str(input("enter your last name: "))
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    print(f"My name is {:s} {:s}".format(first_name, last_name))
