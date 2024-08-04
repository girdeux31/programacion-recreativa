from foo import is_narcissist


print('Exercise 3.2')

digits = 7
output = []

for n in range(10**(digits-1), 10**digits):

    if not n % 10**(digits-1):
        print(n)

    if is_narcissist(n):
        output.append(n)

print(f'Narcissits numbers with {digits} digits')
print(output)
