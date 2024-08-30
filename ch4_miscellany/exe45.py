from foo import get_collatz_reduction, inverted


print('Exercise 4.5')

max_digits = 5

for digits in range(1, max_digits+1):

    numbers = []

    for a in range(10**(digits-1), 10**digits):

        if len(get_collatz_reduction(a)) == inverted(a):
            numbers.append(a)

    print(f'Numbers with {digits} digits that inverted is equal to the number of iterations to reduce it to 1')
    print(numbers)
