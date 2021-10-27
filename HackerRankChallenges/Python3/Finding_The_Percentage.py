#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/26/2021
#
#
#
#Task:
#https://www.hackerrank.com/challenges/finding-the-percentage/problem

def contraints_n(n):
    if n >= 2 and n <= 10:
        return True
    else:
         return False

def contraints_scores(scores):
    invalid_score_count = 0
    for i in scores:
        if i < 0 and i > 100:
          invalid_score_count = invalid_score_count + 1
        else:
           invalid_score_count = invalid_score_count + 0

    if invalid_score_count > 0:
        return False
    else:
        return True

def contraints_score_len(query_scores):
    if len(query_scores) == 3:
        return True
    else:
        return False

def get_average_score(query_scores):
    score_sum = 0
    divisor = len(query_scores)
    for i in query_scores:
        score_sum = score_sum + i
    
    average = score_sum / divisor 
    print(format(average, '.2f'))
  
 
if __name__ == '__main__':
   n = int(input())

   if contraints_n(n):
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    query_scores = student_marks.get(query_name)

    if contraints_scores(query_scores) and contraints_score_len(query_scores):
     get_average_score(query_scores)
    else:
      quit()  
   else:
    quit()
