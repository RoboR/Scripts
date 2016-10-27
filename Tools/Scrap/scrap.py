'''
RoboR works

e.g. to run the script:
    scrap.py -i com.txt -b COM -e :

'''

import sys, getopt
import os.path
import re
  



class Scrap:
    '''
    The priority of accepting arguments is as the order of this
    will not check duplicate arguments
    '''
    methods = dict(
        WORD_WHOLE = 1,
        WORD_EDGES = 2,
        WORD_BEGIN = 3,
        WORD_ENDIN = 4
    )    
        
    rString = ""
    rFile = ""
    rStrBegin = ""
    rStrEnd = ""
                
    
        
        
    def __init__(self):        
        try:
            opts, args = getopt.getopt(sys.argv[1:],"s:i:b:e:",["string=","file=","begin=","end="])
        except getopt.GetoptError:
            print 'scrap.py -s <string> -i <inputfile>'
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-s", "--string"):
                self.rString = arg
            elif opt in ("-i", "--file"):
                self.rFile = arg
            elif opt in ("-b", "--begin"):
                self.rStrBegin = arg
            elif opt in ("-e", "--end"):
                self.rStrEnd = arg
        
        self.scrap_main()
 
                
    def check_argv(self):     
        if not self.rFile or not (self.rString or self.rStrBegin or self.rStrEnd):
            print "USAGE: scrap.py -s <string> -i <inputfile>\n"
            print "scrap.py -h for more info"
            return -2      
            
        return 1
           
           
    def check_file(self):        
        if os.path.exists(self.rFile):
            return 1
        else:
            print "No File Found"
            return -1


    def scrap_file(self):
        fp = open(self.rFile, "r")
        
        for line in fp:
            self.scrap_line(line);
                
                
    def scrap_line(self, line):
        letter = list(line)
        word = ""
                
        for l in letter:
            if (l != ' ' and l != '\n'):
                word += l
            else:
                if (word != ""):
                    if (self.rString != ""):
                        self.scrap_word(word, self.methods['WORD_WHOLE'])
                    elif (self.rStrBegin != "" and self.rStrEnd != ""):
                        self.scrap_word(word, self.methods['WORD_EDGES'])
                    elif (self.rStrBegin != ""):
                        self.scrap_word(word, self.methods['WORD_BEGIN'])
                    elif (self.rStrEnd != ""):
                        self.scrap_word(word, self.methods['WORD_ENDIN'])
                        
                    word = ""                
                
                
    def scrap_word(self, word, state):
        if (state == self.methods['WORD_WHOLE']):
            if (re.search(self.rString, word)):
                print word
                
        elif (state == self.methods['WORD_EDGES']):
            regex = "(" + self.rStrBegin + "\S*?)"+ self.rStrEnd    
            match = re.search(regex, word)
            
            if (match):
                print match.group(1)
                
        elif (state == self.methods['WORD_BEGIN']):
            regex = "(" + self.rStrBegin + "\S*?$)"
            match = re.search(regex, word)
            
            if (match):
                print match.group(1)           
                
        elif (state == self.methods['WORD_ENDIN']):
            regex = "(" + "^\S*?"+ self.rStrEnd + ")"
            match = re.search(regex, word)
            
            if (match):
                print match.group(1)    
                
                
    def scrap_main(self):
        retval = self.check_argv()
                        
        if (retval > -1):
            retval = self.check_file()
            
        if (retval > 0):
            self.scrap_file()


'''
here is MAIN
'''


sp = Scrap()

