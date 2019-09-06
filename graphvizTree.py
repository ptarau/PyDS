from graphviz import Digraph

def showTree(t) :
  g=Digraph()
  i=0
  
  def label(x) : 
    if isinstance(x,tuple) :
      return x[0]
    else :
      return str(x)
   
  def link(a,i,b,j) : 
    si=str(i)
    sj=str(j)
    g.node(si,a)
    g.node(sj,b)
    g.edge(si,sj)
        
  def st(a) :   
    nonlocal i
  
    if isinstance(a,tuple) :
      op=a[0]
      i0=i
      for x in a[1:] :
        l=label(x)
        i+=1
        link(op,i0,l,i)     
        st(x)
     
  st(t)
  g.view()   
  

# small tests

def t1() :
  g=Digraph()
  g.node('1','a')
  g.node('2','b')
  g.edge('1','2')
  g.node('3','c')
  g.edge('1','3')
  g.view()

def t2() :
  g=Digraph()
  g.edge('1','2')
  g.edge('1','3')
  g.edge('2','3')
  g.edge('3','1')
  g.view() 
  
