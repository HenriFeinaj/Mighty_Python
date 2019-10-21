def odd_erase(str):
  word_given = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      word_given = word_given + str[i]
  return word_given

print(odd_erase('ABCDEFG'))
