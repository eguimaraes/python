Every Python list has a sort method that sorts it in place. If you don’t want to mess up
your list, you can use the sorted function, which returns a new list:
x = [4,1,2,3]
y = sorted(x)
x.sort()
# is [1,2,3,4], x is unchanged
# now x is [1,2,3,4]
By default, sort (and sorted ) sort a list from smallest to largest based on naively
comparing the elements to one another.
If you want elements sorted from largest to smallest, you can specify a reverse=True
parameter. And instead of comparing the elements themselves, you can compare the
results of a function that you specify with key :
# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True) # is [-4,3,-2,1]
# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
key=lambda (word, count): count,
reverse=True)List Comprehensions
Frequently, you’ll want to transform a list into another list, by choosing only certain
elements, or by transforming elements, or both. The Pythonic way of doing this is list
comprehensions:
even_numbers = [x for x in range(5) if x % 2 == 0]
squares
= [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]
# [0, 2, 4]
# [0, 1, 4, 9, 16]
# [0, 4, 16]
You can similarly turn lists into dictionaries or sets:
square_dict = { x : x * x for x in range(5) }
square_set = { x * x for x in [1, -1] }
# { 0:0, 1:1, 2:4, 3:9, 4:16 }
# { 1 }
If you don’t need the value from the list, it’s conventional to use an underscore as the
variable:
zeroes = [0 for _ in even_numbers]
# has the same length as even_numbers
A list comprehension can include multiple for s:
pairs = [(x, y)
for x in range(10)
for y in range(10)]
# 100 pairs (0,0) (0,1) ... (9,8), (9,9)
and later for s can use the results of earlier ones:
increasing_pairs = [(x, y)
for x in range(10)
for y in range(x + 1, 10)]
We will use list comprehensions a lot.
# only pairs with x < y,
# range(lo, hi) equals
# [lo, lo + 1, ..., hi - 1]Generators and Iterators
A problem with lists is that they can easily grow very big. range(1000000) creates an
actual list of 1 million elements. If you only need to deal with them one at a time, this can
be a huge source of inefficiency (or of running out of memory). If you potentially only
need the first few values, then calculating them all is a waste.
A generator is something that you can iterate over (for us, usually using for ) but whose
values are produced only as needed (lazily).
One way to create generators is with functions and the yield operator:
def lazy_range(n):
"""a lazy version of range"""
i = 0
while i < n:
yield i
i += 1
The following loop will consume the yield ed values one at a time until none are left:
for i in lazy_range(10):
do_something_with(i)
(Python actually comes with a lazy_range function called xrange , and in Python 3, range
itself is lazy.) This means you could even create an infinite sequence:
def natural_numbers():
"""returns 1, 2, 3, ..."""
n = 1
while True:
yield n
n += 1
although you probably shouldn’t iterate over it without using some kind of break logic.
TIP
The flip side of laziness is that you can only iterate through a generator once. If you need to iterate through
something multiple times, you’ll need to either recreate the generator each time or use a list.
A second way to create generators is by using for comprehensions wrapped in
parentheses:
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
Recall also that every dict has an items() method that returns a list of its key-value pairs.
More frequently we’ll use the iteritems() method, which lazily yield s the key-value
pairs one at a time as we iterate over it.Randomness
As we learn data science, we will frequently need to generate random numbers, which we
can do with the random module:
import random
four_uniform_randoms = [random.random() for _ in range(4)]
#
#
#
#
[0.8444218515250481,
0.7579544029403025,
0.420571580830845,
0.25891675029296335]
#
#
#
#
random.random() produces numbers
uniformly between 0 and 1
it's the random function we'll use
most often
The random module actually produces pseudorandom (that is, deterministic) numbers
based on an internal state that you can set with random.seed if you want to get
reproducible results:
random.seed(10)
print random.random()
random.seed(10)
print random.random()
#
#
#
#
set the seed to 10
0.57140259469
reset the seed to 10
0.57140259469 again
We’ll sometimes use random.randrange , which takes either 1 or 2 arguments and returns
an element chosen randomly from the corresponding range() :
random.randrange(10)
random.randrange(3, 6)
# choose randomly from range(10) = [0, 1, ..., 9]
# choose randomly from range(3, 6) = [3, 4, 5]
There are a few more methods that we’ll sometimes find convenient. random.shuffle
randomly reorders the elements of a list:
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten
# [2, 5, 1, 9, 7, 3, 8, 6, 4, 0]
(your results will probably be different)
If you need to randomly pick one element from a list you can use random.choice :
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
# "Bob" for me
And if you need to randomly choose a sample of elements without replacement (i.e., with
no duplicates), you can use random.sample :
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
# [16, 36, 10, 6, 25, 9]
To choose a sample of elements with replacement (i.e., allowing duplicates), you can just
make multiple calls to random.choice :
four_with_replacement = [random.choice(range(10))
for _ in range(4)]
# [9, 4, 4, 2]Regular Expressions
Regular expressions provide a way of searching text. They are incredibly useful but also
fairly complicated, so much so that there are entire books written about them. We will
explain their details the few times we encounter them; here are a few examples of how to
use them in Python:
import re
print all([
not re.match("a", "cat"),
re.search("a", "cat"),
not re.search("c", "dog"),
3 == len(re.split("[ab]", "carbs")),
"R-D-" == re.sub("[0-9]", "-", "R2D2")
]) # prints True
#
#
#
#
#
#
all of these are true, because
* 'cat' doesn't start with 'a'
* 'cat' has an 'a' in it
* 'dog' doesn't have a 'c' in it
* split on a or b to ['c','r','s']
* replace digits with dashesObject-Oriented Programming
Like many languages, Python allows you to define classes that encapsulate data and the
functions that operate on them. We’ll use them sometimes to make our code cleaner and
simpler. It’s probably simplest to explain them by constructing a heavily annotated
example.
Imagine we didn’t have the built-in Python set . Then we might want to create our own
Set class.
What behavior should our class have? Given an instance of Set , we’ll need to be able to
add items to it, remove items from it, and check whether it contains a certain value. We’ll
create all of these as member functions, which means we’ll access them with a dot after a
Set object:
# by convention, we give classes PascalCase names
class Set:
# these are the member functions
# every one takes a first parameter "self" (another convention)
# that refers to the particular Set object being used
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
When passing functions around, sometimes we’ll want to partially apply (or curry)
functions to create new functions. As a simple example, imagine that we have a function
of two variables:
def exp(base, power):
return base ** power
and we want to use it to create a function of one variable two_to_the whose input is a
power and whose output is the result of exp(2, power) .
We can, of course, do this with def , but this can sometimes get unwieldy:
def two_to_the(power):
return exp(2, power)
A different approach is to use functools.partial :
from functools import partial
two_to_the = partial(exp, 2)
print two_to_the(3)
# is now a function of one variable
# 8
You can also use partial to fill in later arguments if you specify their names:
square_of = partial(exp, power=2)
print square_of(3)
# 9
It starts to get messy if you curry arguments in the middle of the function, so we’ll try to
avoid doing that.
We will also occasionally use map , reduce , and filter , which provide functional
alternatives to list comprehensions:
def double(x):
return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
twice_xs = map(double, xs)
list_doubler = partial(map, double)
twice_xs = list_doubler(xs)
#
#
#
#
[2, 4, 6, 8]
same as above
*function* that doubles a list
again [2, 4, 6, 8]
You can use map with multiple-argument functions if you provide multiple lists:
def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]
Similarly, filter does the work of a list-comprehension if :
def is_even(x):
"""True if x is even, False if x is odd"""
return x % 2 == 0x_evens = [x for x in xs if is_even(x)]
x_evens = filter(is_even, xs)
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)
#
#
#
#
[2, 4]
same as above
*function* that filters a list
again [2, 4]
And reduce combines the first two elements of a list, then that result with the third, that
result with the fourth, and so on, producing a single result:
x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product = list_product(xs)
# = 1 * 2 * 3 * 4 = 24
# *function* that reduces a list
# again = 24enumerate
Not infrequently, you’ll want to iterate over a list and use both its elements and their
indexes:
# not Pythonic
for i in range(len(documents)):
document = documents[i]
do_something(i, document)
# also not Pythonic
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
We’ll use this a lot.
# not Pythonic
# Pythoniczip and Argument Unpacking
Often we will need to zip two or more lists together. zip transforms multiple lists into a
single list of tuples of corresponding elements:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)
# is [('a', 1), ('b', 2), ('c', 3)]
If the lists are different lengths, zip stops as soon as the first list ends.
You can also “unzip” a list using a strange trick:
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
The asterisk performs argument unpacking, which uses the elements of pairs as
individual arguments to zip . It ends up the same as if you’d called:
zip(('a', 1), ('b', 2), ('c', 3))
which returns [('a','b','c'), ('1','2','3')] .
You can use argument unpacking with any function:
def add(a, b): return a + b
add(1, 2)
add([1, 2])
add(*[1, 2])
# returns 3
# TypeError!
# returns 3
It is rare that we’ll find this useful, but when we do it’s a neat trick.args and kwargs
Let’s say we want to create a higher-order function that takes as input some function f and
returns a new function that for any input returns twice the value of f :
def doubler(f):
def g(x):
return 2 * f(x)
return g
This works in some cases:
def f1(x):
return x + 1
g = doubler(f1)
print g(3)
print g(-1)
# 8 (== ( 3 + 1) * 2)
# 0 (== (-1 + 1) * 2)
However, it breaks down with functions that take more than a single argument:
def f2(x, y):
return x + y
g = doubler(f2)
print g(1, 2)
# TypeError: g() takes exactly 1 argument (2 given)
What we need is a way to specify a function that takes arbitrary arguments. We can do this
with argument unpacking and a little bit of magic:
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