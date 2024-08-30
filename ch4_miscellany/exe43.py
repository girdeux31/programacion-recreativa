import matplotlib.pyplot as plt

from foo import get_digital_root


print('Exercise 4.3')

digits = 4
roots = []

for a in range(10**(digits-1), 10**digits):
    roots.append(get_digital_root(a))

fractions = [roots.count(i)/len(roots) for i in range(1, 10)]
print(fractions)

plt.hist(roots, color='lightgreen', ec='black', bins=9)
plt.show()

