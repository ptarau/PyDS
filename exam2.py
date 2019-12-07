from  nxgraphs import *

# Q1

def q1() :
  print('\nQ1','nlog(7n)/log(7) -> O(nlog(n))')
# Q2

def revgraph(g) :
  r = digraph()
  for n in g.nodes() :
    r.add_node(n)
  for f,t in g.edges() :
    r.add_edge(t,f)
  return r

def q2() :
  print('\nQ2')
  g = digraph().random(5, 30)
  print(list(g.edges()))
  r=revgraph(g)
  print(list(r.edges()))

# Q3
def evens(g,source) :
  return [n for n in id_nodes(g,source) if n == 2 * (n // 2) ]

def q3() :
  print('\nQ3')
  g = digraph().random(5, 30)
  print('NODES',list(g.nodes()))
  print('EDGES', list(g.edges()))
  print('BFS_EDGES',list(nx.bfs_edges(g,0)))
  print('ID_NODES',list(id_nodes(g, 0)))
  print('EVENS',evens(g,0))

# Q4
def topsort_edges(g) :
  lg=nx.line_graph(g)
  return  topsort(lg)

def q4():
  print('\nQ4')
  g=None
  ts=None
  while(not ts) :
    g = digraph().random(5, 10)
    ts=topsort(g)
  print('EDGES:', list(g.edges()))
  print('NX TOPSORTED NODES', list(nx.topological_sort(g)))
  print('TOPSORTED NODES',ts)
  print('TOPSORTED LINE-GRAPH EDGES',list(topsort_edges(g)))

# Q5

# binary tree of size n
def bin(n) :
  if n==0 :
    yield ()
  else :
    for k in range(0,n) :
      for l in bin(k) :
        for r in bin(n-1-k) :
          yield (l,r)

def colbin(n) :
  if n==0 :
    yield 0
    yield 1
  else :
    for k in range(0,n) :
      for l in colbin(k) :
        for r in colbin(n-1-k) :
          yield (l,r)

def count(f,n) :
  k=0
  for t in f(n) :
    k+=1
  return k

def q5() :
  print('\nQ5')
  for n in range(6) :
    b=count(bin,n)
    c=count(colbin,n)
    print(n,b,c,c//b)
  print('Answer : C(n)/T(n)= 2^(n+1) because \
a tree of size n has n+1 leaves and \
each can be 0 or 1')
'''
0 1 2 2
1 1 4 4
2 2 16 8
3 5 80 16
4 14 448 32
5 42 2688 64

Answer : C(n)/T(n)= 2^(n+1) because
a tree of size n has n+1 leaves and
each can be 0 or 1

'''

q1()
q2()
q3()
q4()
q5()

