import math

from foo import are_congruents, is_divisor


print('Exercise 2.5')

total = 0
a_min = 100
a_max = 1000
b_max = a_max
m = 42

for a in range(a_min, a_max+1):
    for b in range(a_min, b_max+1):
        if a != b and are_congruents(a, b, m):
            total += 1

print(total)
print(is_divisor(m, total))