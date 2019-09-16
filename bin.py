import graphvizTree as gt


# binary tree of size n
def bin(n) :
  if n==0 : 
    yield ()
  else :
    for k in range(0,n) :    
      for l in bin(k) :
        for r in bin(n-1-k) :        
          yield (l,r)

def countFor(f,n) :
  for i in range(n) :
    count = 0
    for t in f(i) : 
      count+=1
    yield count

def countsFor(mes,f,n) :
  print(mes)
  print([c for c in countFor(f,n)])
  print("")

def showFor(mes,f,n) :
  print(mes)
  for t in f(n) :
    print(t)
  print("")
 
showFor('Binary trees',bin,5)

countsFor('Binary trees',bin,12)

def test() :
  for n in range(6) :
    print(n,list(bin(n)))          
