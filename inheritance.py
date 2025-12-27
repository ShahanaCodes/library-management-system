#single level inheritance
'''class father:
    def bike(self):
        print("father ku oru her honda bike")
class son(father):
    def mobile(selfself):
        print("son ku iphone")
s = son()
s.bike()
s.mobile()'''

#multiple inheritance
'''class Mother:
    def cooking(self):
        print("mother knows cooking")
class father:
    def driving(self):
        print("father knows driving")
class Gfather:
    def land(self):
        print("Gfather have land")
class son(Mother, father, Gfather):
     def dancing(self):
         print("child knows dancing")
s = son()
s.cooking()
s.driving()
s.land()
s.dancing()

#multilevel inheritance
class a:
    def land (self):
        print("grand father land")
class b(a):
    def house(self):
        print("father house")
class c(b):
    def bike(self):
        print("son bike")
class d(c):
    def scooty(self):
        print("daughter scooty")
s= d()
s.land()
s.house()
s.bike()'''

#new example
'''class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def login(self):
        print(f"{self.name} logged in with {self.email}")

    def logout(self):
        print(f"{self.name}logged out")

U= User("gayu", "gayu@gmail.com")
U.login()
U.logout()'''

'''class Customer(User):
    def __init__(self, name, email):
        super().__init__(name, email)#parent constructor calling
        self.cart =[]
    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product} added to {self.name}'s cart")
    def place_order(self):
        print(f"{self.name} placed order for: {', '.join(self.cart)}")
C= Customer("dhara", "dhara@gmail.com")
C.add_to_cart("dress")
C.add_to_cart("lipstick")
C.place_order()'''

#child class-savings account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
            interest = self.balace * self.interest_rate / 100
            self.balance += interest
            return f"Interest added: ₹{interest}. new balance: ₹{self.balance}"
#child class _ current account
class CurrentAccount(BankAccount):
    def __init__(self, account_holder,balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return f"withdrawn ₹{amount}. new balance: {self.balance}"
        else:
            return "Overdraft limit exceded"

        #savings Account
        Savings = SavingsAccount(account_holder:"shahana",balance:3000, interest_rate)
        print(savings.deposit(2000))
        print(savings.add_interest)

        #current account
        curent = currentAccount(account_holder:"sahana")






