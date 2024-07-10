from foo import is_prime


print('Exercise 1.1')

n = 36444293
out = is_prime(n)
print(f'{n} is' + (' ' if out else ' not ') + 'prime')

n += 1
out = is_prime(n)
print(f'{n} is' + (' ' if out else ' not ') + 'prime')
