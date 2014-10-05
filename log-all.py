#!/usr/bin/python


import sys
from epics import PV
from PV_CONN import PV_CONN
import time
import thread
import numpy

sleep = 1 # sleep seconds

volts = PV_CONN('shicane:ps_volt_all')
currs = PV_CONN('shicane:ps_curr_all')
temps = PV_CONN('shicane:ps_temp_all')

line = '#time timestamp '
line += '\tq1_volt\tq2_volt\tq3_volt\tq4_volt\tq5_volt\tq6_volt\tq7_volt\td1_volt\td2_volt'
line += '\tq1_curr\tq2_curr\tq3_curr\tq4_curr\tq5_curr\tq6_curr\tq7_curr\td1_curr\td2_curr'
line += '\tq1_temp\tq2_temp\tq3_temp\tq4_temp\tq5_temp\tq6_temp\tq7_temp\td1_temp\td2_temp'
line+='\n'
sys.stdout.write(line)


relee_plus=0
relee_minus=24
sign=None


while True:

    line = '%s\t'%time.strftime("%Y-%m-%H:%M:%S %s")

    value = volts.get()
    if value == None: line += '\tNone'*9
    else:
        arr = value.tostring().split(' ')
        relee=round(float(arr[0]))
        if relee==relee_plus: sign=1
        else: sign=-1
        q1=sign*float(arr[1])
        q2=sign*float(arr[2])
        q3=sign*float(arr[3])
        q4=sign*float(arr[4])
        q5=sign*float(arr[5])
        q6=sign*float(arr[6])
        q7=sign*float(arr[7])
        d1=sign*float(arr[8])
        d2=sign*float(arr[9])
        line += '\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'%(q1,q2,q3,q4,q5,q6,q7,d1,d2)


    value = currs.get()
    if value == None: line += '\tNone'*9
    else:
        arr = value.tostring().split(' ')
        q1=sign*float(arr[1])
        q2=sign*float(arr[2])
        q3=sign*float(arr[3])
        q4=sign*float(arr[4])
        q5=sign*float(arr[5])
        q6=sign*float(arr[6])
        q7=sign*float(arr[7])
        d1=sign*float(arr[8])
        d2=sign*float(arr[9])
        line += '\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'%(q1,q2,q3,q4,q5,q6,q7,d1,d2)

    value = temps.get()
    if value == None: line += '\tNone'*9
    else:
        arr = value.tostring().split(' ')
        q1=float(arr[0])
        q2=float(arr[1])
        q3=float(arr[2])
        q4=float(arr[3])
        q5=float(arr[4])
        q6=float(arr[5])
        q7=float(arr[6])
        d1=float(arr[7])
        d2=float(arr[8])
        line += '\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'%(q1,q2,q3,q4,q5,q6,q7,d1,d2)

    line+='\n'
    sys.stdout.write(line)
    sys.stdout.flush()
    time.sleep(sleep)


