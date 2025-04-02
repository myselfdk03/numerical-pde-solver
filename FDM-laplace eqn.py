import numpy as np
import math
import matplotlib.pyplot as plt

# -----------------------------------------------Laplace eqn--------------------------------------------------

iter = 10
a=0
b=1
h=0.25
k=0.25
initial = 10
final =20

nx=int((b-a)/h)
ny=int((b-a)/k)
x=np.arange(a,b,h)
y=np.arange(a,b,k)

u = np.zeros([ny+1,nx+1])

for i in range(nx+1):
        for j in range(ny):
            u[0,j]=initial
            u[nx,j]=final
            u[i,0]=initial
            u[i,ny]=final

for _ in range(iter):
    for i in range(1,nx):
        for j in range(1,ny):
            u[i,j]= (u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1])/4

print(u)

