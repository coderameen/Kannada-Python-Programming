#Iterative statements are nothing but looping statement
'''
for loop

while loop
Note: we con't have do while loop in python
'''

#To print number from 1 to 10
# print(1)
# print(2)
# print(3)
print("----------")
for i in range(10):
    print(i)
print("-----------")
for i in range(1,11):
    print(i)
print("----------")
for i in range(1,11,2):
    print(i)
print("-----------")
for i in range(10,0,-1):
    print(i)

print("-----------------")
for i in range(5,11):
    print(i)

print("---------------------")
#-------------------WHILE---------------
#10 to 2
i = 10
while i>=2:
    print(i)
    i-=1

print("-------------")
#1 to 10
i = 1
while i <= 10:
    print(i)
    i+=1


#Traverse on list
fruits = ['apple' ,'mango','banana','grapes']
for fruit in fruits:
    print(fruit)

l= [10,20,30,40,50]
for ele in l:
    print(ele)

print("-------")
n = len(l)
for i in range(0,n):
    print(l[i])



print("--------------------------------")
for i in range(11):      #n-1
    print(i)