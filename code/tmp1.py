import matplotlib.pyplot as plt

# Provided sequence of numbers
data = [6, 7, 15, 15, 6, 12, 3, 14, 10, 6, 4, 6, 11, 12, 14, 13, 14, 13, 11, 10, 15, 14, 11, 10, 6, 13]
data = 
# Plot histogram
n, bins, _ = plt.hist(data, bins=range(0,16), edgecolor='black')
print(len(data))
print(n.sum())
print(n)
print(bins)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Provided Data')
plt.grid(True)
plt.show()


