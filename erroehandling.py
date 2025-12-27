''''#Exception handling
def atm_Withdrwa():
    try:
        balance = 5000
        amount = int(input("enter amount to withdraw: ₹"))

        if amount > balance:
            raise ValueError("insufficient balance.")
        elif amount <= 0:
            raise ValueError("invalid amount. must be greater than 0.")
except ValueError as a:
    print("Error:", a)
else:
     balance -= amount
     print(f"Withdrawl successful. remaining balance: ₹{balance}")

finally:
    print("thank you for using out Atm service.")

#call the function
tm_withdraw()

#exception handling-online shopping
def checkout():
    try:
        cart_total = 3000 #total bill amount
        payment = int(input("Enter payment amount: ₹"))
        if payment < 0:
            raise ValueError("payment cannot be negative.")
        elif payment < cart_toal:
            raise ValueError("insufficient payment. please pay full amount")
        elif payment > 10000:
            raise ValueError("payment limit exceeded! maximum ₹10000")
    except ValueError as e:
        print("Error:", e)
    else:
        change = payment _ cart_total
        print(f"payment successful. change returned:₹{change}")
    finally:
        print("thank you for shopping with us!")
    #call the function
    checkout()'''

# Login system using exception handling

def login_system():
    correct_username = "saha123"
    correct_password = "12345"

    try:
        username = input("Enter your username: ")
        password = int(input("Enter your password: "))

        if username != correct_username:
            raise ValueError("Invalid username.")
        elif password != correct_password:
            raise ValueError("Invalid password.")

    except ValueError as e:
        print("Error:", e)
    else:
        print("Login successful! Welcome", username)
    finally:
        print("Thank you for using our login system.")

# Call the function
login_system()



