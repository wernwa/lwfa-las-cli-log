#!/usr/bin/python


import sys
from epics import PV
from PV_CONN import PV_CONN
import time
import thread
import numpy

from setup import *


volts = PV_CONN('chicane:magn_volt_all', auto_monitor=True )
currs = PV_CONN('chicane:magn_curr_all', auto_monitor=True )
temps = PV_CONN('chicane:temp_all', auto_monitor=True )

line = '#time timestamp '
line += '\tq1_volt\tq2_volt\tq3_volt\tq4_volt\tq5_volt\tq6_volt\tq7_volt\td1_volt\td2_volt'
line += '\tq1_curr\tq2_curr\tq3_curr\tq4_curr\tq5_curr\tq6_curr\tq7_curr\td1_curr\td2_curr'
line += '\tq1_temp\tq2_temp\tq3_temp\tq4_temp\tq5_temp\tq6_temp\tq7_temp\td1_temp\td2_temp'
line+='\n'
sys.stdout.write(line)


relee_plus=0
relee_minus=24
sign=None

pv_cnt = 9

# for the convertion from pv-array,
# display a number or if None the dashes
def get_num_or_none(obj):
    if obj == 'None' or obj == None: return 'None'
    else:
        try:
            num = float(obj)
        except Exception as e:
            print traceback.format_exc()

        return '%.3f'%num


while True:

    try:
        line = '%s\t'%time.strftime("%Y-%m-%d_%H:%M:%S %s")

        value = volts.get()
        if value == None: line += '\tNone'*9
        else:
            arr = value.tostring().split(' ')
            #relee=round(float(arr[0]))
            #if relee==relee_plus: sign=1
            #else: sign=-1
            q1=get_num_or_none(arr[0])
            q2=get_num_or_none(arr[1])
            q3=get_num_or_none(arr[2])
            q4=get_num_or_none(arr[3])
            q5=get_num_or_none(arr[4])
            q6=get_num_or_none(arr[5])
            q7=get_num_or_none(arr[6])
            d1=get_num_or_none(arr[7])
            d2=get_num_or_none(arr[8])
            line += '\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s'%(q1,q2,q3,q4,q5,q6,q7,d1,d2)


        value = currs.get()
        if value == None: line += '\tNone'*9
        else:
            arr = value.tostring().split(' ')
            q1=get_num_or_none(arr[0])
            q2=get_num_or_none(arr[1])
            q3=get_num_or_none(arr[2])
            q4=get_num_or_none(arr[3])
            q5=get_num_or_none(arr[4])
            q6=get_num_or_none(arr[5])
            q7=get_num_or_none(arr[6])
            d1=get_num_or_none(arr[7])
            d2=get_num_or_none(arr[8])
            line += '\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s'%(q1,q2,q3,q4,q5,q6,q7,d1,d2)

        value = temps.get()
        if value == None: line += '\tNone'*9
        else:
            arr = value.tostring().split(' ')
            if len(arr)<pv_cnt: line += '\tNone'*pv_cnt
            else:
                q1=get_num_or_none(arr[0])
                q2=get_num_or_none(arr[1])
                q3=get_num_or_none(arr[2])
                q4=get_num_or_none(arr[3])
                q5=get_num_or_none(arr[4])
                q6=get_num_or_none(arr[5])
                q7=get_num_or_none(arr[6])
                d1=get_num_or_none(arr[7])
                d2=get_num_or_none(arr[8])
                line += '\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s\t%-9s'%(q1,q2,q3,q4,q5,q6,q7,d1,d2)

        line+='\n'
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(sleep_sec)


    except KeyboardInterrupt:
        #print " Bye"
        sys.exit()

