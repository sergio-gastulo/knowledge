import numpy as np
from scipy.optimize import minimize_scalar
import sympy as sp

def simpson(f: callable, E: float, inf_limit: float, sup_limit: float)-> float:

    """
        This function integrates over an interval for a given error E
    """
    x = sp.Symbol('x')
    symbolic_f = f(x)
    diff_f_symbolic = sp.diff(symbolic_f, x, 4)
    diff_f = sp.lambdify(x, diff_f_symbolic, 'numpy')
    to_max = lambda t: -np.abs(diff_f(t))

    max = -minimize_scalar(to_max, bounds = (inf_limit,sup_limit)).fun

    n = int(((max/(E*180))*(sup_limit-inf_limit)**5)**0.25)+1
    if n%2 != 0 : n=n+1

    xx = np.linspace(inf_limit,sup_limit,n+1)

    dx = (sup_limit-inf_limit)/n

    extremos = f(xx[0]) + f(xx[-1])
    impares = 4*sum([f(xx[2*i-1]) for i in range(1,1+int(n/2))])
    pares = 2*sum([f(xx[2*i]) for i in range(1,int(n/2))])

    return (dx/3)*(extremos+impares+pares)


if __name__ == '__main__':
    f = lambda s: (sp.log(s))**2
    E = 0.001
    inf = np.e
    sup = np.e**2
    print(simpson(f,E,inf,sup))