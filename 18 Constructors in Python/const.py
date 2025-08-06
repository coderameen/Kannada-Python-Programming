#Case Study 1: Mobile phone call and sms
class MobilePhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_sms(self, number, message):
        print(f"Sending SMS to {number}: {message}")

phone1 = MobilePhone("Samsung", "Galaxy S24 Ultra")
phone2 = MobilePhone("Apple", "iPhone 16")
phone1.call("9876543210")
phone2.send_sms("9876543210", "Hello from iPhone!")

#Case Study 2: Animal make sound
class Animal:
    def __init__(self, name):
        self.name = name
   

    def make_sound(self, sound):
        print(f"{self.name} says: {sound}")

dog = Animal("Dog")
cat = Animal("Cat")
cow = Animal("Cow")

dog.make_sound("Woof! ")
cat.make_sound("Meow! ")
cow.make_sound("Moo! ")
