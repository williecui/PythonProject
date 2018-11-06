def newton(f,Df,x0,epsilon,max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8,10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        # print ("------------", n, xn, fxn, epsilon)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xntemp = xn
        xn = xn - fxn*1.0/Dfxn
        # print ("---------------", n, xntemp, xn, fxn, Dfxn, fxn/Dfxn)

    print('Exceeded maximum iterations. No solution found.')
    return None

f = lambda x: x**2 - x - 1
print (f)
Df = lambda x: 2*x - 1
print(newton(f,Df,1,1e-8,10))

# f = lambda x: x**3 - x**2 - 1
# Df = lambda x: 3*x**2 - 2*x
# approx = newton(f,Df,1,1e-10,10)
# print(approx)


# def dx(f, x):
#     return abs(0-f(x))
 
# def newtons_method(f, df, x0, e):
#     delta = dx(f, x0)
#     while delta > e:
#         x0 = x0 - f(x0)/df(x0)
#         delta = dx(f, x0)
#     print 'Root is at: ', x0
#     print 'f(x) at root is: ', f(x0)

# def f(x):
#     return 6*x**5-5*x**4-4*x**3+3*x**2
 
# def df(x):
#     return 30*x**4-20*x**3-12*x**2+6*x
# x0s = [0, .5, 1]
# for x0 in x0s:
#     print(newtons_method(f, df, x0, 1e-5))