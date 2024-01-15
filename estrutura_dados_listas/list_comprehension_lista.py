# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = [i * i for i in range(11)]
print(squares)

a = 97 # Código ASCII do 'a'
z_mais = 123 # Código ASCII do 'z' + 1

# [expression for member in iterable]
print([chr(i) for i in range(a, z_mais)])