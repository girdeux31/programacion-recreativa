from foo import is_powered_number


print('Exercise 4.4')

max_power = 5

for power in range(1, max_power+1):

    numbers = []
    
    for a in range(10**power):
        if is_powered_number(a, power=power):
            numbers.append(a)

    print(f'Powered numbers with power {power}:')
    print(numbers)
