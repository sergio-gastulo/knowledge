
import numpy as np

e = np.exp(1)
num = 0.05*(e**2-e)**3
dem = 12*0.001

#print(np.sqrt(num/dem)) #20.6 -> n = 21

xx = np.linspace(e,e**2,21+1) #+1 porque python es raro

f = lambda x: np.log(x)**2

dx = (e**2-e)/21

print(
    dx*(sum([2*f(x) for x in xx])-f(xx[0])-f(xx[-1]))/2
    )

