from foo import get_all_divisors


print('Exercise 2.2')

n_max = 1300
output = []

for a in range(1, n_max+1):

    a_divisors = get_all_divisors(a)

    for b in range(a+1, n_max+1):
        
        b_divisors = get_all_divisors(b)

        if sum(a_divisors) == b and sum(b_divisors) == a:
            output.append((a, b))

print(f'Friend numbers up to {n_max}:')

for out in output:
    print(out)