#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/13/2021
#Title: Validating UID
#Description: ABCXYZ company has up to 100 employees The company decides to create 
# a unique identification number (UID) for each of its employees.The company has assigned 
# you the task of validating all the randomly generated UIDs.
#Constraints: A valid UID must follow the rules below:
#  1.It must contain at least 2 uppercase English alphabet characters.
#  2.It must contain at least 3 digits 0-9.
#  3.It should only contain alphanumeric characters.
#  4.No character should repeat.
#  5.There must be exactly 10 characters in a valid UID.
# Input Format: 
#  The first line contains an integer , the number of test cases.
#  The next  lines contains an employee's UID.
# Output Format:
#  For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines

##There must be exactly 10 characters in a valid UID.
def count_tokens(uid, uid_length):

  if len(uid) == uid_length:
      return True
  else:
      return False

#4.No character should repeat.
def unique_tokens(uid, uid_length):
 ut = []
 for i in uid:
   if i not in ut:
       ut.append(i)
 len_ut = len(ut)
 if len_ut == uid_length:
     return True
 else:
     return False

#It should only contain alphanumeric characters.
def alphaNum_tokens(uid):
 isAlphaNumeric = uid.isalnum()
 if isAlphaNumeric:
     return True
 else:
      return False 

#2.It must contain at least 3 digits 0-9
def checkDigit_tokens(uid):
 counter = 0
 
 for i in uid:
    if i.isdigit():
         counter = counter + 1
 if counter >= 3:
     return True
 else: 
      return False           
   
# 1.It must contain at least 2 uppercase English alphabet characters.
def checkUpperCase_tokens(uid):
 counter = 0
 
 for i in uid:
     if i.isupper():
         counter = counter + 1
 if counter >= 2:
     return True
 else: 
      return False 

#### Main ###
if __name__ == '__main__':
 
 uid_length = 10

 num_testcases = int(input())
 uid_list = []

for i in range(0,num_testcases):
 uid = input() 
 uid_list.append(uid)

for i in uid_list:
 ct  = count_tokens(i, uid_length)
 ut  = unique_tokens(i, uid_length)
 at  = alphaNum_tokens(i)
 cdt = checkDigit_tokens(i)
 cut = checkUpperCase_tokens(i)

 if ( not uid ) or (not ct ) or ( not ut ) or ( not at ) or ( not cdt ) or ( not cut ):
     print("Invalid")
 else:
     print("Valid")

quit()


