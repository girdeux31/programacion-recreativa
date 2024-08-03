from foo import get_ramanujan_number


print('Exercise 3.1')

n_max = 100
ramanujan = []
numbers = []
output = {}

for a in range(1, n_max+1):
    for b in range(a+1, n_max+1):

        r = get_ramanujan_number(a, b)
        ramanujan.append(r)
        numbers.append((a, b))

for (a, b), r in zip(numbers, ramanujan):

    count = ramanujan.count(r)
   
    if count > 1:

        output[r] = []

        for _ in range(count):
            idx = ramanujan.index(r)
            ramanujan.pop(idx)
            ab = numbers.pop(idx)
            output[r].append(ab)

print(f'There are {len(output)} combinations')

for key, values in output.items():

    values_as_str = [str(val) for val in values]
    values_as_str = ", ".join(values_as_str)
    print(f'{key:8} {values_as_str}')
