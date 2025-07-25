import matplotlib.pyplot as plt

months = ['jan', 'feb', 'mar', 'apr','may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

salesOf23 = [1000, 1200, 1500, 1300, 1700, 1800, 1600, 2000, 2100, 2300, 2500, 2700]

salesOf24 = [900, 1200, 1400, 1800, 1700, 2000, 1800, 2200, 2100, 2400, 2500, 2900]


plt.plot(months, salesOf23, marker='o', linestyle="dotted", color = 'green', linewidth=2, label="Sales in 2023")
plt.plot(months, salesOf24, marker='o', linestyle="solid", color = 'blue', linewidth=2, label="Sales in 2024")

plt.title('Sales in 2023-2024')
plt.xlabel('Months')
plt.ylabel('Number of Sales')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('Charts/sales-chart.png')

plt.show()
