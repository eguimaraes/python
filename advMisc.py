x = [4,1,2,3]
y = sorted(x)
x.sort()

x = sorted([-4,1,-2,3], key=abs, reverse=True) # is [-4,3,-2,1]

wc = sorted(word_counts.items(),
key=lambda (word, count): count,reverse=True)

even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

square_dict = { x : x * x for x in range(5) }
square_set = { x * x for x in [1, -1] }

zeroes = [0 for _ in even_numbers]

pairs = [(x, y)
for x in range(10)
for y in range(10)]

# 100 pairs (0,0) (0,1) ... (9,8), (9,9)

increasing_pairs = [(x, y)
for x in range(10)
for y in range(x + 1, 10)]

def lazy_range(n):
i = 0
while i < n:
yield i
i += 1

for i in lazy_range(10):
do_something_with(i)

def natural_numbers():
n = 1
while True:
yield n
n += 1
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

import random
four_uniform_randoms = [random.random() for _ in range(4)]

random.random() 

random.seed(10)
print random.random()
random.seed(10)
print random.random()

random.randrange(10)
random.randrange(3, 6)

up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

my_best_friend = random.choice(["Alice", "Bob", "Charlie"])

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)

four_with_replacement = [random.choice(range(10))
for _ in range(4)]

import re
print all([
not re.match("a", "cat"),
re.search("a", "cat"),
not re.search("c", "dog"),3 == len(re.split("[ab]", "carbs")),"R-D-" == re.sub("[0-9]", "-", "R2D2")])

class Set:
def __init__(self, values=None):
"""This is the constructor.
It gets called when you create a new Set.
You would use it like
s1 = Set()
# empty set
s2 = Set([1,2,2,3]) # initialize with values"""
self.dict = {} # each instance of Set has its own dict property
# which is what we'll use to track memberships
if values is not None:
for value in values:
self.add(value)
def __repr__(self):
"""this is the string representation of a Set object
if you type it at the Python prompt or pass it to str()"""
return "Set: " + str(self.dict.keys())
# we'll represent membership by being a key in self.dict with value True
def add(self, value):
self.dict[value] = True
# value is in the Set if it's a key in the dictionary
def contains(self, value):
return value in self.dict
def remove(self, value):
del self.dict[value]
Which we could then use like:
s = Set([1,2,3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)
# True
# FalseFunctional Tools

def exp(base, power):
return base ** power

def two_to_the(power):
return exp(2, power)

from functools import partial
two_to_the = partial(exp, 2)
print two_to_the(3)

def double(x):
return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
twice_xs = map(double, xs)
list_doubler = partial(map, double)
twice_xs = list_doubler(xs)

[2, 4, 6, 8]

def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) 


def is_even(x):

return x % 2 == 0x_evens = [x for x in xs if is_even(x)]
x_evens = filter(is_even, xs)
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)
#
#
#
#
[2, 4]

x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product = list_product(xs)

for i in range(len(documents)):
document = documents[i]
do_something(i, document)

i = 0
for document in documents:
do_something(i, document)
i += 1
The Pythonic solution is enumerate , which produces tuples (index, element) :
for i, document in enumerate(documents):
do_something(i, document)
Similarly, if we just want the indexes:
for i in range(len(documents)): do_something(i)
for i, _ in enumerate(documents): do_something(i)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)

If the lists are different lengths, zip stops as soon as the first list ends.
You can also “unzip” a list using a strange trick:
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

zip(('a', 1), ('b', 2), ('c', 3))
 
def add(a, b): return a + b
add(1, 2)
add([1, 2])
add(*[1, 2])

def doubler(f):
def g(x):
return 2 * f(x)
return g


def f1(x):
return x + 1
g = doubler(f1)
print g(3)
print g(-1)
# 8 (== ( 3 + 1) * 2)
# 0 (== (-1 + 1) * 2)

def f2(x, y):
return x + y
g = doubler(f2)
print g(1, 2)
def magic(*args, **kwargs):
print "unnamed args:", args
print "keyword args:", kwargs
magic(1, 2, key="word", key2="word2")
# prints
# unnamed args: (1, 2)
# keyword args: {'key2': 'word2', 'key': 'word'}
That is, when we define a function like this, args is a tuple of its unnamed arguments and
kwargs is a dict of its named arguments. It works the other way too, if you want to use a
list (or tuple ) and dict to supply arguments to a function:
def other_way_magic(x, y, z):
return x + y + z
x_y_list = [1, 2]
z_dict = { "z" : 3 }
print other_way_magic(*x_y_list, **z_dict)
# 6
You could do all sorts of strange tricks with this; we will only use it to produce higher-
order functions whose inputs can accept arbitrary arguments:
def doubler_correct(f):
"""works no matter what kind of inputs f expects"""
def g(*args, **kwargs):"""whatever arguments g is supplied, pass them through to f"""
return 2 * f(*args, **kwargs)
return g
g = doubler_correct(f2)
print g(1, 2) # 6