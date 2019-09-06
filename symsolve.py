from sympy import *

def fibo(n) :
  if n<2 :
    return 1
  else :
    return fibo(n-2) + fibo(n-1)

def fiborec() :
  y = Function('y')
  n = symbols('n',integer=True)
  f = y(n)-y(n-1)-y(n-2)
  r=rsolve(f,y(n),{y(0):0, y(1):1})
  print(r)
