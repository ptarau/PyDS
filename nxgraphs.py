import networkx as nx
import graphviz as gv
import numpy as np

class digraph(nx.DiGraph) :

  def random(self,n_nodes,n_edges):
    er = nx.dense_gnm_random_graph(n_nodes, n_nodes)
    for e in er.edges() :
      f,t=e
      self.add_edge(f,t)

    er = nx.dense_gnm_random_graph(n_nodes, n_nodes)
    for e in er.edges() :
      f,t=e
      self.add_edge(f+n_edges,t+n_edges)
    if 0 not in self.nodes(): self.add_edge(0, 1)

    return self

  def rand(self):
    return self.random(12,12)

  def ranDAG(self,n_nodes,n_edges):
    er = nx.dense_gnm_random_graph(n_nodes, n_nodes)
    for e in er.edges() :
      f,t=e
      self.add_edge(f,t)
    if 0 not in self.nodes(): self.add_edge(0, 1)

    return self

  # assumes nodes in range(0,number_of_nodes)
  def to_matrix(self):
    n=max(self.nodes())+1
    m=np.zeros((n,n),dtype=int)
    for f,t in self.edges() :
      m[f,t]=1
    return m

  # turns into a directed graph
  # that mimics an undirected one
  def as_undir(self):
    es=list(self.edges())
    for f,t in es :
      if f not in self[t] :
        self.add_edge(t,f)
    return self

  def connected_components(self):
    g=self.to_undirected()
    css=list()
    ns=set(g.nodes())
    while ns :
       n=ns.pop()
       cs=set(df_nodes(g,n))
       css.append(cs)
       ns -= cs
    return css

  def show(self):
    return show(self)

# depth first traversal
def df_nodes(g,source):
  visited=set()
  def visit(node) :
    if node in visited : return
    visited.add(node)
    yield node
    for child in  g[node] :
      for n in visit(child) :
        yield n
  for n in visit(source) :
    yield n

# iterative deepening traversal
def id_nodes(g,source,max_depth=None):
  if not max_depth :
    max_depth=g.number_of_nodes()
  seen=set()
  def visit(node,fuel) :
    #print('trace',visited)
    if node in visited or not fuel : return
    visited.add(node)
    if node not in seen : yield node
    seen.add(node)
    for child in  g[node] :
      for n in visit(child,fuel-1) :
        yield n
  for fuel in range(0,max_depth+1) :
    visited=set()
    for n in visit(source,fuel) :
      yield n

def search(g,algo,source,target) :
  for n in algo(g,source) :
    if n == target :
      return ('found',target)
  return 'not found'


# TODO adapt this to return the path to target

# see https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
def topsort(g) :
  topsorted=[]
  perm=set()
  temp=set()

  def visit(n) :
    #print(n)
    if n in perm : return
    if n in temp : raise BaseException("not a DAG")
    temp.add(n)
    for m in g[n] : visit(m)
    temp.remove(n)
    perm.add(n)
    topsorted.append(n)

  try :
    for n in g.nodes() :
      if n not in perm: visit(n)
    topsorted.reverse()
    return topsorted
  except :
    return None

# TODO - finish - add backtracking
def gcolor(g,cs) :
   ns=dict()
   for s,t in g.edges() :
     if not ns.get(s) :
       for c in cs :
         ns[s]=c
         if not ns.get(t) :
           for d in cs :
             if d!=c :
               ns[t]=d
   return ns



def show(g):
  dot = gv.Digraph()
  for e in g.edges():
    f, t = e
    dot.edge(str(f), str(t), label='')
    #print(dot.source)
  dot.render('graph.gv', view=True)
  return g

def t1() :
  # edges
  es = [(1,2),(2,3),(1,3),(3,4),(4,5),(5,6),(4,6),(2,5),(1,6)]
  G=digraph()
  G.add_edges_from(es)
  G.show()

def t2() :
    digraph().rand().show()

def t3() :
  g=digraph().rand().show()
  ns=nx.dfs_preorder_nodes(g,source=0)
  print('networx',list(ns))
  print('ours   ',list(df_nodes(g,0)))

def t4() :
  g=digraph().rand().show()
  es=nx.bfs_edges(g, 0)
  ns=[0]+list(map(lambda b:b[1], es))
  print('networx',list(ns))
  print('ours   ',list(id_nodes(g,0)))

def t5() :
  g=digraph().rand() #.show()
  m=g.to_matrix()
  print(m)
  g_again=digraph(m)
  g_again.show()
  mm=g_again.to_matrix()
  print(mm)

def t6() :
  g=digraph([('one',42),(42,'one'),
             ('one','two'),('two','two'),('two',42)])
  g.show()

# testing for a target
def t7() :
  g=digraph().rand().show()
  print(search(g,id_nodes,0,10))

def t8() :
  g = digraph().random(10,10).show()
  #u=dir2undir(g)
  u=g.to_undirected()
  cs=nx.connected_components(u)
  print(list(cs))
  ccs=g.connected_components()
  print(ccs)


def t9() :
  for _ in range(10) :
    g=digraph().random(10,10) # .show()
    t=topsort(g)
    if t:
      g.show()
      tt=list(nx.topological_sort(g))
      print(tt)
      print(t)
      break;

#t0()
#t1()
#t2()
#t3()
#t4()
#t5()
#t7()
#t8()
t9()


