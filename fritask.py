'''def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)
right_triangle(5)'''

'''def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)
inverted_right_triangle(5)'''


def number_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
number_pyramid(5)

def pyramid_pattern(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * (2*i - 1))
pyramid_pattern(5)





