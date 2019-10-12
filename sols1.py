# Q1

def bin(n) :
  if n==0 : 
    yield ()
  else :
    for k in range(0,n) :    
      for l in bin(k) :
        for r in bin(n-1-k) :        
          yield (l,r)
          

def depth(t) :
  if not t : return 0
  (l,r) = t
  return 1+max(depth(l),depth(r))

def t1() :
  for t in bin(3) :
    print(t,depth(t))

def average(n) :
  ds = list(map(depth,bin(n)))
  l = len(ds)
  s=sum(ds)
  return s/l

def t2() :
  print(average(8))

# Q2
'''
/\
 /\
  /\
   /\
   etc.

or   
((),((),((),(()...
 
'''
# T(n)=1+T(n-1) => O(N)

# Q3
'''
$3 : 1 for reverse, one for remove

also ok

if more, extra for copy/assign
'''