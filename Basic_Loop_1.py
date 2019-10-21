#BASIC LOOP APPLICATION

n = int(input("Enter only a positive integer number: "))

while n < 0:
    n = int(input("Enter only a positive integer number: "))

sum = 0
x = 1
while x <= n:
    sum += x
    x += 1
print("The sum is: ", sum)
