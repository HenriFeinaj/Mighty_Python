def first_last_2_characters(str):  
  if len(str) < 2:  
    return "" 
  else:
      return str[0:2] + str[-2:]  
  
print(first_last_2_characters('programing'))  
print(first_last_2_characters('p1'))  
print(first_last_2_characters('p'))
