#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.9
#Hacker Rank Challenge: https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=false
#Challange: Whats your name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
 str = "Hello "+ first + " " + last + "! You just delved into python."
 print(str)
 

if __name__ == '__main__':
    first = input()
    last = input()
 
print_full_name(first,last)
quit()
