import networkx as nx
from graphviz import Digraph

# displays graph with graphviz
def show(dot,show=True,file_name='graph.gv')  :
  dot.render(file_name, view=show) 
  
def showGraph(g) :
  dot=Digraph()
  for e in g.edges():
    print(e)
    f,t=e
    dot.edge(str(f), str(t),label='')
  print(dot.source)
  show(dot)

def t1() :
  # edges
  es = [(1,2),(2,3),(1,3),(3,4),(4,5),(5,6),(4,6),(2,5),(1,6)]
  G=nx.Graph()
  G.add_edges_from(es)
  print('graph',G)
  showGraph(G)

def t2() :
  er = nx.erdos_renyi_graph(20, 0.15)
  showGraph(er)

def t3() :
  mz = nx.sedgewick_maze_graph()
  showGraph(mz)
