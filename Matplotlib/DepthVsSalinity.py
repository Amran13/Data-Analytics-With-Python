import matplotlib.pyplot as plt


salinity = [37.3, 36.0, 35.3, 35.0, 33.5, 33.0, 37.0, 36.7, 35.2, 34.8, 34.5, 34.5, 34.4, 34.3, 34.1]


depth = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]

plt.figure(figsize=(6, 8))


plt.plot(salinity, depth, marker='o', linestyle='-')


plt.gca().invert_yaxis()


plt.xlabel("Salinity (‰)")


plt.gca().xaxis.set_label_position('top')
plt.gca().xaxis.tick_top()


plt.ylabel("Depth (m)")


plt.title("Salinity-Depth Profile || (MS-201) ", pad=30) 

plt.grid(True, linestyle='--', linewidth=0.5)


plt.xlim(30, 40)
plt.ylim(1500, 0)

plt.show()
