from lab2 import a, b, y_func, fmt
import numpy as np
import matplotlib.pyplot as plt
from lab3 import uniform, normal
import mplcyberpunk

#1
n = 100
array = np.linspace(a, b, n)
funcarray = np.empty(len(array))

for i in range(len(array)):
    funcarray[i] = y_func(array[i])

print(' '.join(fmt(x) for x in funcarray))

#2
plt.plot(array, funcarray, label = "f(x)")

plt.xlabel("X-axis", fontsize = 10)
plt.ylabel("Y-axis", fontsize = 10)
plt.title("y = 2/(sinx + 4) plot", fontsize = 12)
plt.legend()

plt.savefig('graph1.png')

plt.clf()

#3
plt.plot(array, funcarray, marker = ".", markersize = 5, color = "#0000FF", markerfacecolor = "#FF0000", markeredgecolor = "#FF0000")
plt.xlabel("X-axis", fontsize = 10)
plt.ylabel("Y-axis", fontsize = 10)
plt.grid(color='green', alpha = 1)
plt.title("y = 2/(sinx + 4) plot", fontsize = 12)

plt.savefig('graph2.png')
plt.clf()

#4
plt.hist(uniform, bins=10, color='green')
plt.title("Histogram for uniform distribution", fontsize = 10)

plt.savefig('histogram1.png')
plt.clf()

plt.hist(normal, bins=20, color='red')
plt.title("Histogram for normal distribution", fontsize = 10)

plt.savefig('histogram2.png')
plt.clf()

#5
uniformints = np.random.randint(1, 5, 50)
counts, _ = np.histogram(uniformints, bins=4)
groups = [f"Число {i}" for i in range (1, 5)]
colors = ["#32CD32", "#2E8B57", "#808000", "#8FBC8F"]
plt.bar(groups, counts, color = colors)
plt.title("Vertical diagram")

plt.savefig('diagram1.png')
plt.clf()

fig, ax = plt.subplots()
colors = ["#1E90FF", "#B0E0E6", "#7B68EE", "#8A2BE2"]
ax.pie(counts, labels = groups, colors = colors)

plt.savefig('diagram2.png')
plt.clf()

#6
x1 = np.linspace(a, b, n)
x2 = np.linspace(a, b, n)
x1, x2 = np.meshgrid(x1, x2)
z = (x1 - 4)**2 + (x2 - 2)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x1, x2, z, color = "red")

plt.savefig('3dgraph1.png')
plt.clf()

#7
fig = plt.figure(figsize=(10, 10))
fig.suptitle("Graph grid 2x2", fontsize=12)

ax1 = fig.add_subplot(221)
ax1.plot(array, funcarray, label="f(x)")
ax1.set_xlabel("X-axis", fontsize=10)
ax1.set_ylabel("Y-axis", fontsize=10)
ax1.set_title("Plot 1", fontsize=12)
ax1.legend()

ax2 = fig.add_subplot(222)
ax2.plot(array, funcarray, marker=".", markersize=5,
         color="#0000FF", markerfacecolor="#FF0000", markeredgecolor="#FF0000")
ax2.set_xlabel("X-axis", fontsize=10)
ax2.set_ylabel("Y-axis", fontsize=10)
ax2.grid(color='green', alpha=1)
ax2.set_title("Plot 2", fontsize=12)

ax3 = fig.add_subplot(223)
ax3.pie(counts, labels=groups, colors=colors)
ax3.set_title("Pie Plot 3", fontsize=12)

ax4 = fig.add_subplot(224, projection='3d')
ax.plot_surface(x1, x2, z, color = "red")
ax4.set_title("3D Plot 4", fontsize=12)
ax4.set_facecolor("#F0F8FF") #background color

plt.savefig("subplot_grid.png")
plt.clf()

#8
styles = ["ggplot", "dark_background", "cyberpunk"]

for s in styles:
    plt.style.use(s)

    fig = plt.figure(figsize=(10, 10))
    fig.suptitle(f"Сетка графиков (стиль: {s})", fontsize=14)

    ax1 = fig.add_subplot(221)
    ax1.plot(array, funcarray, label="f(x)")
    ax1.set_xlabel("X-axis", fontsize=10)
    ax1.set_ylabel("Y-axis", fontsize=10)
    ax1.set_title("Plot 1", fontsize=12)
    ax1.legend()

    ax2 = fig.add_subplot(222)
    ax2.plot(array, funcarray, marker=".", markersize=5,
             color="#0000FF", markerfacecolor="#FF0000", markeredgecolor="#FF0000")
    ax2.set_xlabel("X-axis", fontsize=10)
    ax2.set_ylabel("Y-axis", fontsize=10)
    ax2.grid(color='green', alpha=1)
    ax2.set_title("Plot 2", fontsize=12)

    ax3 = fig.add_subplot(223)
    ax3.pie(counts, labels=groups, colors=colors)
    ax3.set_title("Plot 3", fontsize=12)

    ax4 = fig.add_subplot(224, projection='3d')
    ax.plot_surface(x1, x2, z, color = "red")
    ax4.set_title("Plot 4", fontsize=12)

    plt.savefig(f"subplot_style_{s}.png")
    plt.clf()