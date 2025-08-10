# exception handling is a way to deal with errors without crashing the program.


#Sum of 2 numbers
# n1 = int(input("Enter num1: "))
# n2 = int(input("Enter num 2: "))
# print(n1 + n2)#if n1="coder"

try:
    # n1 = int(input("Enter num1: "))
    # n2 = int(input("Enter num 2: "))
    n2 = 10
    n3= "Ameen"
    print(n1 + n2)
# except:
#     print("Please provide only integer input!!")

except Exception as e:
    print("Unknown error occurred!", e)


#--------------------------using while---------------
#Zero division 
'''
while True:
    try:
        a = int(input("Enter num 1: "))
        b = int(input("Enter num 2: "))
        print(f"The division is {a/b} ")
        
        
        
    except ValueError:
        print("Please dont perform bad typecasts")
    except ZeroDivisionError:
        print("Hey dont divide by 0")
    except Exception as e:
        print("Unkown error occurred", e)
        
'''

#Raise an Exception
'''
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
if b == 0:
    raise ValueError("Please dont divide by 0")

print(f"The division is {a/b}")
'''


#-----------Else-------------------
try:
    a = 234/10
except Exception as e:
    print(e)
#Get execute when there is no error in the try block
else:
    print("Hey I am good!")

#---------------Finally---------
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
try:
    c = a/b
    print(c)
    
except Exception as e:
    print(e)

#This is always executed no matter if try completely executes or not
finally:
    print("This is always executes!!")
    
#------------------Bonus(why finally)----------

def divide(a,b):
    try:
        c = a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    #This is always execute no matter if try complelty executes or not
    finally:
        print("This is always executed!!")
        
a = int(input("Enter number 1: "))
b = int(input("Enter number 2:"))

divide(a,b)