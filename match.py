'''day = input("enter a day:")
match day: #match keyword day vanthu variable name expression nu sluvaanga
    case "monday":
        print("start of the week")
    case "friday":
        print("weekend is coming")
    case "sunday":
        print(" happy holiday!")
    case _: #underscore invalid ku use pannuvom
        print("normal day")'''

'''choice = input("enter operation (+, -, *, /, %, //):")
a= int(input("enter first number: "))
b = int(input("enter second number:"))
match choice:
    case "+":
        print("result:", a + b)
    case "-":
        print("result:", a - b)
    case "*":
        print("result:", a * b)
    case "/":
        print("result:", a / b if b != 0 else "division by zero not allowed") #condition use panniruko
    case "%":
        print("result:", a % b)
    case "//":
        print("result:", a // b)
    case _:
        print("Invalid operation")'''
marks = int(input("enter a mark :"))
match marks:
    case m if m>100 or m< 0:
        print("invalid mark")
    case m if m >=90:
        print("grade A")
    case m if m>=70:
        print("grade B")
    case m if m>=50:
        print("grade c")
    case m if m>=40:
        print("grade average")
    case _:
        print("fail")

