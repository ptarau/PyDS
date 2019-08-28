# lists

a=list()
a.append(1)
a.append(2)

print('a:',a)

b=[3,4,5,6,7]

print(b[0])
c=a+b

print('c:',c)

# tuples

t=(1,2,3)
tt=t+t

# sets

xs=set()

xs.add(1)
xs.add(2)
xs.add(3)
xs.add(4)

ys={3,4,5}

print('xs',xs)
print('ys',ys)

def union(xs,ys) :
  def f() :
    for x in xs :
      yield x
    for y in ys :
      yield y
  return set(f())

def intersect(xs,ys) :
  def f() :
    for x in xs :
      if x in ys :
        yield x
  return set(f())

zs = set(range(2,7))

print('union:',union(xs,ys))

print('intersect:',intersect(xs,zs))

# dicts

d=dict()


key=('good','bad')

d['hello']='bye'
d[42]='meaning of life'
d[key]='maybe'

dd={1:'one',2:'two'}


