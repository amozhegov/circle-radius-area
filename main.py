import math

class AreaCalc:
    # Calculates area of a circle:
    def circle(radius):
        if radius <= 0:
            raise ValueError('Radius must be greateer than 0')
        return f'Area of a circle with radius {radius} is equal to {math.pi * radius ** 2}'
    
    # Calculates area of a triangle:
    def triangle(side_a, side_b, side_c):
        sides = [side_a, side_b, side_c]
        if any(side <= 0 for side in sides):
            raise ValueError('All sides of a triangle must be greater than 0')
        # Check if the triangle is orthogonal
        sides.sort()
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            orthogonal = ''
        else:
            orthogonal = 'not'
        # Area calculation
        p = sum(sides) / 2
        area = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))

        return f'Area of triangle with sides {side_a}, {side_b}, {side_c} is equal to {area}. \nThis triangle is {orthogonal} orthogonal'