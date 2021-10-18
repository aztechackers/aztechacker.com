#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/17/2021
#Task
#Given an integer,n , and n space-separated integers as input, create a 
#tuple,t, of those n integers. Then compute and print the result of hash(t).
#
#Input
#The first line contains an integer,n, denoting the number of elements in the tuple.
#The second line contains n space-separated integers describing the elements in tuple t.
#
#Tuples:
#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.

#Python hash() function is a built-in function and returns the hash value of an 
#object if it has one. The hash value is an integer which is used to 
#quickly compare dictionary keys while looking at a dictionary.




if __name__ == '__main__':
  n = int(input())
  integer_list = map(int, input().split())

  print(str(hash(tuple(integer_list))))
