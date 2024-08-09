from foo import is_lychrel


print('Exercise 3.4')

max_iterations = 40
max_number = 300

for n in range(max_number):

    if is_lychrel(n, max_iterations=max_iterations):
        print(n)
