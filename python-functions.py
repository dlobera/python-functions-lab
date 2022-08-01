#1

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum


#2

def largest(nums):
  return max(nums)

#3

def occurances(str1, str2):
  return str1.count(str2)

#4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product
