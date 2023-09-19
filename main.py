import math

class AreaCalc:
    @staticmethod
    def figure(*args):
        num_args = len(args)
        if num_args == 1:
            # Calculates area of a circle:
            radius = args[0]
            if radius <= 0:
                raise ValueError('Radius must be greater than 0')
            area = math.pi * radius ** 2
            return area        
        elif num_args == 3:
             # Calculates area of a triangle:
            sides = list(args)
            if any(side <= 0 for side in sides):
                raise ValueError('All sides of a triangle must be greater than 0')
            # Check if the triangle is orthogonal
            sides.sort()
            # Area calculation
            p = sum(sides) / 2
            area = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

            return area
        # Figure other than a circle or a triangle
        else:
            raise ValueError('Invalid number of arguments. Supported shapes: circle (1 argument), triangle (3 arguments)')
    @staticmethod
    def is_triangle_orthogonal(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2 


