#Variable are nothing but a container used to store data in respective memory location
#Syntax: variable_name = data
a = 10
print(a) 

#Rule of variables
'''
1. Must start with letter or _ (underscore), never start with digit/number or special symbols
2. Variable name should not be a keyword (like: if, else,for,break,def, or, and)
3. case sensitive (name="alen", Name = "bob")
Note: use valide name that make sense like, name = "ameen", age=30, books = "Python development", 
markes=89
Suppose, Student Details => student_detials = None (Use only lower case!!)

NAMING NOTATION
'''



#----------------------Data Type-------------------
'''
Python Built in datatype: int,float,str,bool,set,list,tuple,dict
'''
num = 100
print(type(num))

person_height = 5.11
print(type(person_height))

name = "alen"
print(type(name))

is_active = False
print(type(is_active))

s = {10,20,30}
print(type(s))

d = {'name':'alen','age':40}
print(type(d))

l = [10,20,30]
print(type(l))

t = (10,20,30)
print(type(t))


#Type Casting/ Type Conversion: converting one datatype to another

num1 = "10"
num2 = "20"
print(int(num1) + int(num2))


#Bonus
#Interview: Mutable or immutable
#immutable: int, string, bool, tuple
#mutable: list, dictionary
n = 100
print(n)
print(id(n))
n = 200
print(id(n))
print(n)

mystr1 = "alen"
print(id(mystr1))
# mystr1 = "bob"
print(id(mystr1))


l = [10,20,30]
print(id(l))
l[0]= 1000
print(id(l))


d = {'name':'alen','age':30}
print(id(d))

d['name'] = 'celvin'
print(id(d))
print(d)




k = 10


print(id(k))