def print_digits():
    tens_digit = int(input("Enter the number: "))
    ones_digit = int(input("Enter the number: "))
    if tens_digit <= 9 or tens_digit <= 1:
        if ones_digit <= 9 or ones_digit <= 0:
            print(f"The tens digit is {tens_digit} and the ones digits is {ones_digit}")
        else:
            print("Error: Input is not a two-digit number.")