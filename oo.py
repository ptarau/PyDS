class BinTree :
  def __init__(self,x,y) :
    self.x=x
    self.y=y

  def __str__(self) :
    def mystr(t) :
      if not mystr(t) :
        yield ('*')
      else : # t is a branch
        if t.x :
          print('L')
          yield ('<')
          for s in mystr(t.x) : yield s
          yield (',')
        else :
          yield '*'
        if t.y:
          print('R')
          for s in mystr(t.y): yield s
          yield ('>')
        else:
          yield '*'
    return "".join(mystr(self))


def b1() :
  x=BinTree(None,None)
  y=BinTree(x,x)
  z=BinTree(x,y)
  #print(z)
  return z



class queue(object) :
  def __init__(self) :
    self.xs=[]
    self.ys=[]

  def add(self,x) :
    self.ys.append(x)

  def remove(self) :
    if self.xs == [] :
      self.ys.reverse()
      self.xs=self.ys
      self.ys=[]
    return self.xs.pop()

  def empty(self) :
    return self.xs == [] and self.ys==[]

  def __str__(self):
    buf=['queue: ']
    for t in reversed(self.xs):
      buf.append(str(t))
      buf.append(' ')
    buf.append('| ')
    for t in self.ys:
      buf.append(str(t))
      buf.append(' ')
    return "".join(buf)

# random tests

from random import randint

def ranops(n) :
  q=queue()

  for i in range(n) :
    dice = randint(0,2)
    if dice>0 : q.add(i)
    elif not q.empty() : q.remove()
  return q

def qtest(n) :
  return str(ranops(n))

# benchmarks using random tests

from timeit import timeit as tm

def qbm(n) :
  print('benchmark for',n,'queue operations')
  print(tm(lambda : ranops(n),number=1))

# short hands for tests

def t1() :
  q=queue()
  print(q.empty())
  q.add(1)
  print(q.empty())
  q.add(2)
  print(q)
  x=q.remove()
  print(x)
  q.add(3)
  q.add(4)
  print(q)
  y=q.remove()
  print(y)
  print(q)
  z=q.remove()
  print(z)
  print(q)

def t2() :
  print(qtest(42))

def t3() :
  qbm(1000000)
