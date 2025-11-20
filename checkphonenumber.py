def isphonenumber(number):
    if len(number) != 12:
        return False

    # Check first 3 characters are digits
    if not number[:3].isdigit():
        return False

    # Check first hyphen
    if number[3] != '-':
        return False

    # Check next 3 digits
    if not number[4:7].isdigit():
        return False

    # Check second hyphen
    if number[7] != '-':
        return False

    # Check last 4 digits
    if not number[8:].isdigit():
        return False

    return True


# Test
print(isphonenumber("415-555-4242"))   # True
print(isphonenumber("415-55-4242"))    # False
