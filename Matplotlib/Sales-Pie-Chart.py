import matplotlib.pyplot as plt

sales = [3000, 2900, 2119, 3443]
location = ['Dhaka', 'Barisal', 'Rajshahi', 'Khulna']
color = ['salmon', 'gold', 'royalblue', 'lightgreen']

plt.pie(sales, labels=location, colors=color, autopct='%1.1f%%')
plt.legend()

plt.show()