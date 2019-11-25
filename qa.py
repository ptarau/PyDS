# ranking a document for most important sentences
import nltk
import networkx as nx
import heapq
import math

default_doc='us_constitution.txt'

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

# from a file, to sentences and tokens
def digest(doc) :
  text=[]
  with open(doc,'r') as f :
    for line in f.readlines() :
      line=line.replace('\n',' ')
      text.append(line)
  text="".join(text) # text as read from file
  sents=nltk.sent_tokenize(text) # list of sentences
  wss=map(nltk.word_tokenize,sents) # list of list of words
  goodTokenSets=[] # token = (word,POS-tag)
  for ws in wss :
    ts=set(w.lower() for (w,t) in nltk.pos_tag(ws) if good_word((w,t)))
    #print('ts',ts)
    goodTokenSets.append(ts)
  return goodTokenSets,sents

# build graph connecting sentences with shared words
def build_intersection_graph(wss) :
  g=nx.DiGraph()
  m=len(wss)
  for i in range(m) :
    for j in range(0,m) :
      add_weighted_edge(g, i, j, wss)
  return g

# heuristics for adding edges:
# bi-directional if they share words
def add_weighted_edge(g,i,j,wss) :
  ws = wss[i]
  us = wss[j]
  shared = ws.intersection(us)
  l = len(shared)
  if l>0 :
    r = len(ws) + len(us) - l
    g.add_edge(i, j, weight=l/r)
    g.add_edge(j, i, weight=l / r)

# yields highest ranked k sentence numbers
# if personalisation dictionary given
# yields those relavant to it
def best_sents(g,wss,k,pers=None) :
  d=nx.pagerank(g,personalization=pers)
  ranked=[]
  for (s,r) in d.items() :
    rank=(1-r) #(1+math.log(1+len(wss[s])))
    heapq.heappush(ranked,(rank,s))
  for _ in range(k) :
    if ranked:
      (r,i) = heapq.heappop(ranked)
      yield i

# summarizer
def summarize(doc=default_doc) :
  wss,sents=digest(doc)
  g=build_intersection_graph(wss)
  xs=best_sents(g,wss,5)
  for i in sorted(xs) :
    yield i,sents[i]

# tests summary extraction
def sumtest(doc=default_doc) :
  print('SUMMARY')
  for ns in summarize(doc) :
    print(ns)
  print('')

# intracts via QA loop or answers canned question
def qa_loop(doc=default_doc,answer_count=3,question=None) :
  wss,sents=digest(doc)
  g = build_intersection_graph(wss)
  prompt='Your question: '
  if question :
    print(prompt,question)
    show_answers(qa_step(wss, sents, g, answer_count, question))
  else :
    while(True) :
      q=input(prompt)
      if not q : break
      show_answers(qa_step(wss, sents, g, answer_count, q))

# displays answers if any
def show_answers(answer_generator) :
    answers=list(answer_generator)
    print('')
    if answers :
      for answer in answers:
        print(answer)
    else :
      print('I have no answer to that.')
    print('')

# finds answer(s) to one question
def qa_step(wss,sents,g,k,question) :
  ws=nltk.word_tokenize(question)
  query_ws = set(w.lower() for (w, t) in nltk.pos_tag(ws) if good_word((w, t)))
  sent_count=len(wss)
  personalizer=dict()
  sharing_count=0
  max_shared=0
  for i in range(sent_count) :
    doc_ws = wss[i]
    shared = query_ws.intersection(doc_ws)
    l=len(shared)
    if l>0 :
      personalizer[i]=l
      sharing_count+=l
      max_shared=max(max_shared,l)
  for i,v in personalizer.items():
     personalizer[i]=v/sharing_count
  xs=best_sents(g,wss,100,pers=personalizer)
  best=[]
  seen=set()
  for i in xs :
    if k<=0 : break;
    shared=wss[i].intersection(query_ws)
    if len(shared)>=max_shared-1 and len(shared)>0:
      s=sents[i]
      if s in seen : continue
      k -= 1
      best.append( (i,s) )
      seen.add(s)
  for x in sorted(best) :
    yield x

# tests ------------

# test QA with canned question - good for fine-tuning things
def qtest() :
  qa_loop(default_doc,answer_count=3,question='What are the powers of the Senate?')

# runs a canned query on default document
def go() :
  sumtest()
  qtest()

# interactive chat about given document
def chat(doc=default_doc) :
  sumtest(doc=doc)
  qa_loop(doc=doc, answer_count=3)

# by default, interact!
chat()


