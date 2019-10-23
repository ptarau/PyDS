import networkx as nx
import graphviz as gv
import networkx.algorithms.traversal.depth_first_search as algs

class digraph(nx.DiGraph) :

  def rand(self):
    er = nx.dense_gnm_random_graph(24, 27)
    for e in er.edges() :
      f,t=e
      self.add_edge(f,t)
    er = nx.dense_gnm_random_graph(24, 7)
    for e in er.edges() :
      f,t=e
      self.add_edge(t,f)

    return self

  def show(self):
    return show(self)

def df_nodes(g,node,visited):
  if node in visited : return
  visited.add(node)
  yield node
  for child in  g[node] :
    for n in df_nodes(g,child,visited) :
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
  print(type(g))
  ns=algs.dfs_preorder_nodes(g)
  print(list(ns))
  visited=set()
  print(list(df_nodes(g,0,visited)))
  print(visited)

#t3()



