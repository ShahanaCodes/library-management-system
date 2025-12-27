'#lambda arguments: expresssion
#lambda
add= lambda x, y: x + y
print(add(3, 5))

#lambda
'''users = [
    {"name": "indhumathi", "age":25}
    {"name": "rahul", "age": 300}
    {"name": "karthik", "age": 28}
]
#sort users by age using lambda
sorted_users = sorted(users, key=lambda post: post["name"])

for p in sorted_users:
    print(p)
#lambda expression
emails = [
    "sha@gmail.com"
    "arun@gamil.com"
    "dharangmail.com"
    "sasigmail.com"
]
#filter valid emails using lambda
valid_emails=list(filter(lambda email: "@" in email, emails))

print(valid_emails)

#not using lambda
def is_valid_email(email):
    return "@" in email
emails =["A@gmail.com", "invalidgmail.com", "emailsAgmail.com"]

valid_emails =list(filter(is_valid_email, emails))
print(valid_emails)

def is_sorted_users(users):
    return users == sorted(users)
users = [24,5,89]

sorted_users = sorted(users)
print(sorted_users )'''