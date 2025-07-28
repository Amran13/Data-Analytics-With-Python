import matplotlib.pyplot as plt
products = ['A1', 'B1', 'C1', 'D1']
products2 = ['A2', 'B2', 'C2', 'D2']
sales = [1000, 1500, 400, 1200]
sales2 = [1200, 1400, 400, 1800]

plt.bar(products, sales, color="blue", width=.7, label="Sales 2020")
plt.bar(products2, sales2, color="skyblue", width=.7, label="Sales 2021")
plt.xlabel("Products")
plt.ylabel('Sales Number')
plt.title('Sales report of XYZ limited')
plt.legend()
plt.grid(axis='y',linestyle="--", alpha=.5)

plt.savefig('Charts/sales-bar-chart.png')
plt.show()