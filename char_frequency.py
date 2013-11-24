#!/usr/bin/env python 

import sys
char_freq_dict = {}

def char_frequency(words):
    
    for ch in words:
        if ch in char_freq_dict:
	    char_freq_dict[ch] += 1
	else:
	    char_freq_dict[ch] = 1
    
    
    return (0)


if __name__ =="__main__":
    if len(sys.argv) < 2 or len(sys.argv) >2:
        print 
	print " python char_frequency.py filename"
	print " filename according to you"
	print

    else:
        try:
	    f = open(sys.argv[1])
	    content = f.read()
	    lst_content = content.split()
	    map(char_frequency, lst_content)
	    #print char_freq_dict
            #for key, val in char_freq_dict.iteritems():
            #    print "%s : %s" %(key, val)
            for key in sorted(char_freq_dict.keys()):
                print str(key) ,  ":" ,  str(char_freq_dict[key])
	    
	    char_freq_dict.clear()
            del char_freq_dict

	except:
	    print 
	    print sys.stderr
        
        f.close()

     


    
    
