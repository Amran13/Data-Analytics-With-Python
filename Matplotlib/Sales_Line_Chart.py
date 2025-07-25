import matplotlib.pyplot as plt

months = ['jan', 'feb', 'mar', 'apr','may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

sales = [1000, 1200, 1500, 1300, 1700, 1800, 1600, 2000, 2100, 2300, 2500, 2700]


plt.plot(months, sales, marker='o', linestyle="dotted", color = 'green', linewidth=2, label="Sales in $")

plt.title('Sales in 2023')
plt.xlabel('Months')
plt.ylabel('Number of Sales')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('Charts/sales-chart.png')

plt.show()
