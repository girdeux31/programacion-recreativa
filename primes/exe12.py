from foo import are_twin_primes


print('Exercise 1.2')

upper_limit = 21

for x in range(1, upper_limit):

    n = 30*(2*x-27)*(x-15)
    out = are_twin_primes(n-1, n+1)

    if not out:
        print(f'x={x}, {n-1} and {n+1} are not twin primes')

# import matplotlib.pyplot as plt  

# plt.plot(
#     range(1, upper_limit),
#     [30*(2*x-27)*(x-15) for x in range(1,21)],
#     'ro-'
# )
# plt.show()