from foo import is_perfect, is_abundant, is_deficient


print('Exercise 2.4')

out = {'perfects': 0, 'abundants': 0, 'deficients': 0}
perfects = []

n_max = 10**4

for n in range(1, n_max+1):

    if is_perfect(n):
        out['perfects'] += 1
        perfects.append(n)
    elif is_abundant(n):
        out['abundants'] += 1
    elif is_deficient(n):
        out['deficients'] += 1

print(out)
print(f'Perfects numbers up to {n_max} are:')
print(perfects)