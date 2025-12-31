from product import Product

# Electronics is a derived class of Product class
class Electronics(Product):
    """
    Electronics is a derived class of Product class
    It has warranty as additional attribute
    """
    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty = warranty
        
    def display_info(self):
        return f"Name: {self.name}, Price: {self.price}, Warranty: {self.warranty}"