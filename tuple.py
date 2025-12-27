t= (1, 2, 3)
print(type(t))

t= (101, "shahana", 99.9, True, [1,2], {"key": "value"})
print(t)

t=(1, 2, 2, 3, 1, "a", "a")
print(t)
print(t.count(1))
print(t.count("a"))

t= ("a", "b", "c", "d")
print(t[0])

a= ("apple", "banana", "cherry", 10, 20)
for fruit in A:
    print(fruit)

    t=(1,8,2,3,5,2,3)
    s=("apple", "ball","cat","apple","ball","cat")
    print(t.count(2))
    print(s.index("cat"))
    print(t.count(10))

#unpacking
t= 1, "hello", 3.14,"indhu",18,43
a, b,c, d, e,f=tprint(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#if we want to change the tuple items we have
t= (1,2,3) #tuple
temp= list(t)
temp[0]=100
t= tuple(temp)
print(t)

#set.py
my_set = {3000, 4,5,5,7,8,0,3,299}
print(my_set)
my_set.clear()
print(my_set)
new_set = {"shaha","shaha","gay","suji","dhara","hema","leela","akalu"}
print (new_set)
new_set.pop()
print(new_set)
my_set = {"apple", "bananana", "cherry"}
for item in my_set:
    print(item)

a={1,2,3}
b={3,4,5}
print(a | b) #union
print(a & b) #intersection
print(a - b) #Difference
print(a ^ b) #symetric diffrence
