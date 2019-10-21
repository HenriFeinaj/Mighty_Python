def countdown(n):
    if n == 0:
        print("The number should not be 0!")
    elif n < 0:
        return "The number should not be negative"
    else:
        print(n)
        countdown(n-1)

x = int(input("Enter your number: "))
countdown(x)
