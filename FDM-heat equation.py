import numpy as np
import math
import matplotlib.pyplot as plt
# Run the code for solution
# ------------------------------------explicit & Crank-Nicolson FDM for 1D heat eqn--------------------------
def explicit(x0,xn,h,k,time_level):
    nx=int((xn-x0)/h)
    nt=int((xn-x0)/k)
    lamb = k/h**2

    x = np.linspace(x0,xn,nx+1)
    # t=np.linspace(x0,xn,nt+1)
    u = np.zeros([time_level+1,nx+1])
    def f(x,t):
        return math.sin(math.pi*x)

    # for _ in range(iter):
    for i in range(nx):
        for j in range(time_level+1):
            u[0,i] = f(x[i],0)
            u[j,0] = 0
            u[j,nx] = 0
    for j in range(time_level):    
        for i in range(1,nx):
            u[j+1,i] = lamb*u[j,i+1] + (1-2*lamb)*u[j,i] + lamb*u[j,i-1]

    plt.figure(figsize=(8, 6))
    plt.plot(x, u[time_level, :], 'o-', label="Numerical Solution")
    plt.xlabel("x")
    plt.ylabel("u(x, t)")
    plt.title(f"Comparison at time t = {k * time_level}")
    plt.legend()
    plt.grid(True)
    plt.show()
    return print(u)
def crank_nicolson(x0,xn,h,k,time_level):
    nx = int((xn-x0)/h)
    nt = int((xn-x0)/k)
    lamb = k/h**2

    x= np.linspace(x0,xn,nx+1)
    y= np.linspace(x0,xn,nx+1)
    u = np.zeros([nx-1,1])
    u_new = np.zeros([nx-1,1])
    A= np.zeros([nx-1,nx-1])
    B = np.zeros([nx-1,nx-1])
    sol = np.zeros([time_level+1,nx+1])

    def f(x):
        return math.sin(math.pi*x)
    for i in range(nx+1):
        sol[0][i] = f(x[i])

    for k in range(nx-1):
        A[k][k] = 1+lamb
        B[k][k] = 1-lamb
    for k in range(nx-2):
        A[k][k+1] = -lamb/2
        A[k+1][k] = -lamb/2
        B[k][k+1] = lamb/2
        B[k+1][k] = lamb/2

    for i in range(1, nx):
        u[i - 1][0] = f(x[i])

    for j in range(1, time_level + 1):
        z = np.dot(B, u)
        p = np.linalg.solve(A, z)
        sol[j, 1:nx] = p[:, 0]
        u = p

    fig = plt.figure(figsize=(10, 6))
    for j in range(time_level + 1):
        plt.plot(x, sol[j, :], label=f'Time level {j}')
    # ax = fig.add_subplot(111,projection = '3d')
    # x,y = np.meshgrid(x,y)
    # ax.plot_surface(x,y,sol,cmap='hot')
    # plt.show()


    plt.xlabel('x')
    plt.ylabel('u(x,t)')
    plt.title('Crank-Nicolson Solution for 1D Heat Equation')
    plt.legend()
    plt.grid(True)
    plt.show()
    return print(sol)

# print(f'EXPLICIT\n:{explicit(int(0),int(1),float(1/3),float(1/36),int(2))}')
print(f'CRANK NICOLSON\n:{crank_nicolson(int(0),int(1),float(1/3),float(1/36),int(2))}')
