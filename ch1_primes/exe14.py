from foo import is_sophie_prime
from foo import get_cunningham_chain


print('Exercise 1.4')

n0, n1 = 2, 100

print('n     len   chain')
print('==================================================')

for i in range(n0, n1+1):

    chain = get_cunningham_chain(i)
    print(f'{i:5d} {len(chain):5d} {chain}')
