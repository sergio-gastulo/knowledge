# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:51:29 2024

@author: sgast
"""

import numpy as np
import matplotlib.pyplot as plt

#%%

"""
    This function solves a problem of the form 
    
    dY/dx = F(x,Y)
    0 \leq x \leq upperbound
    Y(0) = y0

"""

def runge_kutta_4(
        F: callable, 
        upper_bound: float, 
        zero_condition: np.array, 
        n_points: int,
        dim:int) -> np.array:
    
    solution = np.zeros((n_points, dim), float)
    interval = np.linspace(0, upper_bound, n_points)
    step = (upper_bound)/n_points
    solution[0] = zero_condition
    
    for i,t in enumerate(interval):
        if i < len(interval)-1:
            K1 = F(t,solution[i])
            K2 = F(t+step/2,solution[i]+K1*step/2)
            K3 = F(t+step/2,solution[i]+K2*step/2)
            K4 = F(t+step,solution[i]+step*K3)
            solution[i+1] = solution[i] + (step/6)*(K1+2*K2+2*K3+K4)
    
    return solution

#%%

"""

    Testing Runge-Kutta 4 with the ODE:
    x' = -y
    y' = x
    (x,y)(0) = (1,0)
    0 \leq t \leq pi/2
    
    with exact solution:
    x,y = cos(t),sin(t)

"""

f = lambda t,x : np.array([-x[1],x[0]])
b = np.pi/2
x0 = np.array([1,0])
n = 100

xx = np.linspace(0,b,n)
A = runge_kutta_4(
    F=f, 
    upper_bound=b, 
    zero_condition=x0, 
    n_points=n,
    dim=2)

plt.scatter(xx, 
            A[:,0],
            s = 2.5, 
            label = 'Aprox of $x = \cos(t)$')
plt.plot(
    xx,
    np.cos(xx), 
    label = 'Solution $x = \cos(t)$')

plt.scatter(xx, 
            A[:,1],
            s = 2.5, 
            label = 'Aprox of $y = \sin(t)$')

plt.plot(
    xx,
    np.sin(xx), 
    label = 'Solution $y = \sin(t)$')

plt.xlabel('$t$ range')
plt.title('Approx solution vs real solution')
plt.legend()
plt.show()

del(f,b,x0,n,xx,A)

#%%

"""
    Shooting linear method
    the following functions returns a discretization of the ODE
    y'' = p(t) y' + q(t) y + r(t)
    with 
        y(0) = alpha,
        y(b) = beta
    
"""

def shooting_method(
        p: callable,
        q: callable,
        r: callable,
        upper_bound: float,
        alpha: float,
        beta: float,
        n_points: int)->np.array:
    
    F = lambda x,z : np.array([
        z[1],
        q(x)*z[0]+p(x)*z[1]+r(x),
        z[3],
        q(x)*z[2]+p(x)*z[3]+r(x)
        ])
    
    z0 = np.array([alpha,0,0,1])
    
    pre_sol = runge_kutta_4(
        F = F,
        upper_bound = upper_bound, 
        zero_condition = z0, 
        n_points = n_points, 
        dim = 4)
    
    solution = pre_sol[:,0] + ((beta-pre_sol[-1,0])/pre_sol[-1,2])*pre_sol[:,2] 

    return(solution)


#%%

"""
    We will 
"""

p = lambda x: 0
q = lambda x: -1
r = lambda x: 0
b = np.pi/2
alpha = 0
beta = 1
n = 20
U = shooting_method(p, q, r, b, alpha, beta, n)
h = b/n
t = np.linspace(0,b,n)
plt.scatter(t,U, c = 'red')

#VERIFICANDO CON SOLUCIÓN EXACTA:
g = lambda x: np.sin(x)
X = np.linspace(0,b,30)
plt.plot(X,g(X), c= 'blue')
plt.legend(["Discretización de y","Solución exacta y = f(x) = sinh(x)"])


del(p,q,r,alpha, b,beta, U,h,t,g,X,n)

#%%







