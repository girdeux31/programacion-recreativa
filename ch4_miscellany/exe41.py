from foo import get_consecutive_sums


print('Exercise 4.1')

max_number = 1000
max_length = 0
consecutives = {}

for a in range(max_number):

    cs = get_consecutive_sums(a)

    if len(cs) > 0:
        consecutives[a] = cs

        if len(cs) > max_length:

            max_length = len(cs)
            max_a = a

print(f'Number with more consecutives sumes is {max_a} with {max_length} different sums\n')

for cs in consecutives[max_a]:

    cs_str = [str(i) for i in cs]
    cs_str = '+'.join(cs_str) + ' = ' + str(max_a)
    print(cs_str)


