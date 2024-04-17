import numpy as np
from scipy.optimize import minimize_scalar
import sympy as sp
import time

def simpson(f: callable, E: float, inf_limit: float, sup_limit: float)-> float:
    """
        This function integrates over an interval with the simpson rule for a given error E
    """
    
    """
        The following block finds the maxima of |f^(4)(x)| over the interval inf_limit, sup_limit
        it is not optimal at all, but it works
    """
    #Simbolic notation with x
    x = sp.Symbol('x')
    #from callable to symbolic
    symbolic_f = f(x)
    #getting the fourth derivative
    diff_f_symbolic = sp.diff(symbolic_f, x, 4)
    #from symbolic to callable
    diff_f = sp.lambdify(x, diff_f_symbolic, 'numpy')
    #the function to be maximized
    to_max = lambda t: -np.abs(diff_f(t))
    #the actual maximized value
    max = -minimize_scalar(to_max, bounds = (inf_limit,sup_limit)).fun

    """
        Getting n
    """
    #getting n as a result from the error formula
    n = int(((max/(E*180))*(sup_limit-inf_limit)**5)**0.25)+1
    #n has to be even
    if n%2 != 0: n=n+1

    """
        Making the requested sumation
    """
    #the set of points where the discretization is made
    xx = np.linspace(inf_limit,sup_limit,n+1)
    #the step
    dx = (sup_limit-inf_limit)/n
    #extreme values
    extremos = f(xx[0]) + f(xx[-1])
    #even identation values
    impares = 4*sum([f(xx[2*i-1]) for i in range(1,1+int(n/2))])
    #odd identation values
    pares = 2*sum([f(xx[2*i]) for i in range(1,int(n/2))])

    #the sum of the discretized values
    return (dx/3)*(extremos+impares+pares)


def trapezio(f: callable, E: float, inf_limit: float, sup_limit: float)-> float:

    """
        This function integrates over an interval with the trapezoidal rule for a given error E
    """
    
    """
        The following block finds the maxima of |f^(2)(x)| over the interval inf_limit, sup_limit
        it is not optimal at all, but it works
    """
    #Simbolic notation with x
    x = sp.Symbol('x')
    #from callable to symbolic
    symbolic_f = f(x)
    #getting the second derivative
    diff_f_symbolic = sp.diff(symbolic_f, x, 2)
    #from symbolic to callable
    diff_f = sp.lambdify(x, diff_f_symbolic, 'numpy')
    #the function to be maximized
    to_max = lambda t: -np.abs(diff_f(t))
    #the actual maximized value
    max = -minimize_scalar(to_max, bounds = (inf_limit,sup_limit)).fun

    """
        Getting n
    """
    #getting n as a result from the error formula
    n = int(((max/(E*12))*(sup_limit-inf_limit)**3)**0.5)+1

    """
        Making the requested sumation
    """
    #the set of points where the discretization is made
    xx = np.linspace(inf_limit,sup_limit,n+1)
    #the step
    dx = (sup_limit-inf_limit)/n
    #extreme values
    extremos = f(xx[0]) + f(xx[-1])
    #values in the middle
    medios = 2*sum([f(x) for x in xx[1:-1]])

    #the sum of the discretized values
    return (dx/2)*(extremos+medios)



if __name__ == '__main__':
    #testing function, it has to be written on sp library
    f = lambda s: (sp.log(s))**2
    #precision of the integration
    E = 0.001
    #inf limit
    inf = np.e
    #sup limit
    sup = np.e**2

    #the integral from e to e**2 of f(x) dx
    start_simpson = time.time()
    print("Integration with simpson rule:", simpson(f,E,inf,sup))
    end_simpson = time.time()
    print("time taken on simpson integration: ", -start_simpson+end_simpson, "seconds")
    
    start_trapezoidal = time.time()
    print("Integration with trapezoidal rule:", trapezio(f,E,inf,sup))
    end_trapezoidal = time.time()
    print("time taken on trapezoidal integration: ", -start_trapezoidal+end_trapezoidal, "seconds")

    """
        As espected, the time for the simpson integration is higher since takind the fourth derivative 
        is not optimal. These functions have been developed for eductational purpouses. They are not intended
        to be optimal, it was designed for numerical calculations only. 
    """

