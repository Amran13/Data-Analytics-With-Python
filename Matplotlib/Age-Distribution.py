import matplotlib.pyplot as plt

ages = [18, 19, 21, 22, 22, 23, 25, 25, 25, 26, 27, 28, 28, 28, 30,
        32, 35, 35, 36, 37, 40, 42, 45, 47, 50, 52, 55, 58, 60, 62]

plt.hist(ages, bins=12, color='orchid', edgecolor='black')

plt.title('Age Distribution')
plt.xlabel('Age Range')
plt.ylabel('Number of People')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('Charts/age-distribution.png')
plt.show()
