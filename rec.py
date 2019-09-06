from  collections import *

# todo

# reverse a list, recursively

def nrev(xs) :
  if xs==[] : return xs
  head=xs[0]
  tail=xs[1:]
  revtail=nrev(tail)
  return revtail + [head]

# reverse a list using a while loop

# queue with two stacks

# queues with lists

xs = list(range(10))

def qadd1(qs,x) :
  return qs.append(x)

def qremove1(qs) :
  x=qs[0]
  qs=qs[1:]
  return (x,qs)

def qadd (xsys, x) :
  xs,ys = xsys
  ys.append(x)
  return (xs,ys)

def qremove(xsys) :
  xs, ys = xsys
  if xs == [] :
    xs=list(reversed(ys))
    ys=[]
    x=xs.pop()
    return (x, (xs,ys))

'''
/usr/local/bin/python3.7 -i /Users/tarau/Desktop/sit/PyDS/rec.py
>>> q=([],[])
>>> qadd(q,1)
([], [1])
>>> qadd(q,2)
([], [1, 2])
>>> qadd(q,3)
([], [1, 2, 3])
>>> x,q=qremove(q)
>>> x
1
>>> q
([3, 2], [])
>>> 


'''

# deque

'''
Deque objects support the following methods:

append(x)
Add x to the right side of the deque.

appendleft(x)
Add x to the left side of the deque.

clear()
Remove all elements from the deque leaving it with length 0.

pop()
Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

popleft()
Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

remove(value)
Remove the first occurrence of value. If not found, raises a ValueError.

'''
