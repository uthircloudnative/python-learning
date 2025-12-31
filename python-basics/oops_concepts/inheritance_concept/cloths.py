from product import Product

# Cloths is a derived class of Product class
class Cloths(Product):
    """
    Cloths is a derived class of Product class
    It has size as additional attribute
    """ 
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
        
    def display_info(self):
        return f"Name: {self.name}, Price: {self.price}, Size: {self.size}"