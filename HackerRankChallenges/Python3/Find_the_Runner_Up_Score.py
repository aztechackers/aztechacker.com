#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/18/2021
#
#
#Task:
#Given the participants' score sheet for your University Sports Day, you are 
# required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.
#
#Input Format:
#The first line contains n . 
# The second line contains an array  A[] of n integers each separated by a space.
#
#Constraints:
# 2 <= n <= 10
# -100 <= A[i] <= 100

#Output Format
#Print the runner-up score

def check_n(n):
    if 2 <= n and n <= 10:
       return True
    else:
       return False

def check_arr(arr):
    counter = 0 
    for i in arr:
       if -100 <= i and i <= 100:
           continue
       else:
         counter = counter + 1   
    if counter == 0: 
        return True
    else:
        return False

def find_runner_up(arr):
    max_score = max(arr)
    new_arr = []
    for i in arr:
       if i != max_score:
           new_arr.append(i)
       else:
           pass
    runner_up_score = max(new_arr)
    return runner_up_score


if __name__ == '__main__':
   n = int(input()) # dont really need this you can do it with out it0
   arr = list(map(int, input().split()))

   if check_n(n) and check_arr(arr):
     print(find_runner_up(arr))
     quit()
   else:
     quit()  




