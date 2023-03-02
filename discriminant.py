import math


class discriminant:
    def discr(a, b, c):
        d = b ** 2 - 4 * a * c  # D = b2 – 4ас
        if d == 0:  # х = (-b)/2a
            x = (-1 * b) / (2 * a)
            return x
        elif d > 0:  # х1 = (-b - √D)/2a ,  и  х2 = (-b + √D)/2a
            x1 = (-b - math.sqrt(d)) / (2 * a)
            x2 = (-b + math.sqrt(d)) / (2 * a)
            return x1, x2
        else:
            None
