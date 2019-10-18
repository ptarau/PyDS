import networkx as nx
import graphviz as gv

class DGraph :
  def __init__(self):
    self.d=dict()

  def clear(self) :
    self.d = dict()

  def add_node(self,n):
    if not self.d.get(n) :
      self.d[n]=set()

  def add_edge(self,e):
    f,t=e
    self.add_node(f)
    self.add_node(t)
    vs=self.d.get(f)
    if not vs :
      self.d[f]={t}
    else :
      vs.add(t)

  def add_edges_from(self,es):
    for e in es :
      self.add_edge(e)

  def edges(self):
    for f in self.d :
      for t in self.d[f] :
        yield (f,t)

  def number_of_nodes(self) :
    return len(self.d)

  def __repr__(self):
    return self.d.__repr__()

  def show(self):
    dot = gv.Digraph()
    for e in self.edges():
      #print(e)
      f, t = e
      dot.edge(str(f), str(t), label='')
    #print(dot.source)
    show(dot)



def g1() :
  # edges
  es = [(1,2),(2,3),(1,3),(3,4),(4,5),(5,6),(4,6),(2,5),(1,6)]
  G=DGraph()
  G.add_edges_from(es)
  G.add_node(9)
  for e in G.edges() : print('edge',e)
  print('nodes',G.number_of_nodes())
  G.show()

  print('graph =',G)

# displays graph with graphviz
def show(dot,show=True,file_name='graph.gv')  :
  dot.render(file_name, view=show) 
  
def showGraph(g) :
  dot=gv.Digraph()
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
