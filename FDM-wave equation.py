import numpy as np
import math
import matplotlib.pyplot as plt

# -------------------------------------------------explicit FDM 1D wave equation---------------------------------------------

iter = 1
x0=0
xn=1
h=0.05
k=0.1
#  decreasing the value of lamb reduces error lamb <= 0.5
time_level = 9
nx=int((xn-x0)/h)
nt=int((xn-x0)/k)
lamb = (k/h)

x=np.linspace(x0,xn,nx+1)
# t=np.linspace(x0,xn,nt+1)
u = np.zeros([time_level+1,nx+1])
def f(x,t):
    return math.sin(math.pi*x)
def g(x):
    return 0



# for _ in range(iter):
for i in range(nx):
    for j in range(time_level+1):
        u[0,i] = f(x[i],0)
        u[j,0] = 0
        u[j,nx] = 0

for i in range(1,nx):
    u[1,i] = (2*u[0,i] - ( - 2*k*g(x[i])) + (lamb**2)*(u[0,i+1] -2*u[0,i] + u[0,i-1]))/2
# u[1,:] = u[0,:]
for j in range(1,time_level):    
    for i in range(1,nx):
        u[j+1,i] = 2*u[j,i] - u[j-1,i] + (lamb**2)*(u[j,i+1] -2*u[j,i] + u[j,i-1])
print(u)

plt.figure(figsize=(10, 6))
for j in range(time_level + 1):
    plt.plot(x, u[j, :], label=f"Time Level {j}", marker ='o')

plt.title("Wave Propagation Solution")
plt.xlabel("x")
plt.ylabel("u(x, t)")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.show()