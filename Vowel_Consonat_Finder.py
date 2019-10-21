#Vowel or Consonat Finder

#Input of a letter from the user.
letter = input("Enter a letter from the alphabet: ")

#Find if the letter is a vowel or a consonat.

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter you have entered is a vowel! ")
elif letter == "y":
    print("Y it's sometimes a vowel and sometimes it's a consonant")
else:
    print("The letter you have entered is a consonant")


