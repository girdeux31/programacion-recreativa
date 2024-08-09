print('Exercise 3.5b')

kaprekar = 6174

for number in range(1000, 10000):
    
    original_number = number
    iteration = 0

    while number != kaprekar:

        iteration += 1
        ascending = ''.join(sorted(str(number)))
        descending = ascending[::-1]
        number = int(descending) - int(ascending)

        if number == 0:
            iteration = '-'
            break

    print(f'{original_number:4} {iteration}')