class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    # def informatiom(self):
    #     return "Rebecca" 
      
    # Object creation
Student1 = Student("Machio", "15")    
Student2 = Student("Collins", "18") 

#Accesing object properties and methods
print(f"{Student1.name} is {Student1.age} years old.")
print(f"{Student2.name} is {Student2.age} years old.")