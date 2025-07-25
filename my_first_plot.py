import matplotlib.pyplot as plt

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Sat']
y = [10, 12, 7, 9, 13]


plt.plot(x, y)
plt.grid()
plt.title('Backery Shop Analysis')
plt.xlabel('Days')
plt.ylabel('Number of Cookies sold')
plt.show()