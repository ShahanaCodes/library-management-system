'''from abc import ABC, abstractmethod
#Abstract class for discount
class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass

#Different discount strategies
class NoDiscount(Discount):
    def apply(self, price):
        return price
class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price - (price * self.percent / 100)

class FixedAmountDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return price - self.amount if price > self.amount else 0

#product class (uses abstaction)
class product:
    def __init__(self, name, price, discount: Discount):
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self):
        return self.discount.apply(self.price)

    def display(self):
        print(f"product: {self.name}")
        print(f"Original price: ₹{self.price}")
        print(f"Final price after Discount: ₹{self.final_price()}")

p1 = Product(name:"Shoes", price:2000, PercentageDiscount(10))
p1.dispaly()

p2 = Product(name:"bag", price:1500, FixedAmountDiscount(300))
p2.display()

p3= Product(name:"watch", price:2500, NoDiscount())
p3.display

p4 = Product(name:"mobile", price:12000, percentageDiscount(50))
p4.display()'''
from abc import ABC, abstractmethod

# Abstract class for discount
class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass

# Different discount strategies
class NoDiscount(Discount):
    def apply(self, price):
        return price

class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price - (price * self.percent / 100)

class FixedAmountDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return price - self.amount if price > self.amount else 0

# Product class (uses abstraction)
class Product:
    def __init__(self, name, price, discount: Discount):
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self):
        return self.discount.apply(self.price)

    def display(self):
        print(f"\nProduct: {self.name}")
        print(f"Original Price: ₹{self.price}")
        print(f"Final Price after Discount: ₹{self.final_price()}")

# --- Creating product objects ---
p1 = Product(name="Shoes", price=2000, discount=PercentageDiscount(10))
p1.display()

p2 = Product(name="Bag", price=1500, discount=FixedAmountDiscount(300))
p2.display()

p3 = Product(name="Watch", price=2500, discount=NoDiscount())
p3.display()

p4 = Product(name="Mobile", price=12000, discount=PercentageDiscount(50))
p4.display()





