""" Program that plots a trigonometric function """
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(2, 10)

print(type(data))
print("-" * 20)
print(data)
print("-" * 20)
print(data[0])
print("-" * 20)
print(data[0, 0])

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].boxplot([data[0], data[1]])
axs[1, 1].hist2d(data[0], data[1])

plt.show()
