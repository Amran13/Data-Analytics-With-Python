import matplotlib.pyplot as plt


labels = ['Infected', 'Recovered', 'Death']
cases = [3500, 5000, 500]
colors = ['orange', 'green', 'red']

plt.pie(cases, labels=labels , colors=colors, autopct='%.1f%%')
plt.title('Covid19 Case Distribution')
plt.axis('equal')
plt.tight_layout()

plt.savefig('Charts/covid19-case.png')
plt.show()
