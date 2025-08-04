import matplotlib.pyplot as plt


temp = [15, 14.2, 12.1, 10, 9 ,8, 13.2, 12.7, 6.4, 4.9, 4, 3.5, 3, 2.6, 1.5]


depth = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]

plt.figure(figsize=(6, 8))


plt.plot(temp, depth, marker='o', linestyle='-')


plt.gca().invert_yaxis()


plt.xlabel("Temperature (C)")


plt.gca().xaxis.set_label_position('top')
plt.gca().xaxis.tick_top()


plt.ylabel("Depth (m)")


plt.title("Temperature-Depth Profile || (MS-201) ", pad=30) 

plt.grid(True, linestyle='--', linewidth=0.5)


plt.xlim(22, 0)
plt.ylim(1500, 0)

plt.show()
