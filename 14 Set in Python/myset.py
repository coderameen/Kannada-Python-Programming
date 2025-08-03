my_set = {1,2,3}

#empty set
s = set()

#Removes duplicates 
l = [10,10,10,20,34,10,20]
print(set(l))

#membership in set
s = {1,2,3,4}
print(1 in s)
print(5 not in s)

#looping the set
for item in s:
    print(item)

#insert/add element in set
mys = set()
mys.add(100)
mys.add(200)
print(mys)
mys.update([5,6,7])
print(mys)

my_frozen_set = frozenset([11,22,33])
print("my forzen set: ",my_frozen_set)
# my_frozen_set.add(44)# Will raise error (immutable)

#Remove in set
mys.remove(200)#Raise error if not found
mys.discard(10000)#raise no error, if not found
mys.pop()
mys.clear()



#len,min,max,sum,sorted
s = {100,10,50}
print(sorted(s))
#Methematical set operation
a = {1,2,3,4}
b = {3,4,5,6}
#union
a.update(b)
print(a)
#intersection
res = a.intersection_update(b)
print(res)