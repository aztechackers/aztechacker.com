#Author: Jessi Cardoso
#Org: aztechacker.com
#Python version: 3.9.7
#Date: 10/19/2021
#
#
#Task:
#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# 12: 00: 00PM on a 12-hour clock is 12: 00: 00 on a 24-hour clock..
#
#Input Format:
#Complete the timeConversion function in the editor below. 
# It should return a new string representing the input time in 24 hour format.
#timeConversion has the following parameter(s):
#string s: a time in 12hour format
#A single string  that represents a time in 12-hour clock format 
# (i.e. hh:mm:ssAM or hh:mm:ssPM).
#07: 05: 45PM
#Constraints:
#All input times are valid

#Output Format
#19:05:45


import math
import os
import random
import re
import sys


def timeConversion(s):
 Pmeridiem = "PM"
 Ameridiem = "AM"
 inputTime = s.split(':')
 newTime = ""

 
 if Pmeridiem in s:
     if (inputTime[0]) == "12":
         hh = 12
     else:
         hh = int(inputTime[0]) + 12

     mm = inputTime[1]
     ss = inputTime[2].replace("PM","")
     newTime = str(hh) + ":" + mm + ":" + ss
 elif Ameridiem in s:
     if inputTime[0] == "12":
         hh = "00"
     else:
         hh = str(inputTime[0])
     
     mm = inputTime[1]
     ss = inputTime[2].replace("AM", "")
     newTime = hh + ":" + mm + ":" + ss
      
 print(newTime)
 return newTime

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
