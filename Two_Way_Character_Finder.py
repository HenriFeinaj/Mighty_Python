#========================================
#TWO-WAY CHARACTER FINDER IN GIVEN STRING
#========================================

sequence = "Monty Python"
character = str(input())
for index in range(len(sequence)):
    if character == sequence[index]:
        print("Character Found!")
        break
    else:
        print("Failure")

#========================================


sequence = "Monty Python"
character = str(input())

if character in sequence:
    print("Character Found!")
else:
    print("Failure")

#========================================    
