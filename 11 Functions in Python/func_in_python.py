'''
Type of Functions in python
1. Built In Functions: print(), len(), type(), range(), input(), sum(), max(), min(), sorted(), abs()
2. User Defined Functions:  4 types


'''
#1.Built In 
#print()
print("hello")
#len()
print(len("helloo"))
#type()
print(type(5.5))
#sum
print(sum([1,2,3,4,5,6,7,8,9,10]))
#max
print(max([45,3,22,65,1]))
#min
print(min([66,2,35,12]))
#abs
print(abs(-44.3))
#round()
print(round(6.65))
print(round(6.49))
#power(2,3)
print(pow(2,3))
#sorted()
print(sorted([6,3,4,5,1,2]))

import math
print(math.pow(2,3))
print(math.sqrt(25))
print(math.exp(2))
print(math.ceil(6.49))
print(math.floor(6.49))
print(math.factorial(5))#5!=5*4*3*2*1
print(math.fabs(5)) #0 1 1 2 3 5

print(math.pi)
print(math.e)#euler's formula


import statistics as stats 
data = [1,2,3,4,5]#odd
# data = [1,2,3,4,5,6]#even
print(stats.mean(data))
print(stats.median(data))
data = [1,2,3,2,1,2,2,2,5,6]
print(stats.mode(data))
print(stats.stdev(data))



#USER DEFINED FUNCTIONS
'''
1. Non parameterizd, non ruturn function
2. Non parameterized, return function
3. Parameterized, non return function
4. Parameterized., return function
'''
#1. Non Parameterized, non return function
def myfunc():
    a = 10
    b = 20
    result = a + b 
    print(f"The Total sum is {result}")

myfunc()
#2. non parameterized, return function
def mysum():
    a = 10
    b = 20
    result = a + b 
    return result

result = mysum()
print("Sum : ", result)

#3.Parameterized, non return function
def mysum(a,b):
    print(f"The sum is : {a+b} ")

mysum(30,30)


#4.Parameterized, return function
def mytotal(a,b):
    return f"The total sum is : {a+b}"

res = mytotal(40,40)
print(res)



def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

#Default argument

def myfunc(a,b,c=100):
    return a+b+c
res = myfunc(10,10)
print(res)




def greet(*args):
    # print(args)
    for name in args:
        print(f"Hello {name}")

greet("Ameen","Prajwal","Sanaan")


def person_info(**kwargs):
    name = kwargs.get("name")
    age = kwargs.get("age")
    print(f"The name is {name} and The age is {age}")
    
person_info(name = "Mohan", age=54)

