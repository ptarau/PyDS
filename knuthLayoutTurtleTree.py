import turtle
import time

# tree with indices as leaves
# t = ('a',l,r) or ('l',t) or i where l,r are subtrees and i is an int de Bruijn index
# tree with x,y annotations
# t = ('a',x,y,l,r) or ('l',x,y,t) or (i,x,y)

# compute x,y annotations for each node, derived from Knuth's basic layout
def knuth_layout(t) :
  i=0
  def kl(t,d):
    nonlocal i
    x,y = i,d
    if isinstance(t,int) : return t,x,y #leaf
    tlen=len(t)
    if tlen == 2 : #unary
      n,subtree=t
      return  n,x,y,kl(subtree,d+1)
    elif tlen==3 : #binary
      n,l,r=t
      left = kl(l,d+1) 
      i += 1
      right = kl(r,d+1)
      return n,x,y,left,right
  return kl(t,0)
  
# draw an annotated tree, using turtle graphics  
def tdraw(t) :
  A,B=turtle.screensize()
  minX=-A
  minY=B
  turtle.up()
  
  def to(x,y) : turtle.goto(minX+50*x,minY-50*y) 
       
  def label(n,x,y) :
    to(x,y)
    turtle.down()
    turtle.write(n,font=('Arial',18,'normal'))
    turtle.up()
    
  def link(x1,y1,x2,y2) :
    turtle.up()
    to(x1,y1)
    turtle.down()
    to(x2,y2)
    turtle.up()
         
  def td(t) :
    n,x,y = t[0:3]
    label(n,x,y)
    l = len(t)
    if l==4 :
      u = t[3]
      ux,uy=u[1:3]
      link(x,y,ux,uy)
      tdraw(u)
    elif l==5 :
      lt=t[3]
      rt=t[4]
      lx,ly=lt[1:3]
      link(x,y,lx,ly)
      rx,ry=rt[1:3]
      link(x,y,rx,ry)
      td(lt)
      td(rt)
      
  td(t)   

# tests

# small test
def t1() :
  t=('l', ('l', ('a', ('a', 0, ('l', 3)), ('a', ('l', 0), 0))))
  tt = knuth_layout(t)
  print(t)
  print(tt)
  turtle.setup(1200,800)
  tdraw(tt)

