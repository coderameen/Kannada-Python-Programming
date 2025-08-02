# (a + b)

#a and b => operands
# + => operator
#(a + b) => expresion


'''
1. Arithmetic Operators: +,*,/,%,//
2. Comparision operators: ==, !=,>,<,>=,<=
3. Logical Operators: and, or, not
4. Assignment operators: =, +=,-=,/=,*=
5. Membership operators: in, not in
6. Bitwise operator: >>, <<, &, |,^, ~

'''

a = 10
b = 50
print(a == b)
print(a > b)
print(b > a)

print(a >= b)
print(a != b)

print("-------------logical operator---------")
n1 = 10
n2 = 30
print(True and True)
print(False and True)
print(n1==10 and n2!=30)

print(not True)
print(not False)

print("-----------------------member operators------")
#in, not in

l = [10,20,30,40,"apple","mango",'banana']
print(20 in l)
print("banana" in l)
print(1000 not in l)

#Seach
key = 13
l = [10,20,30,40,50]
print(key in l)