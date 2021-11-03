#Author:Jessi Cardos0
#Date:03/28/2018
#Description: Takes CSV File was Input and  and columname and sums column
#Usage: csvsum.py -f <csvfile> -c <csvcolumname>


import sys
import getopt
import csv
import os
import os.path


csvinput = ""
colinput = ""
totalsum = 0.0

#function that evaluates input and sums up values in a field

def getsum():

  global totalsum
  global csvinput
  global colinput

 # check if file is valid/exists if so continue else throw error message and exit
  if os.path.isfile(csvinput):

 # if file exists begin evaluating supplied field if exists as header
   with open(csvinput,"rb") as h:
    hdreader = csv.reader(h)
    hdr = next(hdreader)
    h.close()
 # if supplied field to sum is in the header try reading the values to sum else throw
 # error messege and exit
    if colinput in (hdr):
     try:
      with open(csvinput,"rb") as f:
       reader = csv.DictReader(f)
       for r in reader:
        value = r[colinput]
 # check value in field is a float or not if not throw error
        vf = isinstance(float(value), float)

        if r[colinput] in (None,""):
           r = 0.0
           totalsum += r
        else:
           totalsum += float(r[colinput])
      f.close()
      print ("Field", colinput ," Total Sum:", totalsum)
     except ValueError:
      print("ERROR Field:" , colinput," contains non numerical values")
      sys.exit()
    else:
      print ("ERROR Invalid Field: " ,colinput)
      sys.exit()
  else:
    print ("ERROR File:" , csvinput, "missing or invalid")
    sys.exit()

# main function takes input and assigns variable values
def main():
  helpmsg = "csvsum.py -f <csvfile> -c <csvcolumname>"
  global csvinput
  global colinput
  try:
    opts, args = getopt.getopt(sys.argv[1:],'h:f:c:')
  except getopt.GetoptError:
     print (helpmsg)
     sys.exit(2)
  for opt,arg in opts:
     if opt == '-h':
        print ("Usage: ", helpmsg)
        sys.exit()
     elif opt == '-f':
        csvinput = arg
     elif opt == '-c':
        colinput = arg
     else:
      print ("Invalid Option")
      sys.exit()


main()
print ("*****CSV FIELD SUM ****")
print ("CSV file:" , csvinput)
print ("Field to Sum:", colinput)
getsum()
