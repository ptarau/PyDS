# ranking a document for most important sentences
import nltk
import networkx as nx
import heapq

# nouns,verbs,adjectives
def good_word(wt) :
  w,t=wt
  return t[0] in "NJV"  and w.lower() not in stopwords

# words not worth using for retrivieng content
stopwords= {'am', 'are', 'be', 'been', 'being', 'did', 'do', 'does', 'doing',
             'don', 'few', 'had', 'has', 'have', 'having', 'hers', 'i', 'is',
             'may', 'might', 'most', 'other', 'others', 'our', 'ourselves',
            'own', 's', 'same', 'such',
             'their', 'theirs', 'was', 'were', 'would', 'your',
            'yours', 'yourselves'}

# from a file to sentences, tokens and words
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
    ts=set(w.lower() for (w,t) in nltk.pos_tag(ws) if good_word((w,t)))
    goodWordsSets.append(ts)
  return goodWordsSets,sents

# heuristics for adding edges: bi-directional links
def add_weighted_edge(g,i,j,wss) :
  ws,us = wss[i],wss[j]
  shared = ws.intersection(us)
  l = len(shared)
  r = len(ws) + len(us) - l
  if l > 0:
    g.add_edge(i, j, weight=l/r)
    g.add_edge(j, i, weight=l/r)
    
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

# build graph connecting words that occur in the same sentence
def build_co_occurence_graph(wss) :
  g=nx.DiGraph()
  for ws in wss :
    for w1 in ws :
      for w2 in ws :
        if w1 != w2 :
          g.add_edge(w1,w2)
  return g

# keywords, highest ranked first
def extract_keywords(wss,k) :
  g=build_co_occurence_graph(wss)
  d=nx.pagerank(g)
  by_rank = [(r,w) for (w,r) in d.items()]
  by_rank.sort()
  sorted=by_rank.reverse()
  for _,w in by_rank:
    if k>0 : yield w
    k-=1

# summary and keyword extractor
def summary_and_keywords(name='us_constitution.txt',s_count=6,w_count=6) :
  wss,sents=digest(name)
  g=build_intersection_graph(wss)
  summary=[(i,sents[i]) for i in sorted(best_sents(g,s_count))]
  keywords=[w for w in extract_keywords(wss,w_count)]
  return (summary,keywords)

def go() :
  summary,keywords=summary_and_keywords()
  print('SUMMARY:')
  for s in summary: print(s)
  print('')
  print('KEYWORDS:',keywords)

go()
