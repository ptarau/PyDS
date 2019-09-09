# simple graph coloring in Python 3
import itertools as it
 
# colors
cols=['r','g','b']

# edges
es = [(1,2),(2,3),(1,3),(3,4),(4,5),(5,6),(4,6),(2,5),(1,6)]

# pick a coloring if valid 
def pick_colors(vs,es) :
  for (i,j) in es :
    if vs[i-1]==vs[j-1] :
      return None
  return [(vs[i-1],vs[j-1]) for (i,j) in es]
 
# tries all possible colorings - works for small graphs  
def coloring(cols,es) :
  vss = it.product(cols,repeat=6)
  for vs in vss :
    edge_cols = pick_colors(vs,es)
    if edge_cols : yield edge_cols

# prints out all colorings
def go() :
  for edge_cols in coloring(cols,es) :
    print(edge_cols)

'''
>>> go()
[('r', 'g'), ('g', 'b'), ('r', 'b'), ('b', 'r'), ('r', 'b'), ('b', 'g'), ('r', 'g'), ('g', 'b'), ('r', 'g')]
[('r', 'g'), ('g', 'b'), ('r', 'b'), ('b', 'g'), ('g', 'r'), ('r', 'b'), ('g', 'b'), ('g', 'r'), ('r', 'b')]
[('r', 'b'), ('b', 'g'), ('r', 'g'), ('g', 'r'), ('r', 'g'), ('g', 'b'), ('r', 'b'), ('b', 'g'), ('r', 'b')]
[('r', 'b'), ('b', 'g'), ('r', 'g'), ('g', 'b'), ('b', 'r'), ('r', 'g'), ('b', 'g'), ('b', 'r'), ('r', 'g')]
[('g', 'r'), ('r', 'b'), ('g', 'b'), ('b', 'r'), ('r', 'g'), ('g', 'b'), ('r', 'b'), ('r', 'g'), ('g', 'b')]
[('g', 'r'), ('r', 'b'), ('g', 'b'), ('b', 'g'), ('g', 'b'), ('b', 'r'), ('g', 'r'), ('r', 'b'), ('g', 'r')]
[('g', 'b'), ('b', 'r'), ('g', 'r'), ('r', 'g'), ('g', 'r'), ('r', 'b'), ('g', 'b'), ('b', 'r'), ('g', 'b')]
[('g', 'b'), ('b', 'r'), ('g', 'r'), ('r', 'b'), ('b', 'g'), ('g', 'r'), ('b', 'r'), ('b', 'g'), ('g', 'r')]
[('b', 'r'), ('r', 'g'), ('b', 'g'), ('g', 'r'), ('r', 'b'), ('b', 'g'), ('r', 'g'), ('r', 'b'), ('b', 'g')]
[('b', 'r'), ('r', 'g'), ('b', 'g'), ('g', 'b'), ('b', 'g'), ('g', 'r'), ('b', 'r'), ('r', 'g'), ('b', 'r')]
[('b', 'g'), ('g', 'r'), ('b', 'r'), ('r', 'g'), ('g', 'b'), ('b', 'r'), ('g', 'r'), ('g', 'b'), ('b', 'r')]
[('b', 'g'), ('g', 'r'), ('b', 'r'), ('r', 'b'), ('b', 'r'), ('r', 'g'), ('b', 'g'), ('g', 'r'), ('b', 'g')]
>>> 
'''