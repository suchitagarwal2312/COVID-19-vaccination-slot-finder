# -*- coding: utf-8 -*-
"""
Created on Mon May 17 00:38:43 2021

@author: vasu
"""

#pip install requests

import requests

import time

from datetime import datetime , timedelta
print("enter age for which you are searching")
person_age = int(input("enter age"))

print("enter pincode for which you are searching")
area_pincode = list(input("Enter pincode"))

print("enter for how many days from now you are searching")
total_days=int(input("enter days"))
print_flag = 'Y'

print("start searching for covid vaccine slots")
current = datetime.today()
form = [current + timedelta(days=i) for i in range(total_days)]
correct_date = [i.strftime("%d-%m-%y") for i in form]

while True:
    i=0
    for find_code in area_pincode:
        for enter_date in correct_date:
            
            url = "https://api.demo.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode={}&date={}".format(find_code,enter_date)
            
            requirements = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
                }
            
            final_op = requests.get(url , headers = requirements)
            
            if final_op.ok:
                file_json = final_op.json()
                
                flag=False
                if file_json["centers"]:
                    if (print_flag.lower()=="y"):
                        
                        for place in file_json["centers"]:
                            
                            for availability in place["sessions"]:
                                if(availability["min_age_limit"]<= person_age and availability["available_capacity"]>0):
                                     print('the pincode for which you are searching:'+ find_code)
                                     print('it is available on : {}'.format(enter_date))
                                     print('name of hospital and destination:',place["name"])
                                     print('name for the block is :' , place['block_name'])
                                     print('Price for the vaccine is:' , place['fee_type'])
                                     print('availability status is:' , availability["available_capacity"])
                                     
                                     
                                     if (availability['vaccine'] != ''):
                                         print("the type of vaccine is", availability['vaccine'])
                                     
                                     i = i+1
                                else:
                                    pass
                    
                    else:
                        pass
                
                else:
                    print("I found no response") 
                                    
    if(i==0):
        print("rn no slots available")
    else:
        print("search is finished")                                     
    date_now = datetime.now() + timedelta(minutes=1)
    
    while datetime.now() < date_now:
        time.sleep(1)
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     