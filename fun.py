def fibo(n) :
  if n<2 : 
    return 1
  else :
    return fibo(n-2) + fibo(n-1)
  
succ = lambda x : x+1  

fibo1 = lambda x : 1 if x<2 else fibo1 (x-1) + fibo1(x-2)


def fibo2(n) :
  i = 1
  j = 1 
  k=0
  while(k<n) :
    ij=i+j
    i=j
    j=ij
    k+=1
  return i
  
def fibos(n) :  
  def f() :
    i,j = 0,1
    k = 0 
    while(k<n) :
      k+=1
      i,j=j,i+j
      yield i
  return list(f())
  
def fibos1(n) :
   rs=[]
   i,j = 0,1 
   k = 0
   while(k<n) :
     k+=1
     i,j=j,i+j
     rs.append(i)
   return(rs)

# examples of use

print('hello')

print(fibo(10))


