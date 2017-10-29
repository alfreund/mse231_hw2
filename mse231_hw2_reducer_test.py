#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:59:50 2017

@author: andreafreund
"""
import sys
from datetime import datetime
from itertools import groupby
from operator import itemgetter
import math

date_format="%Y-%m-%d %H:%M:%S"
def read_mapper_output(file,separator='\t'):
    for line in file:
        yield line.rstrip().split(separator,1)

def main(separator='\t'):
    data=read_mapper_output(sys.stdin,separator=separator)
    '''
    Main function
    ''' 

    for key, group in groupby(data,itemgetter(0)):
        trip_data=[]
        fare_data=[]
        for key,ride_data in group:
            line=ride_data.strip().split(",")
            if len(line)==11:
                fare_data = line
                #fare[0]=medallion
                #fare[1]=hack
                #fare[2]=vendor
                #fare[3]=start time
                #fare[4]=paymenttype
                #fare[5]=fare amount
                #fare[6]=surcharge
                #fare[7]=tax
                #fare[8]=tip
                #fare[9]=toll
                #fare[10]=total amount
                
            elif len(line)==14:
                trip_data=line
                #trip[0]=medallion
                #trip[1]=hack
                #trip[2]=vendor
                #trip[3]=1
                #trip[4]=blank
                #trip[5]=start_time
                #trip[6]=end_time
                #trip[7]=passanger count
                #trip[8]=time in seconds
                #trip[9]=distance in miles
                #trip[10]=lon1
                #trip[11]=lat1
                #trip[12]=lon2
                #trip[13]=lat2
                try:
                    end_time=datetime.strptime(line[6], '%Y-%m-%d %H:%M:%S')
                    start_time=datetime.strptime(line[5], '%Y-%m-%d %H:%M:%S')
                except:
                    trip_data=[]
                
            else:
                pass
            
            #take out bad data
            try:
                if fare_data==[] or trip_data==[] or trip_data[0]=="medallion":
                    #get rid of header and any empty row
                    pass
                elif trip_data[10]==0 or trip_data[11]==0  or trip_data[12]==0  or trip_data[13]==0:
                    pass
                else:
                    diff=end_time-start_time
                    ddist=float(trip_data[9])
                    lon1=float(trip_data[10])
                    lat1=float(trip_data[11])
                    lon2=float(trip_data[12])
                    lat2=float(trip_data[13])
                    p=0.017453292519943295 #pi/180
                    c=math.cos
                    a=0.5-c((lat2-lat1)*p)/2+c(lat1*p)*c(lat2*p)*(1-c((lon2-lon1)*p))/2
                    dis=7922*math.asin(math.sqrt(a))
                    if ((dis > ddist) or (dis < 0.1*ddist) 
                            or (dis > 3000) or (dis <= 0) or (diff.seconds==0)):
                        pass
                        #omit trips for which the average velocity is greater than 100 mi/hr
                    elif (ddist/(diff.seconds/(60**2)) > 100):
                        pass
                    elif diff.seconds < 60:
                        pass
                    else:
                        #output:
                        #ID+time,medallion,hack,vendor,payment,fare,surcharge,tax,tip,tolls,total,start_time
                        #end_time,passangers,trip time,distance,lon1,lat1,lot2,lat2
                        ID=fare_data[0]+fare_data[3]
                        trip_output=trip_data[5:]
                        print (ID+"\t".join(fare_data[0:3]+fare_data[4:]+trip_output))             

            except ValueError:
                        continue
if __name__ == '__main__':
    main()
