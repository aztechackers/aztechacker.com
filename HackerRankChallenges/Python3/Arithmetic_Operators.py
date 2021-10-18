#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/17/2021
#
#
#
#The provided code stub reads two integers from STDIN, a and b .
# Add code to print three lines where:
# 1.The first line contains the sum of the two numbers.
# 2.The second line contains the difference of the two numbers(first - second).
# 3.The third line contains the product of the two numbers.
#
#The first line contains the first integer, a.
#The second line contains the second integer, b.
#Constraints 
# 1 <= a <= 10**10
# 1 <= b <= 10**10

def const_check(a,b):
  if a < 1 or b < 1:
      return False
  elif a > 10**10 or b > 10**10:
      return False
  else:
      return True  
    

if __name__ == '__main__':
  a = int(input())
  b = int(input())

  add = a + b
  diff = a - b
  prod = a * b
  
  if const_check(a,b):
     print(add)
     print(diff)
     print(prod)
     quit()

  else:
      quit()




