from foo import is_prime, is_marsenne_prime, marsenne


print('Exercise 1.3')

upper_limit = 15

for n in range(1, upper_limit):

    if is_prime(n):
    
        m = marsenne(n)
        out = is_marsenne_prime(n)

        if not out:
            print(f'n={n}, M(n)={m}, is not marsenne prime')
