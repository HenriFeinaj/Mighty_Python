def odd_even():
    number = int(input("Enter number: "))
    if (number % 2) == 0:
        return number, "is an even! "
    else:
        return number, "is an odd! "

print (odd_even())


