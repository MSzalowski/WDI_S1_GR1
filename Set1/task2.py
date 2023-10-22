def sum_of_digits(number):
  if (isinstance(number, int) == False):
    return 0
  
  absNumber=abs(number)
  sum=0
  while absNumber>0:
    sum+=absNumber%10
    absNumber//=10
  return sum

# Tests
assert(sum_of_digits(0) == 0)
assert(sum_of_digits(1) == 1)
assert(sum_of_digits(123) == 6)
assert(sum_of_digits(333) == 9)
assert(sum_of_digits(3333) == 12)

def digital_root(number):
  sum=sum_of_digits(number)
  while sum>9:
    sum=sum_of_digits(sum)
  return sum

# Tests
assert(digital_root(0) == 0)
assert(digital_root(1) == 1)
assert(digital_root(123) == 6)
assert(digital_root(333) == 9)
# 3333 -> 3+3+3+3 = 12 -> 1+2 = 3
assert(digital_root(3333) == 3)
