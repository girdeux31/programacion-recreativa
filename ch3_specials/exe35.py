print('Exercise 3.5')

kaprekar = 6174
number = 3452  # must be a 4-digit number with no more than 2 repeated digits
iteration = 0

while number != kaprekar:

    iteration += 1
    ascending = ''.join(sorted(str(number)))
    descending = ascending[::-1]
    number = int(descending) - int(ascending)

    if number == 0:
        raise ValueError(f'Not posible to continue')

    print(f'{iteration:02}: {descending} - {ascending} = {number}')