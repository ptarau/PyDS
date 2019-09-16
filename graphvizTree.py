from graphviz import Digraph

def decorateSimple(t) :
  i=0
  def st(t) :
    nonlocal i
    if t :
      j = i
      for s in t:
        i += 1
        yield (str(j),str(i))
        for e in st(s): yield e

  for e in st(t) : yield e

def showSimple(t) :
  g=Digraph()
  for e in decorateSimple(t) :
    f,t=e
    #g.node(f,'*')
    #g.node(t,'*')
    g.edge(f,t)
  g.view()

def showTree(t) :
  g=Digraph()
  i=0
  
  def label(x) : 
    if isinstance(x,tuple) :
      return str(x[0])
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
  # print(g)
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
  g.clear()

def t1a() :
  g=Digraph()
  g.edge('1','2')
  g.edge('1','3')
  g.edge('2','3')
  g.edge('3','1')
  g.view() 
  
def t2() :
  t=('l', ('l', ('a', ('a', 0, ('l', 3)), ('a', ('l', 0), 0))))
  print(t)
  showTree(t)
  
def l(x) : ('l',x)
def a(x,y) : ('a',x,y)

def t3() :
   t=l(a(l(a(l(0),l(1))),a(0,0)))
   print(t)
   showTree(t)
   
def s1() :
  return  list(decorateSimple(((),((),(),()),(),(((),),))))

def s2() :
  showSimple(((),((),(),()),(),(((),),)))
  
# test on multiple trees  

# defines lambda node
def l(x) : return ('l',x)

# defines app;lication node
def a(x,y) : return ('a',x,y)

def test(i) :
  ts=[
    l(a(a(1,a(l(l(0)),1)),1)),
    l(l(l(l(a(0,a(1,l(l(a(0,a(2,0)))))))))),
    l(l(l(a(a(0,a(1,a(a(l(l(0)),0),2))),1)))),
    l(l(l(a(l(1),a(l(a(1,0)),a(a(a(2,0),0),0)))))),
    l(l(l(a(l(a(2,a(a(l(0),l(a(1,a(1,a(1,l(1)))))),l(0)))),a(2,0)))))
  ]
  t=ts[i]
  print(i,'==>',t)
  showTree(t)
