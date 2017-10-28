#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:14:01 2017

@author: oseasa
"""
import sys
from datetime import datetime

def main():

#infile = open("join6.tsv", "r")

    for line in sys.stdin:
        line = line.rstrip('\n')
    
        if (line!=""):
            #line = line.strip()
            line = line.split("\t") #21 columns
            #variables needed in output
            hack_license = line[2]       
                
            try:
                start_year = datetime.strptime(line[12], '%Y-%m-%d %H:%M:%S').strftime('%Y')   
                pickup_datetime= datetime.strptime(line[12], '%Y-%m-%d %H:%M:%S')
                dropoff_datetime= datetime.strptime(line[13], '%Y-%m-%d %H:%M:%S')
                #trip time (trip_time not always accurate; recalculating)
                time = dropoff_datetime - pickup_datetime
                #trip distance
                distance = float(line[16])  
                #fare
                fare = float(line[10])
                #passengers
                passengers = float(line[14])
                #mapper key
                driver_id = hack_license+start_year
                #add date rounded to the closest hour
                rounded_time=str(datetime.strptime(line[12], '%Y-%m-%d %H:%M:%S').replace(second=0,minute=0))

            except (ValueError, IndexError):
                continue
                
                #new_vars = [driver_id, pickup_hr, dropoff_hr, pickup_datetime, 
                             #dropoff_datetime, fare, time, distance, passengers]
                
            print ('%s\t%s\t%s\t%s\t%s\t%f\t%s\t%f\t%d\t%d\t%s' % 
                       (driver_id, driver_id+rounded_time,rounded_time,pickup_datetime, 
                        dropoff_datetime, fare, time, 
                        distance, passengers, 1,hack_license))
    
if __name__ == '__main__':
    main()
