mypublic_v = 10000
class MyClass:
    mypublic_v = 100
    _myprotected = 500
    __myprivate_v = 1000
    def myfunc(self):
        print("This is function")
        print(self.__myprivate_v)
        
obj = MyClass()
print(obj.mypublic_v)
print(obj._myprotected)
# print(obj.__myprivate_v)

obj.myfunc()
print("------------------------------------------")

class A:
    n = 10
    _n = 100
    __n = 1000  # private

class B(A):
    x = "Hello"
    def myfunc(self):
        print(self.n)           # public
        print(self._n)          # protected
        print(self._A__n)       # accessing private with name mangling =>self._ClassName__ProtectVariable

obj = B()
obj.myfunc()
print(obj._A__n)












