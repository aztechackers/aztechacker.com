#Author:Jessi Cardoso 
#Date: 03/28/2018
#
#Description: Gets Access Logs error codes 
#Usage: geterrorcode.py -f <accesslogfile>


import sys
import getopt
import os
import os.path
import re
import string
import collections

loginput = ""
clienterrorlist = [" 400 "," 401 ", " 402 "," 403 "," 404 "," 405 "," 406 "," 407 "," 408 "," 409 "," 410 "," 411 "," 412 "," 413 "," 414 "," 415 "," 416 "," 417 "," 418 "," 421 "," 422 "," 423 "," 424 "," 426 "," 428 "," 429 "," 431 "," 451 "]
servererrorlist = [" 500 "," 501 "," 502 "," 503 "," 504 "," 505 "," 506 "," 507 "," 508 "," 510 "," 511 "]
errcodecount=0
#function that evaluates input and sums up values in a field

def getcount():
  global loginput
  global clienterrorlist
  global servererrorlist
  global errcodecount
 # check if file is valid/exists if so continue else throw error message and exit 
  if os.path.isfile(loginput):
   try:
      for code in clienterrorlist:
       cmd = "grep -c " +code+ " " +loginput
       errcodecount = int(os.popen(cmd).read())
       if errcodecount != 0:
        print("Error Code:" , code, "Count:", errcodecount)
       else:
        pass 
      for code in servererrorlist: 
       cmd = "grep -c " +code+ " " +loginput
       errcodecount = int(os.popen(cmd).read())
       if errcodecount != 0:
        print("Error Code:" , code, "Count:", errcodecount)
       else:
        pass
   except ValueError:
     print("ERROR")
     sys.exit()
  else:
    print ("ERROR File:" , loginput, "missing or invalid")
    sys.exit()

# main function takes input and assigns variable values
def main():
  helpmsg = "geterrorcode.py -f <accesslogfile> "
  global loginput

  try:
    opts, args = getopt.getopt(sys.argv[1:],'h:f:')
  except getopt.GetoptError:
     print (helpmsg)
     sys.exit(2)
  for opt,arg in opts:
     if opt == '-h': 
        print ("Usage: ", helpmsg)
        sys.exit()
     elif opt == '-f': 
        loginput = arg
     else:
      print ("Invalid Option")
      sys.exit()


main()
print ("****Accesslog Common Error Codes*****")
print ("Access log file:" , loginput)
getcount()
