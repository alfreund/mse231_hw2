#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:10:32 2017

@author: oseasa
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:14:01 2017

@author: oseasa
"""
import sys

def main():

#infile = open("join6.tsv", "r")

    for line in sys.stdin:
        line = line.rstrip('\n')
    
        if (line!=""):
            #line = line.strip()
            line = line.split("\t") #8 columns
            #variables needed in output
            date = line[0]
            hour=line[1]
            #output=c(ID,reducer_2_output.tsv)
            ID=date+hour
            if float(line[3])>1/60:
            #keep only a record of the cab drivers that were active for
            #at least a minute
                print ('\t'.join((ID,('\t'.join(line)))))
    
if __name__ == '__main__':
    main()
