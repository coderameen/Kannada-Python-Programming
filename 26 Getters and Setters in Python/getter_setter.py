class Person:
    def __init__(self,name):
        self._name = name
       
    #Getter method
    def get_name(self):
        return self._name
       
    #setter method
    def set_name(self,name):
        self._name = name
       
       

obj = Person("Ashok")
print(obj.get_name())
#setter
obj.set_name("bob")
print(obj.get_name())

#you can also use property for getter and setter

class Person:
    def __init__(self, name):
        self._name = name  # Use _name to avoid recursion

    @property
    def name(self):
        return self._name  # Return the internal variable

    @name.setter
    def name(self, name):
        self._name = name  # Set the internal variable

# Test
obj = Person("Ameen")
print(obj.name)  # Output: Ameen

obj.name = "Vineet"
print(obj.name)  # Output: Vineet
