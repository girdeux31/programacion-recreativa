print('Exercise 3.3')

iterations = 10
number = 1

for iter in range(1, iterations+1):

    iter_sum = 0
    txt = ''

    for _ in range(iter):

        iter_sum += number
        txt += f' + {number}'
        number += 2

    txt += f' = {iter}**3 = {iter**3}'

    print(f'{iter} {txt} {iter_sum == iter**3}')
