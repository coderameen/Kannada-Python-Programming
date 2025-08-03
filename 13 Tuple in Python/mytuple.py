my_tuple = (1,2,3)


#emplty tuple
my_tuple = tuple()
my_tuple = ()
print(type(my_tuple))

#nested_tuple
nested_tuple = ((1,2),(3,4))


#Accessing tuple elements/Tuple indexing
t = (11,22,33,44,55)
print(t[0])
print(t[1])
print(t[-1])
print(t[1:3])#slice
print(t[::-1])#reverse

#len,sum,min,max,*(repetition), in

#Looping in tuple
t_marks = (87,98,78,92,29)
for i in t_marks:
    print(i)

#enumerate
my_t = ('Alen','bob','celvin')
for index,value in enumerate(my_t):
    print(index, value)

#count - count no. of occurrence
my_t = (11,11,11,22,33,11,44)
my_t.count(11)
my_t.index(22)#index of element

#NOTE: Tuple are immutable, so we don't have methods like .append()
#.remove(), .pop()

#Type casting
l = [10,20,30]
print(tuple(l))


#sort in tuple
t = (3,6,1,8,11,10)
sorted_t = sorted(t)
print(sorted_t)