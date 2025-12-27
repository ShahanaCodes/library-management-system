#Right triangle star pattern
n = 5
for i in range(1, n+1):
    print("*" * i)


#number pyramid
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
#pyramid pattern
n = 5
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2*i - 1))
    print()

# inverted triangle
n = 5
for i in range(n, 0, -1):
    print("*" * i)
