import networkx as nx
import graphviz as gv
import numpy as np
import copy
# add a few methods to nx graphs
class digraph(nx.DiGraph) :
  # customized random graph generator
  def random(self,n_nodes,n_edges):
    er = nx.gnm_random_graph(n_nodes, n_nodes,directed=True)
    for e in er.edges() :
      f,t=e
      self.add_edge(f,t)

    # ensure more than one "island"
    er = nx.dense_gnm_random_graph(n_nodes, n_nodes)
    for e in er.edges() :
      f,t=e
      self.add_edge(f+n_nodes,t+n_nodes)
    if 0 not in self.nodes(): self.add_edge(0, 1)

    return self

  # small random graph
  def rand(self):
    return self.random(12,12)

  # random directed  graph  - TODO - acyclic
  def ranDAG(self,n_nodes,n_edges):
    er = nx.dense_gnm_random_graph(n_nodes, n_nodes)
    for e in er.edges() :
      f,t=e
      self.add_edge(f,t)
    if 0 not in self.nodes(): self.add_edge(0, 1)

    return self

  # turns a directed graph into a 0,1 matrix
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

  # returns a list of connected components
  def connected_components(self):
    g=self.to_undirected()
    css=list()
    ns=set(g.nodes())
    while ns :
       n=ns.pop() # remove n from set
       cs=set(df_nodes(g,n)) # island reacheable from n
       css.append(cs) # add island
       ns -= cs # all nodes not on the island
    return css

  # networkx based pagerank
  def pagerank(self):
    return nx.pagerank(self)

  # pagerank using the weights of the pagerank of the line-graph
  def meta_rank(self):
    c=copy.deepcopy(self)
    pr = c.pagerank()
    print('PR', pr,'\n')

    lg=self.to_line_graph()
    #show(lg,fname='meta.gv')
    lpr=nx.pagerank(lg)
    print('LR', lpr, '\n')
    for k in list(lpr) :
      r=lpr[k]
      lpr[k]=r*r
    g=copy.deepcopy(self)
    #for f,t in g.edges() : g[f][t]["weight"]=lpr[(f,t)]
    nx.set_edge_attributes(g,lpr,name="weight")
    #print('EATS',dict(nx.get_edge_attributes(g,name="weight")),'\n')
    #print("LPR",lpr,'\n')
    mr = g.pagerank()
    print('MR', mr, '\n')

    nx.set_node_attributes(g,mr,name='weight')
    #print('NATS', dict(nx.get_node_attributes(g, name="weight")),'\n')
    #show(g)
    return g

  def to_line_graph(self):
    return nx.line_graph(self)


  # dosplays graph using graphviz
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

# search using dfs, bfs, id algorithm
def search(g,algo,source,target) :
  for n in algo(g,source) :
    if n == target :
      return ('found',target)
  return 'not found'

# transitve closure using numpy matrices
def tc_with_mat(g) :
  m = g.to_matrix()
  dim = m.shape[0]
  res=m
  pow=m
  for _ in range(dim) :
    pow=pow.dot(m)
    res = np.logical_or(res, pow)
  return digraph(res)


# Transitive closure using dfs
def tc(g,refl=False) :
  t=digraph()
  for n in g.nodes() :
    for m in df_nodes(g,n) :
      if m!=n or refl:
        #print(n,m)
        t.add_edge(n,m)
  return t



# topological sort
# https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
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

def show(g,fname='graph.gv'):
  def round(x) :
    prec = 1000
    return str(int(prec*x)/prec)
  dot = gv.Digraph()
  d = nx.get_node_attributes(g, name='weight')
  de = nx.get_edge_attributes(g, name='weight')
  #print(len(d),"DDD",d)
  #print(len(d), "EEE", de)
  for (n,w) in d.items() :
      label = round(w)
      dot.node(str(n),label=str(n)+":"+label)
  for e,w in de.items():
    f, t = e
    #w = g[f][t].get('weight')
    label=''
    if w : label=round(w)
    dot.edge(str(f), str(t), label=label)
    #print(dot.source)
  dot.render(fname, view=True)
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

def t10() :
  g = digraph().random(8,20) # .show()
  m = g.to_matrix()
  print(m)
  print(m.shape)
  mm = m * m
  #print(mm)
  dim = m.shape[0]
  G = tc_with_mat(g)
  G.show()

def t11() :
  g = digraph().random(8,20)
  print(g.number_of_edges())
  t = tc(g)
  print(t.number_of_edges())
  t.show()

def t12() :
  g = digraph().random(5, 30)
  print(g.number_of_edges())
  lg=g.to_line_graph()
  show(g)
  show(lg,fname='line_graph.gv')

def t13() :
  g = digraph().random(5, 30)
  g=g.meta_rank()
  show(g,fname='meta.gv')

#t0()
#t1()
#t2()
#t3()
#t4()
#t5()
#t7()
#t8()
#t9()
#t10()
#t13()

