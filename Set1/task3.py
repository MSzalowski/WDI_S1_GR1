# a * x + b = 0
def linear_equation(a, b):
    if a == 0:
      # If a is 0, then the equation is not linear
        return None
      # x = -b / a
    return -b / a
  
assert(linear_equation(0, 0) == None)
assert(linear_equation(0, 1) == None)
assert(linear_equation(1, 0) == 0)
assert(linear_equation(1, 1) == -1)
assert(linear_equation(2, 4) == -2)
assert(linear_equation(4, 2) == -0.5)

# ax^2 + bx + c = 0
def quadratic_equation(a, b, c):
    if a == 0:
        return linear_equation(b, c)
    # D = b^2 - 4ac
    D = b * b - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return [x1, x2]
      
assert(quadratic_equation(0, 0, 0) == None)
assert(quadratic_equation(0, 0, 1) == None)
assert(quadratic_equation(0, 1, 1) == -1)
assert(quadratic_equation(1, 0, 0) == 0)
assert(quadratic_equation(1, 4, 3) == [-1, -3])
assert(quadratic_equation(1, -4, 3) == [3, 1])
