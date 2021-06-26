"""
    def count_triangle_area(width, height):
    return (width * height / 2)
    print(f'Area of triangle with width 10 and height 8 is {count_triangle_area(10,8)}')
"""
# from geometry.triangle import count_triangle_area
# print(f'Area of triangle with width 10 and height 8 is {count_triangle_area(10,8)}')

# from geometry.triangle as gt
# print(f'Area of triangle with width 10 and height 8 is {gt.count_triangle_area(10,8)}')

from geometry.triangle import count_triangle_area as count_triangle
print(f'The Area of triangle with width 10 and height 8 is {count_triangle(10,8)}')
