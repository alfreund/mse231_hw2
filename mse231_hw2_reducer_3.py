#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 07:46:15 2017

@author: oseasa
"""
import sys
from itertools import groupby
from operator import itemgetter
#from operator import itemgetter


# input comes from STDIN
def read_mapper_output(file,separator='\t'):
    for line in file:
        yield line.rstrip().split(separator,9)
        
def main(separator='\t'):
    data=read_mapper_output(sys.stdin,separator=separator)
    #here I don't use the key from the mapper, but rather the second column
    for date_time, group in groupby(sorted(data,key=itemgetter(0)),itemgetter(0)):
        n_trip=0
        t_occupied=0
        t_onduty=0
        n_pass=0
        n_mile=0
        earnings=0
        drivers_onduty=0
        for item in group:
            date=item[1]
            hour=item[2]
            try:
                drivers_onduty+=1
                t_onduty+=float(item[4])
                t_occupied+=float(item[5])
                n_trip+=float(item[6])
                n_mile+=float(item[7])
                n_pass+=float(item[8])
                earnings+=float(item[9])
            except ValueError:
                pass
        print( "%s\t%s\t%d\t%.4f\t%.4f\t%d\t%d\t%.4f\t%.2f" % (date,hour,drivers_onduty,t_onduty,t_occupied,n_pass,n_trip,n_mile,earnings))
if __name__ == '__main__':
    main()