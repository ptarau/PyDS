import graphvizTree as gt
import time

# binary tree of size n
def bin(n) :
  if n==0 : 
    yield ()
  else :
    for k in range(0,n) :    
      for l in bin(k) :
        for r in bin(n-1-k) :        
          yield (l,r)

# rose tree (multi-way tree) of size n
def rose(n):
  if n == 0:
    yield []
  else:
    for k in range(0, n):
      for l in rose(k):
        for r in rose(n - 1 - k):
          yield [l] + r
          
          
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
 
def picsFor(mes,f,n) :
  print(mes)
  for t in f(n) :
    print(t)
    gt.showSimple(t)
    time.sleep(3)
    print("")
    
def test() :
  for n in range(6) :
    print(n,list(bin(n)))  



def go() :
  showFor('Binary trees',bin,3)
  showFor('Rose trees', rose, 3)

  countsFor('Binary trees',bin,12)
  countsFor('Rose trees', rose, 12)

  picsFor('Binary trees',bin,3)
  picsFor('Rose trees', rose, 4)
  
