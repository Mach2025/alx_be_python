# Class creation
class  Product_Catalog:
# function Defination
    def __init__(self,name, price,quantity):
        self.name = name
        self.price = price
        self.quanitiy = quantity


    def total_value(self):
        return int(self.price * self.quanitiy)


# Object creation
Product_Catalog1 = Product_Catalog ("Rice","120","1KG") 
Product_Catalog2 = Product_Catalog ("Beans","350","5KG")   
Product_Catalog3 = Product_Catalog ("Greengrams","670","10KG") 
Product_Catalog4 = Product_Catalog ("UgaliFlour","800","8KG") 
Product_Catalog5 = Product_Catalog ("BlackBeans","600","4KG")   

print(f"{Product_Catalog1.name} total value: {Product_Catalog1.total_value()} KES")
print(f"{Product_Catalog2.name} total value: {Product_Catalog2.total_value()} KES")
print(f"{Product_Catalog3.name} total value: {Product_Catalog3.total_value()} KES")
print(f"{Product_Catalog4.name} total value: {Product_Catalog4.total_value()} KES")
print(f"{Product_Catalog5.name} total value: {Product_Catalog5.total_value()} KES")



        
