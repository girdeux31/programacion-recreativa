from foo import is_divisor


print('Exercise 2.1')

b_max = 5
a = b_max

while True:

    if all([is_divisor(a, b) for b in range(1, b_max+1)]):
        break
    else:
        a += 1

print(f'Number \'{a}\' is the smallest integer that can be divided by all integers from 1 up to {b_max}')
