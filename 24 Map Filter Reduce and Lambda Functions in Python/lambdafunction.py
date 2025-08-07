
#---------------------------MAP--------------
numbers = [3,4,5,6,7,8]
def square(x):
    return x*x

res = map(square,numbers)
print("resssss>>>",list(res))



#-------------------------Filter-------------
def age_greater_than_18(x):
    if x>=18:
        return True
    else:
        return False
a = [12,8,23,19,15,25,32,77,3,18]
new = list(filter(age_greater_than_18,a))
print(new)


#-------------------Reduce-----------
from functools import reduce
numbers= [1,2,3,4,5,6,7,8,9,10]
def sum(a,b):
    return a+b
res = reduce(sum,numbers)
print("reduce>>>>>>>>",res)


#-------------lambda function----------------------
# lambda arguments: expression

#WAP to find square of a number
def square(x):
    return x*x

result = square(5)
print(result)

#Lambda Function
square = lambda x:x*x
print(square(5))




#Map(): map() applies a function to each item in a list (or any iterable).

mylist = [1,2,3,4,5]
#douuble each number using map and reduce
result = list(map(lambda x:x*2, mylist))
print(result)
# print(list(result))

#filter(): filter() is used to filter items based on a condition.
#Program to filter only even number from list
mylist = [1,2,3,4,5]
evens = filter(lambda x:x%2==0, mylist)
print("filter>>",list(evens))

#reduce() applies a function to the first two items, then the result with the next item, and so on.
#multiply all numbers to gether 1*2*3*4*5
from functools import reduce
mylist = [1,2,3,4]
product = reduce(lambda x,y:x*y, mylist)
print(product)
