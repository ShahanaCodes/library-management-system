#pre defined
print(len("hello"))
print(type(123))
print(max(3, 6, 1))

#user defined
def greet(name):
    return f"hello, {name}!"
print(greet("sasi"))

def function_name(fname, lname): #parameter
    print(fname+lname+' '+ "hello world")
function_name(fname: "sasi", lname: "kumar") #arguments
function_name(fname: "arun", lname: "deepan")

def calc(a,b):
    c= a + b
    print(c)
calc(a,10 b,30)
calc(a,50, b,20)

def div(x,y):
     x-=y
     print(x)
div(x: 60, y: 30)
div(x: 30, y: 20)