from foo import is_inverted_squared


print('Exercise 4.2')

max_number = 10000

for a in range(max_number, 0, -1):

    if is_inverted_squared(a):
        break

print(f'The biggest number (up to {max_number}) that is a inverted squared is {a}')
