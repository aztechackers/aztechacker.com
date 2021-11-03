#----------------------------------------------------------------------------------
# Script: RubyTest.rb
# Auther: Jessi Cardoso
# Created: 12/15/2015
# Description:
# This script is intended demostrate Ruby scripting knowledge and skills
# and fullfills the below requirements
# 1.Create New directory
# 2.Fill the directory with 20 files having .json extension and have at least 4
# top level fields of which one is "version" with format Major.Minor.Revision.Build
# 3.Create another new directory
# 4.Copy files from one directory to the other
# 5.Rename the new files to GUID's with json extentions
# 6.Edit the version fields Build value to be +1(increase build number by 1)
#----------------------------------------------------------------------------------


require 'fileutils'    # fileutils gem required for file handling
require 'json'         # json gem required for creating and manipulation json hashes
require 'securerandom' # securerandom gem required to generate random/unique GUID's



mainDir='/Users/jessicardoso/Desktop'                 #variable that stores directory we are working in
intDIRNAME='/Users/jessicardoso/Desktop/InitialDir'   #variable that stores intial directory to create
finDIRNAME='/Users/jessicardoso/Desktop/FinalDir'     #variable that stores final directory to create
FILECOUNT=20                                          #variable that stores number files to create
Index=0                                               #variable used as an index/counter for different functions

class CreateDirFiles                                  #CreateDirFiles class created to fullfill reqs# 1,2
   def initialize(directory,filecounts,index)        #method 'initialize' definition used to intialize and set variables in class
       @directory=directory
       @filecount=filecounts
       @i=index
   end                                                #end of intialize method

   def CrtIntDir                                      #method 'CrtIntDir' definition used to full reqs# 1,2
       puts "----Creating--First--Directory---"
       Dir.mkdir(@directory) unless File.exists?(@directory)   #New Directory created from passed parameter to class
       puts "Directory #{@directory} created!"
       puts "-------Creating---Files---------"

       while @i < @filecount                         #while loop begins, changes working directory to one created and creates files
            Dir.chdir @directory
            fileName="JSONfile" + @i.to_s + ".json"  #variable storing unique file name (non GUID), with '.json' extension
            File.new("#{fileName}", 'w')             #create new file in current working directory


            id=@i                                    #set variable 'id' = @i will be used to create file id's
            tempHash = {                             #declare\create JSON hash and levels
            "id"=>@i,
            "version"=>"1.0.0.1",
            "company"=>"BottleRocket",
            "Script"=>"DevOpsTest"
            }                                        #end of JSON hash declaration
            File.open("#{fileName}", 'w') do |f|     #write JSON hash to newly created file in current directory
               f.write(tempHash.to_json)
            end                                      #end of JSON file write

            puts "File #{fileName} created!"
            @i+=1                                    #increment local counter/index
        end                                          # end of while loop
     end                                             #end of CrtIntDir Method
 end                                                 #end of CreateDirFiles class

class CreateDirFinal                                 #CreateDirFinal class created to fullfill reqs# 3,4,5,6
   def initialize(directory1,directory2,mnDir)       #method 'initialize' passed parameter to class
       @directory1=directory1
       @directory2=directory2
       @mdDir=mnDir
   end                                               #end of 'initialize' method

   def CrtFinDir                                     #method CrtFinDir used to complete work for reqs# 3,4,5,6
       Dir.chdir @mdDir                              #change directory to main working directory
       puts "----Creating--Final--Directory---"
       Dir.mkdir(@directory2) unless File.exists?(@directory2)   # create final directory in current main directory
       puts "Directory  #{@directory2} created!"

       srcDir=@directory1 << '/.'                                #variable holds source file path/file locations to copy from
       FileUtils.cp_r(srcDir, @directory2)                       #copy files from intial directory to newly created final directory
       puts "File Copy Complete!!!"


       puts "---Renaming Files to have a GUID scheme---!"
       Dir.chdir @directory2                                    #change directory to newly created final directory to begin file work
       files=@directory2 << '/*'                                #variable declareing to use all files in directory
       Dir.glob(files).sort.each do |file|                      #begin iterating and renaming each file in directory using File.rename function
        File.rename(file,SecureRandom.uuid+".json")             #files renamed to have a random unique GUID with .json extenstion
       end                                                      #end file rename

       Dir.glob(files).each do |file|                          #begin iterating through each file in directory for JSON file changes
         puts "--Updating #{file} Build Number-- "
         jsonFile = File.read(file)                            #variable used store current jsonFile being worked
         hash = JSON.parse(jsonFile)                           #get hash information from current json file
         version=hash["version"]                               # get version field and store the information in version variable
         arrayVersion = version.split('.')                     #split version string by '.' and create array for manipulation
         vMajor=arrayVersion[0].to_i                           #assign version attributes to variables and convert to integer type
         vMinor=arrayVersion[1].to_i
         vRevision=arrayVersion[2].to_i
         vBuild=arrayVersion[3].to_i + 1                                                #increase build number by 1 and store in build variable
         newVersion = "#{vMajor}" +"."+"#{vMinor}"+"."+"#{vRevision}"+"."+"#{vBuild}"   #combine version attributes into one variable
         hash["version"]="#{newVersion}"                     #assign 'version' field from hash new version number

         File.open(file, 'w') do |f|                         #update file with new version hash
                 f.write(hash.to_json)
          end                                                #end writing updated json to file
       end                                                   #end making changes to file
         puts "---All Work Complete!!!---"
   end                                                       #end of CrtFinDir method
end                                                          #end of CreateDirFinal class

CID=CreateDirFiles.new(intDIRNAME,FILECOUNT,Index)           #declare new instance of CreateDirFiles Class with parameters
FID=CreateDirFinal.new(intDIRNAME,finDIRNAME,mainDir)        #declare new instance of CreateDirFinal Class with parameters

CID.CrtIntDir                                                # call method CrtIntDir from CreateDirFiles Class to begin work on reqs# 1,2
FID.CrtFinDir                                                # call method CrtFinDir from CreateDirFinal Class to complete work on reqs# 3,4,5,6
