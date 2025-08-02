#Emplty List
myl = []
myl = list()

#List is a collection of mixed data enclosed within a square brackets.
l = [10,20,'a','b',"vineet",9.56,(10,20),[11,22],{10,56},{"name":"alen","age":25}]
# print(type(l))
print(len(l))
# print(l[-1].get('age'))

print("---")
for ele in l:
    if isinstance(ele, dict):
        if "age" in ele:
            print(ele['age'])


l2 = [11,22,33,44,55,66]
#indexing
print(l2[0])
print(l2[-1])
print(l2[1:4])#slicing

#concatination
l1 = [10,20,30]
l2 = [55,66,77]
print(l1 + l2)

#repetition
l= [1,2,4]
print(l*3)

#index
l = [10,20,30,40,50]
res = l.index(30)
print(res)

#Membership in and not in
fruits = ['apple','orange','grapes']
print('mango' in fruits)
print('apple' not in fruits)


#min, max,sum
l = [21,53,21,3,6,]
print(min(l))



#Insert element in list
'''
1.append(ele)
2.insert(index,ele)
3.extend(list)
'''
myl = []
myl.append(10)
myl.append(20)
myl.append(30)
myl.insert(1,15)
l5 = [11,22]
myl.extend(l5)
print(myl)


print("----------Remove-----------")
#Remove
'''
pop()
pop(index)
remove(ele)
clear
del
'''
myl = [10,20,30,40,50,60]
myl.pop()
myl.pop(2)
myl.remove(50)
print(myl)
myl.clear()
print(myl)
# del myl
# print(myl)

#	Counts occurrences of element
l = [11,22,33,22,22,22,55,66,77]
print(l.count(22))#4

#sort element
l = [3,6,4,9,8,1,2,5]
l.sort()
print(l)
l = [3,6,4,9,8,1,2,5]
res = sorted(l)
print(res)

#Reverse
l = [1,2,3,4,5,6,7]
l.reverse()
print(l)
l = [1,2,3,4,5,6,7]
res = reversed(l)
print(list(res))

#shallow copy
copied = l.copy()
print(copied)


#enumerate
myl = [10,20,30,40,50,60]
for idx,ele in enumerate(myl):
    print(idx,ele)


#-------list comprehension--------
l = [x for x in range(10)]
print(l)

#even
l = [x for x in range(10) if x%2==0]
print(l)

#odd
l = [x for x in range(10) if x%2!=0]
print(l)


#Squares of numbers
l = [x**2 for x in range(1,11)]
print(l)

#convert lower letters into upper letters
myl = [ch.lower() for ch in "coder ameen"]
print(myl)
print("".join(myl))


#Vowels (a,e,i,o,u)

res= [ch for ch in "coder ameen" if ch in "aeiou"]
print(res)