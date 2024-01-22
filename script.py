# Your code below:
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
cubes = []

# for loop
for digit in single_digits:
  print(digit)

  # appending the digits' squares to the squares list
  squares.append(digit ** 2)
  print(squares)

# list comprehension -> single digits to the cubes list
cubes = [digit ** 3 for digit in single_digits]

print(cubes)
