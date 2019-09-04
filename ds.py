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


# files: seen as yet another generator
# where the read or write operation is
# what we iterate on

# turns a string into given file
def string2file(fname,text) :
  with open(fname,'w') as f :
    f.write(text)

# turns content of file into a string
def file2string(fname) :
  with open(fname,'r') as f :
    s = f.read()
    return s

def test1() :
  s=file2string('ds.py')
  ls=s.split('\n')
  for l in ls :
    print(l)

def test2() :
  xs = [2,3874,0,2,1,2098,1,0,77]
  return list(set(sorted(xs)))

def qsort(xs) :
  if xs==[] : return xs
  x=xs[0]
  ys=xs[1:]
  ls=[y for y in ys if y<=x]
  bs=[y for y in ys if y>x]
  return qsort(ls) + [x] + qsort(bs)

# list and set comprehensions

lc1=[x for x in range(9) if x < 5]

def cart_prod(xs,ys) :
  return [(x,y) for x in xs for y in ys]

def lc2() :
  return cart_prod([1,2,3],['a','b'])

def cart_prod1(xs,ys) :
  for x in xs :
    for y in ys:
      yield (x,y)

def lc3() :
  return cart_prod1([1, 2, 3], ['a', 'b'])
















