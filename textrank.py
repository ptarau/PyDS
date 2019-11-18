# ranking a document for most important sentences

import nltk
import networkx as nx

def tokenize(s) :
  s = s.replace('.', ' .')
  ws = s.split()
  return ws

def digest(doc) :
  text=[]
  with open(doc,'r') as f :
    for line in f.readlines() :
      line=line.replace('\n',' ')
      text.append(line+" ")
  text="".join(text)
  sents=nltk.sent_tokenize(text)
  wss=map(tokenize,sents)
  return wss

  #print(list(wss))

def build_intersection_graph(wss) :
  g=nx.DiGraph()
  for s in wss :
    print(s)


def t1() :
  r=nltk.sent_tokenize("The cat sits on the mat. The dog barks.")
  for s in r :
    s=s.replace('.',' .')
    ws=s.split()
    print(ws)


def t2() :
  wss=digest('doc.txt')
  build_intersection_graph(wss)
  # if intersection has elements
  # connect latest sentence to earler
  

#print(list(r))

t2()