import matplotlib as mpl
import matplotlib.pyplot as plt

from foo import get_collatz_reduction


print('Exercise 4.5')

file = 'exe45_len.png'
max_number = 10**4
color_map = 'plasma'
y_max = 300
size = 4
numbers = []
colors = []

cmap = mpl.colormaps[color_map]

for a in range(2, max_number+1):

    maximum = len(get_collatz_reduction(a))
    numbers.append(maximum)
    colors.append(cmap(maximum/y_max))

plt.scatter(range(2, max_number+1), numbers, s=size, c=colors)
plt.gca().set_ylim([0, y_max])
plt.xlabel('Input number')
plt.ylabel('Collatz length')
plt.savefig(file)
plt.show()
