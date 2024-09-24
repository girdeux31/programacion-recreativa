import itertools
import numpy as np
from foo import check_eulers_conjecture


print('Exercise 4.7')

# Euler's conjecture
# \sum_{i=1}^k a_i^n != b^n
# where a and b != 0 and n > 1

# See some solutions in https://en.wikipedia.org/wiki/Euler%27s_sum_of_powers_conjecture

# FIXME: too slow
k = 4
n = 5
max_number = 145
# faster ;)
k = 3
n = 3
max_number = 7


coef = np.ones(k+1)

for coef in itertools.combinations(range(1, max_number), k+1):
           
    if check_eulers_conjecture(np.array(coef), n):

        coef_str = [f'{c}^{n}' for c in coef[:-1]]
        coef_str = '+'.join(coef_str)
        b_str = f'{coef[-1]}^{n}'
        print(f'{coef_str} = {b_str} = {coef[-1]**n}')
