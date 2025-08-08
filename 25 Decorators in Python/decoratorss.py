def decorator(func):
    def wrapper():
        print("Adding some LOC....")
        func()
        print("Adding more LOC...")
    return wrapper
   
@decorator
def func():
    print("HELLOOOOO.....")
   
func()





def ice_cream_toppings(ice_cream):
    def wrapper():
        print("Adding Choco Chips.....")
        ice_cream()
        print("Adding Caramel....")
    return wrapper

@ice_cream_toppings
def ice_cream():
    print("Normal Ice Cream...")
   
# ice_cream()


# res = ice_cream_toppings(ice_cream)
# res()

ice_cream()