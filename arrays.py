# dynamic Python arraylist  emulated with built-in lists

class array :
  def __init__(self):
    self.n = 0  # Count actual elements (Default is 0)
    self.A = []

  def __len__(self):
    return self.n

  def __getitem__(self, k):
    if not 0 <= k < self.n: return None
    return self.A[k]

  def empty(self) :
    return self.n==0
  
  def append(self, x):
    if self.n==0 :
      self.A = [x]
      self.n = 1
      return
    l=len(self.A)
    if self.n == l:
      self._resize(2 * l)
    self.A[self.n] = x
    self.n += 1

  def pop(self):
    self.n -= 1
    if self.n == 0:
      x=self.A[0]
      self.A = []
      return x

    x=self.A[self.n]
    self.A[self.n]=None
    l = len(self.A)
    #print('-------',self.n)
    if self.n==l//4 :
      self._resize(l//2)
    return x

  def _resize(self, size):
    B = [None]*size
    for k in range(self.n):
      B[k] = self.A[k]
    self.A = B

  def __str__(self) :
    return str(self.A)


# random tests

from random import randint

def ranops(n) :
  a=array()

  for i in range(n) :
    dice = randint(0,2)
    if dice>0 : a.append(i)
    elif not a.empty() : a.pop()
  return a

def atest(n) :
  return ranops(n)

# benchmarks using random tests

from timeit import timeit as tm

def abm(n) :
  print('benchmark for',n,'array operations')
  print(tm(lambda : ranops(n),number=1))

# short hands for tests

def t1() :
  a=array()
  print(a.empty())
  a.append(1)
  print(a.empty())
  a.append(2)
  print(a.n,a)
  x=a.pop()
  print(a,x)
  a.append(3)
  a.append(4)
  print(a)
  y=a.pop()
  print(a,y)
  z=a.pop()
  print(a,z)

def t2() :
  a=atest(42)
  print(len(a),a)

def t3() :
  abm(1000000)
