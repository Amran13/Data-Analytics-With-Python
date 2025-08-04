import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8) )
# Plot 1 (Bar Chart)
y = [23, 45, 41, 13, 7]
x = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5']
plt.subplot(2, 2, 1)
plt.title('Sales Plot 2023')
plt.grid(axis='y',linestyle = '--', linewidth = 0.5)
plt.xlabel('Products')
plt.ylabel('Number of Sales')
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.bar(x, y, color='royalblue')


#plot 2 (Line Chart)
sales1 = [12, 16, 18, 23, 28, 37]
sales2 = [13, 18, 23, 26, 27, 30]
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
plt.subplot(2, 2, 2)
plt.title('Sales of 2023-2024')
plt.plot(months, sales1, color='royalblue', marker='o', label='Sales 2023')
plt.plot(months, sales2, color='lightgreen', marker='o', label='Sales 2024')
plt.grid(linestyle='--', linewidth=.5)
plt.xlabel('Months')
plt.ylabel('Sales Number')
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend()


# Plot 3 (Pie Chart)
subjects = ['Sea Weed', 'Coral', 'Sea Grass', 'Shrimp']
productions = [17, 39, 48, 39]
colors = ['lightgreen', 'royalblue', 'skyblue', 'gold']
plt.subplot(2,2,3)
plt.title('Marine Production in 2025')
plt.pie(productions, labels=subjects, autopct='%1.1f%%', colors=colors, textprops={'fontsize': 8})
plt.legend(loc=3, fontsize=8)


#plot 4 (Histogram)
ages = [18, 19, 21, 22, 22, 23, 25, 25, 25, 26, 27, 28, 28, 28, 30,
        32, 35, 35, 36, 37, 40, 42, 45, 47, 50, 52, 55, 58, 60, 62]
plt.subplot(2,2,4)
plt.hist(ages, bins=12, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age Range')
plt.ylabel('Number of People')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)



plt.tight_layout()
fig = plt.gcf()  # Get the current figure

# Horizontal line across the middle
fig.lines.append(plt.Line2D([0.05, 0.95], [0.5, 0.5], color='r', linewidth=1))

# Vertical line down the center
fig.lines.append(plt.Line2D([0.5, 0.5], [0.05, 0.95], color='gray', linewidth=1))
plt.savefig('Charts/Subplot.png', dpi=300)
plt.show()
