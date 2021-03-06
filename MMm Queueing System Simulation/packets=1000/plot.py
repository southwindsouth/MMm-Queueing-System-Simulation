import numpy as np
import matplotlib.pyplot as plt
import math
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Major ticks every  
# 
# 
# 
#  10, minor ticks every 5 for x axis
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



plt.xlim(0, 10)
plt.ylim(0, 0.06)

# calculate and plot analytical results
x1 = np.arange(1, 100)
y1 = 1/(100 - x1)
plt.plot(x1, y1,'y-', label="Analysis_mm1", linewidth=1)







m=2
x1 = np.arange(1, 100)
rou=x1/100
n=0
miu=100/m
xigema=np.empty(99) 


# for n in range(m):
#     xigema = ((m*rou)**n)/math.factorial(n)

# xigema_right=(1/(1-rou))* ((m*rou)**m)/math.factorial(m)
# p0=1/(xigema+xigema_right)  
# pm_plus=p0* ((m*rou)**m)/math.factorial(m)/(1-rou)
# p1=pm_plus*rou/(1-rou)/x1+1/miu
# plt.plot(x1, p1,'b-', label="Analysis_mm2", linewidth=1)



m=5
for n in range(m):
    xigema = ((m*rou)**n)/math.factorial(n)

xigema_right=(1/(1-rou))*((m*rou)**m)/math.factorial(m)
p0=1/(xigema+xigema_right) 
pm_plus=p0* ((m*rou)**m)/math.factorial(m)/(1-rou)
k1=pm_plus*rou/(1-rou)/x1+1/miu
plt.plot(x1, k1,'r-', label="Analysis_mm5", linewidth=1)


# add labels, legend, and title
plt.xlabel(r'$\lambda$ [pkts/s]')
plt.ylabel(r'$E[T]$ [s]')
plt.legend()
plt.title(r'Analysis')


plt.savefig('plot_analysis.pdf')
plt.show()














# load and plot simulation results
x2, y2 = np.loadtxt('mm1.out', delimiter='\t', unpack=True)
plt.plot(x2, y2, 'r.', label="Simulation_mm1")

x3, y3 = np.loadtxt('mm2.out', delimiter='\t', unpack=True)
plt.plot(x3, y3, 'g.', label="Simulation_mm2")

x4, y4 = np.loadtxt('mm3.out', delimiter='\t', unpack=True)
plt.plot(x4, y4, 'b.', label="Simulation_mm5")

# add labels, legend, and title
plt.xlabel(r'$\lambda$ [pkts/s]')
plt.ylabel(r'$E[T]$ [s]')
plt.legend()
plt.title(r'Simulation')

plt.savefig('plot_simulation.pdf')
plt.show()