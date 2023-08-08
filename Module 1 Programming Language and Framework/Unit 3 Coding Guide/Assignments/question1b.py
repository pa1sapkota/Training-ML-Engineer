

'''
Suppose we have a Product class that represents a generic product, and we want to calculate the
total price of a list of products. 

Initially, the Product class only has a price attribute, and
we can calculate the total price of products based on their prices.


Now, let's say we want to add a discount feature, where some products might have a
discount applied to their prices. 


To add this feature, we would need to modify the
existing Product class and the calculate_total_price function, which violates the
Open/Closed Principle. Redesign this program to follow the Open-Closed Principle
(OCP) which represents “Software entities (classes, modules, functions, etc.) should be
open for extension, but closed for modification.”

'''

from abc import ABC, abstractmethod





class Product:
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def calculated_price(self):
        pass

class discountedProduct(Product):
    def __init__(self, price,discount):
        super().__init__(price)
        self.discount=discount
    def calculate_price(self):
        discounted_price = self.price - (self.price * self.discount)
        return (discounted_price)
    

class regularProduct(Product):
    def calculate_price(self):
        return (self.price)



def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price

# Using the calculate_total_price function with a list of products
products = [regularProduct(100),discountedProduct(190,0.2),regularProduct(50)]
total_price = calculate_total_price(products)
print(f"Total Price: {total_price}")