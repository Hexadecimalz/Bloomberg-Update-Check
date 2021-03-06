#!/usr/bin/env python3
import time
from urllib.request import urlopen
import os
import sys
'''
Title: Bloomberg Terminal Update Check
Python 3.8.2 Linux / Windows / macOS
This code will check the Bloomberg Software Website to see if an update has been released
for an existing terminal installation. Updates can be released randomly, sometimes it's helpful
to get ahead of the update, and Bloomberg releases links using a standard format. This code
will cycle through all 31 days of all months, even months without 31 days. A file is created
when the update is found, and the code will not produce a result again until the next month.
You could program the script to e-mail you of pertinent changes very easily, or for a task
to download the file to be distributed through the network.
'''
#Checks if a URL returns True or False
def checkurl(url):
    try:
        urlopen(url)
        return True
    except:
        return False
    
#Check if a file is real
def checkfile(file):
    try:
        if os.path.exists(file) == True:
            return True
    except:
        return False
    
#Computers are stupid, figure out where the hell I am
def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def main(argv):
    #Where the script is
    dir = getScriptPath()
    #Predefined URL bits from Bloomberg
    urlstart = "https://bdn-ak-ssl.bloomberg.com/software/trv/upgr"
    urlend = ".exe"
    #Below extracts the pertinent bits of date to get what we need
    date = (time.strftime("%m/%Y"))
    month = date[0:2]
    year = date[3:7]
    #Loop through all 31 days and see if Bloomberg released an update
    for x in range(1, 32):
        day = str(x)
        if len(day) < 2:
            day =  "0" + str(x)
        else:
            day = str(x)
        fulldate = month + day + year
        fullurl = urlstart + fulldate + urlend
        print (fullurl)
        if checkurl(fullurl) == True:
            if checkfile(dir+os.sep+fulldate) != True:
                f= open(fulldate,"w+")
                f.close()
                return True

if __name__ == "__main__":
    if main(sys.argv) == True:
        print ("An update is found!")
