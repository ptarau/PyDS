import networkx as nx
import graphviz as gv

class digraph(nx.DiGraph) :

  def rand(self):
    er = nx.dense_gnm_random_graph(12, 12)
    for e in er.edges() :
      f,t=e
      self.add_edge(f,t)
    er = nx.dense_gnm_random_graph(12, 12)
    for e in er.edges() :
      f,t=e
      self.add_edge(t,f)
    if 0 not in self.nodes(): self.add_edge(0, 1)

    return self

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


#t1()
#t2()
#t3()
t4()
