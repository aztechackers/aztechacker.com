#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.9
#Hacker Rank Challenge: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=false
#Challange: String Split and Join
#Date:12/06/2021

def split_and_join(line):
    if ' ' in line:
     string_list = line.split( )
     new_string = '-'.join(string_list)
    else:
     string_list = line.split('-')
     new_string = ' '.join(string_list) 


    return new_string
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)