import matplotlib.pyplot as plt

days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5',
        'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10']
temperature = [28, 30, 33, 31, 29, 32, 34, 33, 31, 30]

plt.plot(days, temperature, color='orange', linewidth=2, label='Temperature (°C)')
plt.fill_between(days, temperature, color='orange', alpha=0.3)

plt.title('10-Day Temperature Trend')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
