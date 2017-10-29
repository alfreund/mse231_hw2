#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:14:01 2017

@author: oseasa
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
def main():
    '''
    Main function
    ''' 
    for line in sys.stdin:
        line = line.rstrip('\n')
        if (line!="") and ("pickup" not in line):
            line = line.strip()
            splits = line.split(",")
            #shared vars in both datasets (in same position)
            medallion = splits[0]  
            hack_license = splits[1]
            if len(splits) == 11: 
            # Fare data
                pickup_datetime = splits[3]
                unique_trip_id = ",".join([medallion,hack_license,pickup_datetime])
            #do not include pickup_datetime again 
            elif len(splits)==14:
            #Trip data  
                pickup_datetime = splits[5]
                unique_trip_id = ",".join([medallion,hack_license,pickup_datetime])
            else:
                unique_trip_id="NA"
            
            unique_trip_id = ",".join([medallion,hack_license,pickup_datetime])
            #unique "trip ID" is combination of medallion & pickup datetime
            print (unique_trip_id+"\t"+line.strip())
    
if __name__ == '__main__':
    main()