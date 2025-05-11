from foo import primorial


print('Exercise 6.3')

limit = 20
for n in range(1, limit+1):
    value = primorial(n)
    print(value)
