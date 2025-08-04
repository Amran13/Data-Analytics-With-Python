import matplotlib.pyplot as plt


salinity = [37.3, 36.0, 35.3, 35.0, 33.5, 33.0, 37.0, 36.7, 35.2, 34.8, 34.5, 34.5, 34.4, 34.3, 34.1]

temp = [15, 14.2, 12.1, 10, 9, 8, 13.2, 12.7, 6.4, 4.9, 4, 3.5, 3, 2.6, 1.5]

depth = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]


fig, axes = plt.subplots(1, 2, figsize=(12, 8), sharey=True)


fig.suptitle("Temperature, Salinity, and Depth Profile using Python (MS-201)", fontsize=16, y=0.95)


axes[0].plot(salinity, depth, marker='o', linestyle='-', color='blue')
axes[0].invert_yaxis()
axes[0].set_xlabel("Salinity (‰)")
axes[0].xaxis.set_label_position('top')
axes[0].xaxis.tick_top()
axes[0].set_ylabel("Depth (m)")
axes[0].set_xlim(30, 40)
axes[0].set_ylim(1500, 0)
axes[0].grid(True, linestyle='--', linewidth=0.5)
axes[0].set_title("Salinity-Depth Profile", pad=30)


axes[1].plot(temp, depth, marker='o', linestyle='-', color='red')
axes[1].invert_yaxis()
axes[1].set_xlabel("Temperature (°C)")
axes[1].xaxis.set_label_position('top')
axes[1].xaxis.tick_top()
axes[1].set_xlim(22, 0)
axes[1].grid(True, linestyle='--', linewidth=0.5)
axes[1].set_title("Temperature-Depth Profile", pad=30)


plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()
