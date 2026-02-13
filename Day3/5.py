class InValidNameLengthException(Exception):
    pass

class InValidNameException(Exception):
    pass


def validate(fname, lname):
    if len(fname) <= 3 or len(lname) <= 3:
        raise InValidNameLengthException("Length must be more than 3")

    if not fname.isalpha() or not lname.isalpha():
        raise InValidNameException("Only characters are allowed")


try:
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")

    validate(fname, lname)

    print("First Name:", fname)
    print("Last Name:", lname)

except InValidNameLengthException as e:
    print(e)

except InValidNameException as e:
    print(e)