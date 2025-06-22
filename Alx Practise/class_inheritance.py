# class Animal:
#     def __init__(self, name):
#         self.nane = name

#     def make_sound (self):
#             print("Generic animal sound")

# class Dog (Animal):  #Call parent class constructor
#     def __init__(self, name, breed):
#         super().__init__(name) 
#         self.bread = breed

#     def make_sound(self):
#         print("Wooof!")  
# dog = Dog("Buddy","Labrador")
# dog.make_sound()

# class Car:
#   def __init__(self, engine):
#     self.engine = engine  # Engine object as an attribute

#   def start(self):
#     self.engine.start()

# class Engine:
#   def start(self):
#     print("Engine starting...")

# car = Car(Engine())
# car.start()  # Output: Engine starting...

class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

animals = [Dog(), Animal()]
for animal in animals:
  animal.make_sound()  

#Polymorphic Behavior with Duck Typing

#Python uses a concept called “duck typing” to achieve polymorphic behavior. 
# Duck typing emphasizes the object’s behavior over its type or class. 
# It’s based on the idea that “if it looks like a duck and quacks like a duck, then it must be a duck.
class Duck:
    def quack(self):
        return "Duck quacks"

class Person:
    def quack(self):
        return "Person imitates duck"

# Polymorphic behavior using duck typing
def make_sound(obj):
    return obj.quack()

duck_obj = Duck()
person_obj = Person()

print(make_sound(duck_obj))    # Output: "Duck quacks
print(make_sound(person_obj))  # Output: "Person imitates du