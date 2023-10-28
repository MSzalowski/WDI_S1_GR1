def GCD(a, b):
  if a == 0:
      return b
  elif b == 0:
      return a
  elif a >= b:
      return GCD(a % b, b)
  else:
      return GCD(a, b % a)

def LCM(a, b):
  if (a == 0 or b == 0):
    return 0
  return a * b / GCD(a, b)

# Tests
# GCD
assert(GCD(0, 0) == 0)
assert(GCD(0, 1) == 1)
assert(GCD(1, 0) == 1)
assert(GCD(1, 1) == 1)

assert(GCD(2, 2) == 2)
assert(GCD(2, 4) == 2)
assert(GCD(4, 2) == 2)

assert(GCD(124, 48) == 4)

# 2-2
# 3-4