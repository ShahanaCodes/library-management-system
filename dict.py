#create dictionary
student = {
    "name": "shaha",
    "age": 26,
    "city": "chennai",
}
#1. get()
print( student.get("name"))
print( student.get("email")) #no key, so return none

#2.keys()_list type print
print( student.keys())

#3. values()
print( student.values())

#4.items() _tuple form
print( student.items())

#5. update()_new data
student.update({"email": "saha@gmail.com", "city": "pudukkottai","dob" : "jan first"})
print("after updatr:", student)

#6,pop()_specific key-a remove
student.pop("age")
print("after popitems:", student)

#8.setdefault()
student.setdefault("gender", "female")
print("after setdefault:", student)

#9.copy() _duplicate dict.create
new_student = student.copy()
print("copied dict:", new_student)

#10. clear()
student.clear()
print("after clear:", student)

#11.del_specify key delete
del new_student["gender"]
print("after del gender:")

student1= {
    "name": "shaha",
    "age": 26,
    "city": "chennai"
}

for a,b in student1.items():
    print(f"{a}:{b}")# formatting string

    a="hello"
    b= 10
    print(f"{a} {b}")