def range_iter():
    for n in range(10):
        if n % 2 == 0:
            continue
        if n > 6:
            break
        print(n)


#range_iter()

# from lesson7.fibonacci_numbers import with_while_loop
# from lesson7.my_triangle import triangle_type,triangle_are

import random

if __name__=='__main__':
    pass
    # with_while_loop()
    # triangle_area()
    # triangle_type()
    print(random.random())