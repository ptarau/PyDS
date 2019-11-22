# ranking a document for most important sentences
import nltk
import networkx as nx
import heapq

# nouns,verbs,adjectives
def good_word(wt) :
  t=wt[1]
  return t[0] in "NJV"

# from a file to sentences and tokens
def digest(doc) :
  text=[]
  with open(doc,'r') as f :
    for line in f.readlines() :
      line=line.replace('\n',' ')
      text.append(line) #?
  text="".join(text)
  sents=nltk.sent_tokenize(text)
  wss=map(nltk.word_tokenize,sents)

  goodWordsSets=[]
  for ws in wss :
    ts=set(w for (w,t) in nltk.pos_tag(ws) if good_word((w,t)))
    goodWordsSets.append(ts)

  return goodWordsSets,sents

# heuristics for adding edges: pick one

# from last to first
def add_weighted_edge_(g,i,j,wss) :
  ws = wss[i]
  us = wss[j]
  shared = ws.intersection(us)
  l = len(shared)
  r = len(ws) + len(us) - l
  if l > 1:
    to = min(i,j)
    fr = max(i,j)
    g.add_edge(fr, to, weight=l/r)

# bi-directional links
def add_weighted_edge__(g,i,j,wss) :
  ws = wss[i]
  us = wss[j]
  shared = ws.intersection(us)
  l = len(shared)
  r = len(ws) + len(us) - l
  if l > 1:
    g.add_edge(i, j, weight=l/r)
    g.add_edge(j, i, weight=l/r)
    
# from longest to shortest
def add_weighted_edge(g,i,j,wss) :
  ws = wss[i]
  us = wss[j]
  shared = ws.intersection(us)
  l = len(shared)
  r = len(ws) + len(us) - l
  if l > 1:
    if len(us)<len(ws) :
      fr=i
      to=j
    else :
      fr = j
      to = i
    g.add_edge(fr, to, weight=l/r)

# build graph connecting sentences with shared words
def build_intersection_graph(wss) :
  g=nx.DiGraph()
  m=len(wss)
  for i in range(m) :
    for j in range(0,m) : #?
      add_weighted_edge(g, i, j, wss)
  return g

# highest ranked k sentences
def best_sents(g,k) :
  d=nx.pagerank(g)
  ranked=[]
  for (w,r) in d.items() :
    heapq.heappush(ranked,(1-r,w))
  for _ in range(k) :
    (r,i) = heapq.heappop(ranked)
    yield i

# summarizer
def summarize(name='us_constitution.txt') :
  wss,sents=digest(name)
  g=build_intersection_graph(wss)
  for i in sorted(best_sents(g,5)) :
    yield i,sents[i]

def go() :
  for ns in summarize() :
    print(ns)


def qa_loop(doc,question=None) :
  wss,sents=digest(doc)
  if question :
    q=question
  else :
    q=input('Your question: ')
  ws=nltk.word_tokenize(q)
  #print(wss[0])
  #print(ws)
  good_ws = set(w for (w, t) in nltk.pos_tag(ws) if good_word((w, t)))
  print('GOOD',good_ws)
  #shared={ws for ws in wss if good_ws.intersection(ws)}
  l=len(wss)
  print(l,'==',len(sents))
  for i in range(l) :
    doc_ws = set(wss[i])
    #if i<5 : print(doc_ws)
    shared = good_ws.intersection(doc_ws)
    if shared : print(shared,i)
    #if len(shared) > 1 : print(sents(shared[0]))

  #print(shared)
#go()

qa_loop('us_constitution.txt','Who can tax the people?')


