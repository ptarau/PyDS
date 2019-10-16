import networkx as nx
from graphviz import Digraph

# displays graph with graphviz
def showDot(dot,show=True,file_name='graph.gv')  :
  dot.render(file_name, view=show) 
  
def showGraph(g) :
  dot=Digraph()
  for e in g.edges():
    f,t=e
    dot.edge(str(f), str(t),label='x')
    showDot(dot)

        
def t0() :
  # edges
  es = [(1,2),(2,3),(1,3),(3,4),(4,5),(5,6),(4,6),(2,5),(1,6)]
  G=nx.Graph()
  G.add_edges_from(es)
  print('graph',G)
  showGraph(G)


