import networkx as nx
import graphviz as gv
import numpy as np

def ran_graph(m,n) :
  return nx.gnm_random_graph(n,m,
            seed=None,directed=False)

def ran_matrix(m, n):
  g = ran_graph(m, n)
  print(list(g.edges()))
  m = nx.to_numpy_matrix(g,dtype=int)
  return m




def show(g):
  dot = gv.Graph()
  for e in g.edges():
    f, t = e
    dot.edge(str(f), str(t), label='')
    #print(dot.source)
  dot.render('graph.gv', view=True)
  return g


def t1() :
  m = ran_matrix(10,6)
  g = nx.Graph(m)
  show(g)
  print(m)

def t2() :
  g=ran_graph(20,10)
  show(g)

t2()
