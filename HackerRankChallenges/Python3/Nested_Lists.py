#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/24/2021
#
#
#
#Task:
#https://www.hackerrank.com/challenges/nested-list/problem

## syntax and gramer module
import ast 

#Operator is a built-in module providing a set of convenient operators.

from operator import itemgetter 

### main function

if __name__ == '__main__': 

 #hold list of of  records name to score
 records = []  
 name_list = []
 #For loop for input take int for input to define range  accepts name followed by score and updates list
 for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])

#first find  min value in the nested list/record based on score records[1]
min_score = min(records, key=itemgetter(1))[1]

#remove records that match min value
new_records = [i for i in records if i[1] != min_score]

#find new min alue in the nested list/record based on score new_records[1]
new_min = min(new_records, key=itemgetter(1))[1]

#create final list that only contains records that have the new min value
final_score_records = [i for i in new_records if i[1] == new_min]

#create new list with names only 
for i in list(zip(*final_score_records))[0]:
         name_list.append([i])

# sort name list
name_list.sort()

#print names line by line but remove brackets and quoates first
for i in name_list:
    n1 = (str(i)[1:-1])
    n2 = ast.literal_eval(n1)
    print(n2)







