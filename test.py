'''Reverse a string without using slicing'''
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print(reverse_string("hello"))
'''Find the second largest number in a list'''
def second_largest(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 4, 45, 99]))
'''Count frequency of each character in a string'''
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("banana"))
'''Class Student with name, marks, and display method'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("saha", 90)
s1.display()
'''BankAccount class with deposit, withdraw, and balance-check'''
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print(f"Balance: {self.balance}")

acc = BankAccount("John", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()
'''Check whether a number is prime or not'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(10)) # False

