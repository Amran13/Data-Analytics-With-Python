import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))  # Create a figure

# Plot 1 (Bar Chart)
y = [23, 45, 41, 13, 7]
x = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5']
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('Sales Plot 2023', fontsize=10)
ax1.grid(axis='y', linestyle='--', linewidth=0.5)
ax1.set_xlabel('Products', fontsize=8)
ax1.set_ylabel('Number of Sales', fontsize=8)
ax1.bar(x, y, color='royalblue')
ax1.tick_params(axis='x', labelsize=8)
ax1.tick_params(axis='y', labelsize=8)

# Plot 2 (Line Chart)
sales1 = [12, 16, 18, 23, 28, 37]
sales2 = [13, 18, 23, 26, 27, 30]
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('Sales of 2023-2024', fontsize=10)
ax2.plot(months, sales1, color='royalblue', marker='o', label='Sales 2023')
ax2.plot(months, sales2, color='lightgreen', marker='o', label='Sales 2024')
ax2.grid(linestyle='--', linewidth=0.5)
ax2.set_xlabel('Months', fontsize=8)
ax2.set_ylabel('Sales Number', fontsize=8)
ax2.legend(fontsize=8)
ax2.tick_params(axis='x', labelsize=8)
ax2.tick_params(axis='y', labelsize=8)

# Plot 3 (Pie Chart)
subjects = ['Sea Weed', 'Coral', 'Sea Grass', 'Shrimp']
productions = [17, 39, 48, 39]
colors = ['lightgreen', 'royalblue', 'skyblue', 'gold']
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title('Marine Production in 2025', fontsize=10)
ax3.pie(productions, labels=subjects, autopct='%1.1f%%',
        colors=colors, textprops={'fontsize': 8})
ax3.legend(loc=3, fontsize=8)

# Plot 4 (Histogram)
ages = [18, 19, 21, 22, 22, 23, 25, 25, 25, 26, 27, 28, 28, 28, 30,
        32, 35, 35, 36, 37, 40, 42, 45, 47, 50, 52, 55, 58, 60, 62]
ax4 = fig.add_subplot(2, 2, 4)
ax4.hist(ages, bins=12, color='skyblue', edgecolor='black')
ax4.set_title('Age Distribution', fontsize=10)
ax4.set_xlabel('Age Range', fontsize=8)
ax4.set_ylabel('Number of People', fontsize=8)
ax4.grid(axis='y', linestyle='--', alpha=0.6)
ax4.tick_params(axis='x', labelsize=8)
ax4.tick_params(axis='y', labelsize=8)

# Add separating lines (in figure coordinates: 0-1 range)
fig.subplots_adjust(wspace=0.3, hspace=0.4)  # Adjust spacing

# Add horizontal and vertical line across the figure
fig_width, fig_height = fig.get_size_inches()
fig.dpi = 100
fig.canvas.draw()

# Use absolute coordinates to draw the lines
fig.lines.append(plt.Line2D([0.5, 0.5], [0.07, 0.95], color='gray', linewidth=1))  # vertical
fig.lines.append(plt.Line2D([0.05, 0.95], [0.5, 0.5], color='gray', linewidth=1))  # horizontal

# Save and show
plt.savefig('Charts/Subplot.png', dpi=300)
plt.show()
