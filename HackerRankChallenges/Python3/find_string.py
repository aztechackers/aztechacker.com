#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.9
#Hacker Rank Challenge: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=false
#Challange: Find a string


def count_substring(string, sub_string):
    stringlen = len(string)
    substrlen = len(sub_string)
    subcount = 0
    
    if stringlen >= 1 and stringlen <= 200:
        if sub_string in string:
          for i in range(stringlen):
            if string[i:i+substrlen] == sub_string: 
              subcount += 1
        else:
            subcount = 0
    else:
        quit()
    return subcount

if __name__ == '__main__':
    string = input()
    sub_string = input()
    
    count = count_substring(string, sub_string)
    print(count)

