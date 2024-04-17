import numpy as np

e = np.exp(1)
num = 0.183*(e**2-e)**5
dem = 180*0.001
print("approximation of n:", (num/dem)**0.25) #6.89 -> n = 7 -> n = 8
n = 8
xx = np.linspace(e,e**2,n+1) #+1 porque python es raro
f = lambda x: np.log(x)**2
dx = (e**2-e)/n
extremos = f(xx[0]) + f(xx[-1])
impares = 4*sum([f(xx[2*i-1]) for i in range(1,1+int(n/2))])
pares = 2*sum([f(xx[2*i]) for i in range(1,int(n/2))])
h = (e**2-e)/n
print("I=", (h/3)*(extremos+impares+pares))