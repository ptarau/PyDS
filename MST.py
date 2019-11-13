# derived from: https://gist.github.com/Peng-YM/84bd4b3f6ddcb75a147182e6bdf281a6

# several minimum spanning tree algorithms
# with graphviz pics showing the result

import networkx as nx
import graphviz as gv
import numpy as np
import random
import math
import heapq


# turns weighted graph into matrix
def to_matrix(g):
  n=max(g.nodes())+1
  m=np.zeros((n,n),dtype=int)
  for f,t,d in g.edges(data=True) :
    m[f,t]=d['weight']
  return m

# random weighted undirected graph
def ran_graph(m,n) :
  g= nx.gnm_random_graph(n,m,seed=None,directed=False)
  for f,t,d in g.edges(data=True) :
    r=random.random()
    r=int(math.trunc(1000*r))
    r=r/1000
    d['weight']=r #.randint(0,10)
  return g

# used for the algorithms
class WeightedGraph:
  # overloaded contructor:
  # if M is an int, user random matrix
  # otherwise make matrix from given underected weighted graph
  def __init__(self,M):
    if isinstance(M,int) :
      self.graph=np.random.rand(M,M)
      self.vert_count=M
      self.edge_count= M * M
    else :
      n=len(M)
      self.graph= np.array([[float('+inf')]*n]*n)
      for f,t,d in M.edges(data=True) :
        self.graph[f,t]=d['weight']
      self.vert_count=n
      self.edge_count= n*n

def show(g,name='graph.gv'):
  dot = gv.Graph()
  for e in g.edges(data=True):
    f, t, d = e
    dot.edge(str(f), str(t), label=str(d['weight']))
  #print(dot.source)
  dot.render(name, view=True)
  return g

def tshow(mst,algo='mst') :
  g=nx.Graph()
  for f,t in mst :
    g.add_edge(f,t,weight='')
  show(g,name=algo+'.gv')

# Union find data structure for quick kruskal algorithm
class UF:
    def __init__(self, N):
        self._id = [i for i in range(N)]

    # judge two node connected or not
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # quick union two component
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root

    # find the root of p
    def find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p

# kruskal's algorithm
# see also: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
def kruskal(G):
    # initialize MST
    MST = set()
    edges = set()
    # collect all edges from graph G
    for j in range(G.vert_count):
        for k in range(G.vert_count):
            if G.graph[j][k] != 0 and (k, j) not in edges:
                edges.add((j, k))
    # sort all edges in graph G by weights from smallest to largest
    sorted_edges = sorted(edges, key=lambda e:G.graph[e[0]][e[1]])
    uf = UF(G.vert_count)
    for e in sorted_edges:
        u, v = e
        # if u, v already connected, abort this edge
        if uf.connected(u, v):
            continue
        # if not, connect them and add this edge to the MST
        uf.union(u, v)
        MST.add(e)
    return MST

# prim's algorithm
# see also https://en.wikipedia.org/wiki/Prim%27s_algorithm
def prim(G):
    # initialize the MST and the set X
    MST = set()
    Closed = set()

    # select an arbitrary vertex to begin with
    Closed.add(0)
    while len(Closed) != G.vert_count:
        #Open = set()
        Open = []


        # for each element x in Closed, add the edge (x, k) to Open if
        # k is not in Open
        for x in Closed:
            for k in range(G.vert_count):
                weight =G.graph[x][k]
                if k not in Closed and weight != 0:
                    #Open.add((x,k))
                    heapq.heappush(Open,(weight,x, k))
        # find the edge with the smallest weight in Open
        # can be made faster with priority queues
        #edge = sorted(Open, key=lambda e:G.graph[e[0]][e[1]])[0]
        weight,x,k = heapq.heappop(Open)
        edge = x,k

        # add this edge to MST
        MST.add(edge)
        #print('!!!! ADD',edge)
        # add the new vertex to X
        Closed.add(edge[1])
    return MST



# runs the algorithms on random weighted matrix
def mgo():
    WG = WeightedGraph(10)
    print(WG.graph)
    print("================USING PRIM ALGORITHM================")
    mst = prim(WG)
    # print the edges of the MST
    print(mst)
    tshow(mst, algo='prim')
    print("================END PRIM ALGORITHM================")
    print("================USING KRUSKAL ALGORITHM================")
    mst = kruskal(WG)
    # print the edges of the MST
    print(mst)
    tshow(mst, algo='kruskal')
    print("================END KRUSKAL ALGORITHM================")

# runs the agorithms on random weighted undirected graph
def go():
    g=ran_graph(10,10)
    show(g)
    
    WG=WeightedGraph(g) 
    print(WG.graph)
    print("================USING PRIM ALGORITHM================")
    mst = prim(WG)
    # print the edges of the MST
    print(mst)
    tshow(mst,algo='prim')
    print("================END PRIM ALGORITHM================")
    print("================USING KRUSKAL ALGORITHM================")
    mst = kruskal(WG)
    # print the edges of the MST
    print(mst)
    tshow(mst,algo='kruskal')
    print("================END KRUSKAL ALGORITHM================")

go()

