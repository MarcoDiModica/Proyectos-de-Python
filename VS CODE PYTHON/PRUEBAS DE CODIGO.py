import matplotlib.pyplot as plt
import numpy as np

# plot()
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# scatter()
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.show()

# bar()
languages =['Python', 'Java', 'C', 'C++', 'JavaScript']
popularity = [56, 39, 34, 34, 29]
plt.bar(languages, popularity)
plt.show()

# hist()
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()

# pie()
sizes = [25, 20, 45, 10]
labels = ['Cats', 'Dogs', 'Tigers', 'Goats']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
