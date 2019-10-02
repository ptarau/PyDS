# emulation of dynamic hash maps - similar to dict in Python

class hashmap() :
  def __init__(self):
    self.H=[[]]*4
    self.ctr=0
  def add(self,k,v):
    h=hash(k) % len(self.H)
    vs=self.H[h]
    found=False
    for i in range(len(vs)) :
       if vs[i][0]==k :
         found=True
         vs[i][1]=v
         break
    if not found :
      vs.append((k,v))


  def __str__(self):
    return str(self.H)
    '''
    buf=[]
    for kv in H :
      if kv :
        for k,v in H[k] :
          buf.append((str(k),str(v)))
    '''







def t1() :
  d=hashmap()
  d.add('hello','Joe')
  d.add("bye",'Bill')
  d.add("howdy",'Mary')
  print(d)

