from foo import is_inverted_squared


print('Exercise 4.2b')

max_number = 10000
numbers = []

for a in range(max_number):

    if is_inverted_squared(a):
        numbers.append(a)

print(f'All inverted squares (up to {max_number}) are:')
print(numbers)