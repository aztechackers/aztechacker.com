#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.9
#Hacker Rank Challenge: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=false
#Challange: Mutations

def mutate_string(string, position, character):
    list_chars = list(string)
    list_chars[position] = character
    charstring =''.join(list_chars)
    return charstring

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)