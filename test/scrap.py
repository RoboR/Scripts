import sys, getopt
import os.path


rString = ""
rFile = ""


def main(argv):
    global rString
    global rFile
    
    try:
        opts, args = getopt.getopt(argv,"s:i:",["string=","file="])
    except getopt.GetoptError:
        print 'scrap.py -s <string> -i <inputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--string"):
            rString = arg
        elif opt in ("-i", "--file"):
            rFile = arg
        
if __name__ == "__main__":
    main(sys.argv[1:])


def check_argv():
    global rString
    global rFile
    
    if not rString or not rFile:
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




retval = check_argv()

if (retval > -1):
    retval = check_file()

#if (retval > 0):
    
#if (retval > 0):    

sys.exit(2)
