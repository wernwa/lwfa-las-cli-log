#!/usr/bin/python


import sys
from epics import PV
from PV_CONN import PV_CONN
import time
import thread

from setup import *

pvs=[]


if __name__ == "__main__":


    if len(sys.argv)<=1:
        print 'usage: ./log.py <epcis_var1> <epcis_var2> <epcis_var3> ...'
        sys.exit(0)

    for i in range(1,len(sys.argv)):
        print sys.argv[i]
        pvs.append(PV_CONN(sys.argv[i]))
    line = '#time timestamp\t'
    for pv in pvs:
        line += '\t%s'%pv.pvname
    line+='\n'
    sys.stdout.write(line)


    while True:
        line = '%s\t'%time.strftime("%Y-%m-%H:%M:%S %s")
        for pv in pvs:
            line += '\t%-9s'%pv.get()
        line+='\n'
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(sleep_sec)


