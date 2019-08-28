# lists

a=list()
a.append(1)
a.append(2)

print('a:',a)

b=[3,4,5]

c=a+b

print('c:',c)

# sets

xs=set()

xs.add(1)
xs.add(2)

ys={3,4,5}

print('xs',xs)
print('ys',ys)

def union(xs,y) :
  def f() :
    for x in xs :
      yield x
    for y in ys :
      yield y
  return set(f())

print('union:',union(xs,ys))


