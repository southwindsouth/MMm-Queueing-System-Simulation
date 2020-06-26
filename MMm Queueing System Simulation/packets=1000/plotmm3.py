import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Major ticks every 10, minor ticks every 5 for x axis
x_major_ticks = np.arange(0, 101, 10)
x_minor_ticks = np.arange(0, 101, 5)

# Major ticks every 0.1, minor ticks every 0.1 for y axis
y_major_ticks = np.arange(0, 1.1, 0.2)
y_minor_ticks = np.arange(0, 1.1, 0.1)

ax.set_xticks(x_major_ticks)
ax.set_xticks(x_minor_ticks, minor=True)
ax.set_yticks(y_major_ticks)
ax.set_yticks(y_minor_ticks, minor=True)

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

# calculate and plot analytical results
import math
m=5
x1 = np.arange(1, 100)
rou=x1/100
n=0
miu=100/m
 
xigema=np.zeros(99) 
  
for n in range(m):
    xigema = xigema+((m*rou)**n)/math.factorial(n)


xigema_right=(1/(1-rou))*((m*rou)**m)/math.factorial(m)

p0=1/(xigema+xigema_right) 

 
pm_plus=p0* ((m*rou)**m)/math.factorial(m)/(1-rou)


y1=(pm_plus*(rou/(1-rou)/x1))+1/miu

plt.plot(x1, y1,'b-', label="Analysis", linewidth=1)

# load and plot simulation results
x2, y2 = np.loadtxt('mm3.out', delimiter='\t', unpack=True)
plt.plot(x2, y2, 'rx', label="Simulation")

# add labels, legend, and title
plt.xlabel(r'$\lambda$ [pkts/s]')
plt.ylabel(r'$E[T]$ [s]')
plt.legend()
plt.title(r'M/M/5 ($\mu=20$ [pkts/s])')

plt.savefig('plot_mm5.pdf')
plt.show()