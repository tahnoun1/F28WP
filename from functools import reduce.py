from functools import reduce
from math import sqrt, ceil

#QUESTION 1:
"""Using iteration (a for-next or a while loop or similar), write a program `mult1` that if given a list of integers
 or reals will return their product (the result of multiplying all the numbers together).
 We do not care about behaviour if mult1 is not given a list of integers or reals; likewise for mult2 and mult3 below. 
 mult1 should return 1 for the empty list, because 1 is the multiplicative unit. Thus:

mult1([]) returns 1, and
mult1([1,2,3,10]) returns 60.
"""


def mult1(l):
    total=1  
    for i in l:
        total=(total*i)
    return(total)

a=mult1([1,2,3,10])
print(a)
 
############
#QUESTION 2:
"""Using recursion, write a program `mult2` that if given a list of integers or reals will return their product 
(warning: this question is very slightly harder than it seems; make sure to test your answer)."""


def mult2(l):
     total=1  
    for i in l:
        total=(total*i)
    return(total)

b=mult2([1,2,3,10])
print(b)
    

############
#QUESTION 3:
"""Using Python lambda and reduce (see specifically the example on line 2 of this link), write a program mult3 that if 
given a list of integers or reals, returns their product."""


def mult3(l):
    pass


############
#QUESTION 4:


"""
Using if type(x) is list or otherwise, write a recursive program **flatten** that inputs an arbitrarily nested list 
structure and outputs a “flattened” list consisting of the list of all the data in the list, but with any nested list 
structure removed. So for instance,
- flatten([]) returns [], and
- flatten([["hi"],5]) returns ["hi",5], and
- flatten([[[],[["hello"],[" "]],[1],[[["world"]],[]]],"!"]) returns ["hello"," ",1,"world!"].   
"""


def flatten(li):
    pass

############
#QUESTION 5:


"""Write a program `prime_factors` that inputs a number n, which you may assume is greater than 2, and outputs the list of its 
primefactors (prime numbers are 2, 3, 5, 7, 11, 13, 17, and so on). You may assume basic arithmetic operations, 
including modulus n % k and divisibility. However, if you find a library call “prime_factors_of”, you can’t use that"""

#Hint: this helper function may come in useful
def isprime(number):
    pass

def prime_factors(number):
    pass

############
#QUESTION 6:

"""Write a program `largest` that inputs a nonempty list of numbers and outputs its greatest element. You do not need to 
worry about error-handling, e.g. if the input is the empty list."""


def largest(li):
    pass


##########
#QUESTION 7:
"""Write a program `largest_factor` that inputs a number n and outputs its largest prime factor."""


def largest_factor(number):
    pass


##########
#QUESTION 8:

"""Write a program `first_big_f` that inputs a number n and a function f mapping numbers to numbers, and outputs the least 
strictly positive number i (so i is in [1,2,3,...]) such that f(i) contains n digits. 
So for example if f=lambda x:10**x then firstbigf f 10 should calculate 9 (because 10**9, which is equal to 1000000000, 
has ten digits)."""


def first_big_f(n, f):
    pass

##########
#QUESTION 9:
"""Write a program `first_big_fib` that inputs a number n and outputs the index of the first Fibonacci number to contain n digits."""


# This program treats the Fibonacci sequence as "0,1,1,2...", with "0" as the zeroeth value
def fibonacci(index):
    fiblist = [0, 1]
    if index == 0:  # edge case handling
        return fiblist[0]
    while index > (len(fiblist) - 1):
        nextfib = fiblist[-1] + fiblist[-2]
        fiblist.append(nextfib)
    return fiblist[-1]




def first_big_fib(n):
    return first_big_f(n, fibonacci)






##########
#QUESTION 10:

"""A **Pythagorean triple** is a 3-tuple of strictly positive numbers (x,y,z) such that z*z=x*x+y*y. Using Python generators 
write a Python generator function pyth_triples() to generate all Pythagorean triples. So:

x=triples() and then next(x) should return a first triple, and then next(x) should return a second triple, and then
next(x) should return a third one, and so on.

"""

#See: Wikipedia: https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#I

def pyth_triples():
    m = 2
    while True:
        for n in range(1, m):
            yield (m**2-n**2, 2*m*n,m**2+n**2)
        m += 1





##########
#QUESTION 11:

"""
The **zip function** inputs two lists (which you may assume have the same length) and outputs the list of pairs of the lists
‘zipped’ together. For instance, zip([1,2,3],["one","two","three"]) returns [(1,"one"),(2,"two"),(3,"three")]. Implement
 zip yourself, from first principles, using (a) iteration; (b) recursion; (c) list comprehension.
"""


#(a):
def my_zip_iter(l1, l2):
    result = []
    for i in range(len(l1)):
        result.append((l1[i], l2[i]))
    return result


#(b):
def my_zip_recur(l1, l2):
    if not l1:
        return []
    else:
        result = [(l1[0], l2[0])]
        result.extend(my_zip_recur(l1[1:], l2[1:]))
        return result



#(c):
def my_zip_comp(l1, l2):
    return [(l1[i], l2(i)) for i in range(len(l1))]
