#class simple example
'''class student:
    def display(self):
        print(f"my name is {self.name} and i am {self.age}years old")
#create objects
s1= student()
s1.name= "saha"
s1.age=21
s1.display()
s2 = student()
s2.name= "gayu"
s2.age=20
s2.display()

class C_name:
    x=10 + 20
    print(x)
#class creation using init
class student:
    def __init__(self, name, grade):
        self.name =name
        self.grade =grade
        print(f"name:{self.name}, grade:{self.grade}")

#creation objects
student1 = student(name="saha", grade="a")
student2 = student(name="dhara", grade="b")
student3 = student(name="suji", grade="c")
student4 = student(name="gayu", gra0de="d")'''

'''class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color= color
        print(f"{self.color} {self.brand} is starting..")
    def start(self):
        print(f"{self.color} {self.brand} is starting..")
    def stop(self):
        print(f"{self.color} {self.brand} is stoping..")
    def moving(self):
        print(f"{self.brand} {self.color} is moving..")
car1= car("toyota","red")
car2 = car("honda", "blue")
car3 = car("kia", "white")
car4= car("tvs","black")
car1.start()
car2.start()
car2.stop()
car3.stop()
car1.moving()'''
#new
'''class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}, balance = {self.balance}")
        else:
            print("Insufficient balance!")
# Object உருவாக்கம்
acc1 = BankAccount(holder="saha", balance=5000)

acc1.deposit(2000)
acc1.withdraw(7000)'''

'''class Laptop:
    def __init__(self, brand, RAM, price):
        self.brand=brand
        self.RAM=RAM
        self.price=price
    def display(self):
        print(f"{self.brand} {self.RAM} {self.price}")
Laptop1= Laptop("dell", "16", 40,000)
Laptop1.display()'''
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def display(self):
        print(f"brand: {self.brand}")
        print(f"ram: {self.ram} GB")
        print(f"Price: ₹{self.price}")
Laptop1 = Laptop("Dell", 16, 60000)
Laptop2 = Laptop("HP", 8, 45000)
Laptop1.display()


