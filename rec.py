from  collections import *

# todo

# reverse a list, recursively

# queue with two stacks


# deque

'''
Deque objects support the following methods:

append(x)
Add x to the right side of the deque.

appendleft(x)
Add x to the left side of the deque.

clear()
Remove all elements from the deque leaving it with length 0.

copy()
Create a shallow copy of the deque.

New in version 3.5.

count(x)
Count the number of deque elements equal to x.

New in version 3.2.

extend(iterable)
Extend the right side of the deque by appending elements from the iterable argument.

extendleft(iterable)
Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

index(x[, start[, stop]])
Return the position of x in the deque (at or after index start and before index stop). Returns the first match or raises ValueError if not found.

New in version 3.5.

insert(i, x)
Insert x into the deque at position i.

If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raised.

New in version 3.5.

pop()
Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

popleft()
Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

remove(value)
Remove the first occurrence of value. If not found, raises a ValueError.

reverse()
Reverse the elements of the deque in-place and then return None.

New in version 3.2.

rotate(n=1)
Rotate the deque n steps to the right. If n is negative, rotate to the left.

When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft()).

'''