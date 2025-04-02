import numpy as np
import math
import matplotlib.pyplot as plt

# -------------------------------------------Poisson eqn---------------------------------------------

iter = 10
a=0
b=4
h=1
k=1
nx=int((b-a)/h)
ny=int((b-a)/k)

x=np.linspace(a,b,nx+1)
y=np.linspace(a,b,ny+1)

u = np.zeros([ny+1,nx+1])

def f(x,y):
    return (x*y)**2
def g(x,y):
    return (x+y)

for _ in range(iter):
    for i in range(nx+1):
        for j in range(ny+1):
            u[0,j]=0
            u[nx,j]=f(x[nx],y[j])
            u[i,0]=0
            u[i,ny]=f(x[i],y[ny])
    for i in range(1,nx):
        for j in range(1,ny):
            u[i,j]= (u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1])/4  -(h**2)*(g(x[i],y[j]))/4
print(u)