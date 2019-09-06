def subset(Xs) : 
  if not Xs : yield Xs
  else :
    X = Xs[0]
    Ys = Xs[1:]
    for Zs in subset(Ys) :
      yield Zs
      yield (X,) + Zs
    
def test() : 
  for t in subset( (0,1,2,3) ) : print(t)
