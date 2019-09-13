# O(n^2)
# T(n) = T(n-1) + n
def insertion_sort(xs):
  for i in range(1, len(xs)):
    here = i
    while here > 0 and xs[here - 1] > xs[here]:
      xs[here], xs[here - 1] = xs[here - 1], xs[here]
      here -= 1
  return xs

# O(n^2)
# # T(n) = T(n-1) + n
def bubble_sort(xs):
  l = len(xs)
  for i in range(l - 1):
    swapped = False
    for j in range(l - 1 - i):
      if xs[j] > xs[j + 1]:
        swapped = True
        xs[j], xs[j + 1] = xs[j + 1], xs[j]
    if not swapped:
      break  # Stop iteration if the xs is sorted.
  return xs

# O(n log(n)) T(n) = 2T(n/2)+n
def merge_sort(xs):
	#if list contains only 1 element return it
	if len(xs) <= 1:
		return xs
	else:
		mid = int(len(xs)/2)
    # sort both slices
		ls = merge_sort(xs[:mid])
		rs = merge_sort(xs[mid:])
    # merge the sorted
		return merge_lists(ls,rs)

def merge_lists(ls,rs):
	i,j = 0,0
	result = []
	#iterate through both left and right sublist
	while i<len(ls) and j<len(rs):
		#if left value is lower than right then append it to the result
		if ls[i] <= rs[j]:
			result.append(ls[i])
			i += 1
		else:
			#if right value is lower than left then append it to the result
			result.append(rs[j])
			j += 1
	#concatenate the rest of the left and right sublists
	result += ls[i:]
	result += rs[j:]
	#return the result
	return result

# O(N^2) worst case, but O(n log(n)) on average
def quick_sort(xs) :
  if xs==[] : return xs
  x=xs[0]
  ys=xs[1:]
  ls=[y for y in ys if y<=x]
  bs=[y for y in ys if y>x]
  return quick_sort(ls) + [x] + quick_sort(bs)

# timing

from timeit import timeit as tm
from random import randint

def randints(n) :
  for i in range(n) :
    yield randint(0,n-1)

def qbm(f,n) :
  print('benchmark for sorting',n,'numbers')
  print(tm(lambda : f(list(randints(n))),number=1))

# tests
def t1() :
  ns = [5,3,6,8,1,9,4,5,6,9,0,2,3,6]
  print('insertion_sort')
  print(ns)
  print(insertion_sort(ns))

def t2() :
  ns = [5,3,6,8,1,9,4,5,6,9,0,2,3,6]
  print('bubble_sort')
  print(ns)
  print(bubble_sort(ns))

def t3() :
  print('merge_sort')
  ns = [5,3,6,8,1,9,4,5,6,9,0,2,3,6]
  print(ns)
  print(merge_sort(ns))

def t4() :
  print('quick_sort')
  ns = [5,3,6,8,1,9,4,5,6,9,0,2,3,6]
  print(ns)
  print(merge_sort(ns))


def go() :
  t1()
  t2()
  t3()
  t4()
