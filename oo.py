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
    for t in list(reversed(self.xs)) + self.ys :
      buf.append(str(t))
      buf.append(' ')
    return "".join(buf)

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

t1()
