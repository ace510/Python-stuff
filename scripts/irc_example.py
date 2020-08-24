def print_fraction(divided_num, denominator):
    
    while True:
        whole_num = divided_num // denominator # Finds the integer portion of a number
        numerator = divided_num % denominator # Finds the numerator of the remainder

        # If the numerator is 0, do not print a 0/x fraction
        if numerator == 0:
            result = str(whole_num)
            print(result)
            break

        # If the numerator is not 0, print the whole number with the fraction
        else:
            denominator -= 1

print_fraction(40,8)

print_fraction(40,7)

print_fraction(100,9)

print_fraction(483,7)