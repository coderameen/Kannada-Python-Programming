name = "Alen"
# name = 'bob'
# name = '''Coder ameen'''
# name = """celvin"""#User """ """ when you are using sentence
sentence = """Python  is a general purpose high level programming language. """
print(name)
print(sentence)

#Concatination
s1 = "Welcome"
s2 = " Python"
print(s1+s2)


#2.Indexing in String
name = "Alen"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
# print(name[4])
print(name[-1])#-ve indexing
print(name[-2])
mystr = "Hello"
print(mystr[:4])#slicing


#3. Length of string
name = "coder ameen"
print(len(name))


#4.reverse a string
str2 = "Prajwal"
print(str2[::-1])


#5.methods
str2 = "Hello World"
print(str2.lower())#hello world
print(str2.upper())#HELLO WORLD
print(str2.replace('World', 'Python'))#Hello Python
str2 = "ameen"
print(str2.capitalize())#Ameen

str3 = "coderameen"
print(str3.find("oder"))#1
print(str3.index("ameen"))#5 => ameen starts with index 5
print(str3.strip("coder"))


str4 = "coder07"
# only letter
print(str4.isalpha())#False
str4 = "coderameen"
print(str4.isalpha())#True

#Only Digit
s1 = "9873847"
print(s1.isdigit())#True
s2= "9865ameen"
print(s2.isdigit())#False
print(s2.isalnum())#True
print(s2.isspace())
print(s2.startswith("986"))
print(s2.endswith("meen"))


l = ['I','love','Python','','Great']
print(" ".join(l))


print("----------")
#String comparision
print("abc"=="abc")
print("ABC"=="abc")#Case Sensitive

print("abc" > "bcd")#False
print("abc"<"bcd")#True