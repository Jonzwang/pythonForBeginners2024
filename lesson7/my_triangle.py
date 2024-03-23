def triangle_type(a=3, b=4, c:int=5):
    print(f"{a=}, {b=}, {c=}")
    if a == b and b == c and c == a:
        _type = 'Equilateral'
    elif a != b and b and b !=c and c != a:
        _type = 'scalene'
    else:
        _type = 'isosceles'
    print(f"The triangle type is '{_type}'")

def triangle_area(a=3, b=4, c=5):
    s = 0.5 * (a + b + c)
    ls = s * (s - a) * (s - b) * (s-c)
    print(f"{a=}, {b=}, {c=}, {s=}, {ls=}")
    area = ls ** .5
    print(f"The triangle's area is '{area}'")


def valid_triangle(a=3, b=4, c=5):
    return a+b>c and b+c>a and c+a>b


if __name__ == '__main__':
    count = 0
    limit = 5
    while count < limit:
        a, b, c = float(input("a=")), float(input("b=")), float(input('c='))
        if valid_triangle(a, b, c):
            triangle_type(a, b, b)
            triangle_area(a, b, c)
        else:
            print(f"this is not a valid triangle")
        count += 1

# triangle_type()
# triangle_type(4, 4, 4)
# triangle_type(4, 4, 5)
# triangle_type(4, 5, 11)
#
# triangle_type()
# triangle_type(4, 6, 6)
# triangle_type(4, 5, 9)