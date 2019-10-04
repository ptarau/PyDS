# emulation of dynamic hash maps - similar to dict in Python

class hashmap() :
  def __init__(self):
    self.H=[[]]*4
    self.ctr=0

  def add(self,k,v):
    h=hash(k) % len(self.H)
    vs=self.H[h]
    if not vs : vs=[(k,v)]
    else :
      found=False
      for i in range(len(vs)) :
        if vs[i][0]==k :
          found=True
          vs[i][1]=v
          break
      if not found :
        vs.append((k,v))
    self.H[h]=vs

  def get(self,k) :
    h = hash(k) % len(self.H)
    vs = self.H[h]
    for i in range(len(vs)):
      if vs[i][0] == k: return vs[i][1]
    return None

  def remove(self,k) :
    h = hash(k) % len(self.H)
    vs = self.H[h]
    if not vs: return
    where=-1
    for i in range(len(vs)) :
      if vs[i][0]==k :
        where=i
        break
    if where >= 0 :
      vs.pop(where)

  def __str__(self):
    #return str(self.H)
    buf=['[\n']
    i=0
    for kvs in self.H :
      if kvs :
        buf.append(str(i) + ":")
        for kv in kvs :
          buf.append(str(kv))
        buf.append("\n")
      i+=1
    buf.append(']')
    return "".join(buf)

  def __getitem__(self,k) :
    return self.get(k)

  def __setitem__(self,k,v) :
    self.add(k,v)


def t1() :
  d=hashmap()
  d.add('hello','Joe')
  d.add("bye",'Bill')
  d.add("howdy",'Mary')
  d.add("cheers",'Mike')
  d.add("so long", 'Jill')
  print(d)
  print(d.get('howdy'))
  d.remove('noShuchKey')
  d.remove('cheers')
  print(d)
  print(d.get('cheers'))
  print(d['bye'])
  d['cheers']='Henry'
  print(d)
  return(d)

t1()

# todo: make the hashMap grow and shrink
# todo: make it support Python [] syntax for get, add
