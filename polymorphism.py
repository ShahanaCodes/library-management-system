
#duck typing
'''class Cat():
   def speak(self):
     print("Cat Sound")
class Dog():
  def speak(self):
    print("Dog Sound")
class common():
   def person(self,name):
    name.speak()
c = Common()
a = Cat()
b= Dog()
c.person(b)
c.person(a)'''

'''class Pycharm:
    def execute(self):
        print("Running code in Pycharm")
class VScode:
    def execute(self):
        print("Running code in VScode")
class Programmer:
    def coding(self, ide):
        ide.execute()
ide1= Pycharm()
ide2 =VScode()

p = Programmer()
p.coding(ide1)'''

'''class PayPal:
    def pay(self, amount):
        return f"paid ₹{amount} using credit card."
#credit card payment
class CreditCard:
    def pay(self, amount):
        return f"paid ₹{amount}using Credit card."
#upi payment
class UPI:
    def pay(self, amount):
        return f"paid ₹{amount}using UPI."
#paypal payment
#function using duck typing
def checkout(Payment_method, amount):
    print(Payment_method.pay(amount))
#usage
credit = CreditCard()
upi = UPI()
paypal = Paypal()

checkout(credit, amount:,100)
checkout(upi, amount:200)
checkout(paypal, amount:1000)


#*args
class Add():
    def Numbers(self,*args):
    total= sum(args)
    print("sum is", total)
d = add()
d.numbers(*args:,4,6,7,8,9,10)'''

#**kwargs
'''class person():
    def library(selfself,**Kwargs):
        #print(kwargs)
       for key, value in Kwargs.items() :
           print(f"{key}={value}")
p= person()
p.library()
p.library(name="indhu",age=26)
p.library(department="cs",city="pudukkottai", name="saha",cname="lcm")'''

#overloading
class book:
    def __init__(self,pages) :
        self.pages = pages
    def __add__ (self,others):
        return self.pages + others.pages
b1 = book(200)
b2 =book(300)
print(b1 + b2)


#sub
'''class Account:
    def __init__(self, balance):
        self.balance = balance
    def __sub__(self,other):
        return self.balance - other.balance
a1 = Account(1000)
a2 = Account(500)
print(a1 - a2)

#overriding
class Employee:
    def __init__(self, name, base_salary):'''
