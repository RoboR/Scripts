'''
RoboR works

Task:
    - Change it to a class
    - scrap_word() scrap_word_BeEnd() change to onlly a single function, and use
    a Switch case, add an argument to check
    - Add remaining scrap_word case

'''

import sys, getopt
import os.path
import re


rFile       = ""
rString     = ""
rStrBegin   = ""
rStrEnd     = ""


def main(argv):
    global rString
    global rFile
    global rStrBegin
    global rStrEnd
    
    try:
        opts, args = getopt.getopt(argv,"s:i:b:e:",["string=","file=","begin=","end="])
    except getopt.GetoptError:
        print 'scrap.py -s <string> -i <inputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--string"):
            rString = arg
        elif opt in ("-i", "--file"):
            rFile = arg
        elif opt in ("-b", "--begin"):
            rStrBegin = arg
        elif opt in ("-e", "--end"):
            rStrEnd = arg
        
if __name__ == "__main__":
    main(sys.argv[1:])


def check_argv():
    global rString
    global rFile
    global rStrBegin
    global rStrEnd
    
    if not rFile or not (rString or rStrBegin or rStrEnd):
        print "USAGE: scrap.py -s <string> -i <inputfile>\n"
        print "scrap.py -h for more info"
        return -2      
    
    return 1


def check_file():
    global rFile
    
    if os.path.exists(rFile):
        return 1
    else:
        return -1


def scrap_file():
    #print "Scrapping....."
    fp = open(rFile, "r")
    
    for line in fp:
        scrap_line(line);
        
        
def scrap_line(line):
    letter = list(line)
    word = ""
            
    for l in letter:
        if (l != ' ' and l != '\n'):
            word += l
        else:
            if (word != ""):
                if (rString != ""):
                    scrap_word(word)
                elif (rStrBegin != "" and rStrEnd != ""):
                    scrap_word_BeEnd(word)
                elif (rStrBegin != ""):
                    #scrap_word(word)
                    print "It is the beginning"
                elif (rStrEnd != ""):
                    #scrap_word(word)
                    print "THE END"
                    
                word = ""


def scrap_word(word):
    if (re.search(rString, word)):
        print word

def scrap_word_BeEnd(word):
    global rStrBegin
    global rStrEnd
    
    regex = "(" + rStrBegin + "\S*?)"+ rStrEnd    
    match = re.search(regex, word)
    
    if (match):
        print match.group(1)





    
retval = check_argv()

if (retval > -1):
    retval = check_file()

if (retval > 0):
    scrap_file();
    
#if (retval > 0):    

sys.exit(2)
