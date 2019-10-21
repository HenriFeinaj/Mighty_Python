def letter(x, y):
  
  letter_1 = ( y[:2] + x[2:] )
  letter_2 = ( x[:2] + y[2:] )
  return (letter_1 + ' ' + letter_2)

print(letter('abc', 'xyz'))
