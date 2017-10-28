#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 07:46:15 2017

@author: oseasa
"""
import sys

from datetime import datetime
from itertools import groupby
from operator import itemgetter


# input comes from STDIN
def read_mapper_output(file,separator='\t'):
    for line in file:
        yield line.rstrip().split(separator,10)
        
def main(separator='\t'):
    data=read_mapper_output(sys.stdin,separator=separator)
    #here I don't use the key from the mapper, but rather the second column
    for driver_time, group in groupby(sorted(data,key=itemgetter(1)),lambda x:x[1]):
        n_trip=0
        t_occupied=0
        t_onduty=1
        n_pass=0
        n_mile=0
        earnings=0
        for item in group:
            try:
                n_trip+=1 #number of trips
                #get hours of the drop and pick-up times for the trip
                n_pass+=int(item[8])
                start_time = datetime.strptime(item[3], '%Y-%m-%d %H:%M:%S')
                end_time= datetime.strptime(item[4], '%Y-%m-%d %H:%M:%S') 
                #helps to determine how to split the t_occupy values
                current_time=datetime.strptime(item[2], '%Y-%m-%d %H:%M:%S')
                if int(end_time.strftime('%H'))!=int(start_time.strftime('%H')):
                    if int(end_time.strftime('%H'))>int(current_time.strftime('%H')):
                    #the time should only be from start to next hour
                        t_occupied= (end_time.replace(second=0,minute=0)- start_time).seconds/(60**2)+t_occupied
                        #needs to be multiplied
                        fraction=((end_time.replace(second=0,minute=0)- start_time).seconds)/((end_time-start_time).seconds)
                        n_mile+=float(item[7])*fraction
                        earnings+=float(item[5])*fraction
                    else:
                    #from start of hour till the end of the ride
                        t_occupied= (end_time-end_time.replace(second=0,minute=0)).seconds/(60**2)+t_occupied
                        fraction=((end_time-end_time.replace(second=0,minute=0)).seconds)/((end_time-start_time).seconds)
                        n_mile+=float(item[7])*fraction
                        earnings+=float(item[5])*fraction
                else:
                    t_occupied=t_occupied=(end_time-start_time).seconds/(60**2)+t_occupied
                    n_mile+=float(item[7])
                    earnings+=float(item[5])
            except ValueError:
                pass
        if t_occupied<0.5:
            t_onduty=t_onduty-t_occupied
        date=datetime.strptime(item[3], '%Y-%m-%d %H:%M:%S').date()
        hour=int(start_time.strftime('%H'))
        hack_license=item[10]
        print( "%s\t%s\t%s\t%.4f\t%.4f\t%d\t%d\t%.4f\t%.2f" % (date,hour,hack_license,t_onduty,t_occupied,n_pass,n_trip,n_mile,earnings))
if __name__ == '__main__':
    main()