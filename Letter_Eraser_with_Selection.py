#Function for erasing a specific letter from a sting.
def letter_erase(str, n):
      x = str[:n] 
      y = str[n+1:]
      return (x + y)
#This part prints the word without the third letter.
#Or whatever the letter we want to erase depending its number location.(For example: 5 for the letter "N")
print(letter_erase('Python', 3))
