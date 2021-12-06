#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version:  3.9.9
#Hacker Rank Challenge: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=false
#Challange: sWAP cASE
#Date: 12/6/2021


def swap_case(s):
 list_c = []

 for i in s: 
     if i.isupper() == False:
         list_c.append(i.upper())
     else:
         list_c.append(i.lower())

 char_string = ''.join(list_c)

 return char_string
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)