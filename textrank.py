# ranking a document for most important sentences
import nltk
import networkx as nx
import heapq

def good_word(wt) :
  t=wt[1]
  return t[0] in "NJV"

def digest(doc) :
  text=[]
  with open(doc,'r') as f :
    for line in f.readlines() :
      line=line.replace('\n',' ')
      text.append(line+" ")
  text="".join(text)
  sents=nltk.sent_tokenize(text)
  wss=map(nltk.word_tokenize,sents)
  goodWordsSets=[]
  for ws in wss :
    ts=set(w for (w,t) in nltk.pos_tag(ws) if good_word((w,t)))
    goodWordsSets.append(ts)
  return goodWordsSets,sents

  #print(list(wss))

def build_intersection_graph(wss) :
  g=nx.DiGraph()
  m=len(wss)
  for i in range(0,m) :
    for j in range(i,m) :
      if wss[i].intersection(wss[j]) :
        g.add_edge(i,j)
  return g

def best_sents(g,k) :
  d=nx.pagerank(g)
  ranked=[]
  for (w,r) in d.items() :
    heapq.heappush(ranked,(r,w))
  for _ in range(k) :
    (r,i) = heapq.heappop(ranked)
    yield i


def summarize(fname='us_constitution.txt') :
  wss,sents=digest(fname)
  g=build_intersection_graph(wss)
  for i in best_sents(g,5) :
    yield i,sents[i]
  

#print(list(r))

def go() :
  for ns in summarize() :
    print(ns)

go()
