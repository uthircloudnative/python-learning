"""
Product is a base class for all products,
Which has name and price as common attributes
Any class can inherit these attributes and methods from this class
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def display_info(self):
        return f"Name : {self.name}, Price: {self.price}"