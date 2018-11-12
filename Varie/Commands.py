# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 20:50:52 2018

@author: Utente
"""
#import os
import subprocess
#import traceback
from ErrorPrinting import printError

try:
    status = subprocess.getstatusoutput("ls -all")
    print("status = " + str(status) + "\n" + "Return Code: status[0] = " + str(status[0]) + "\n" + "status[1] = " + str(status[1]))
    i = 0; i = i /0;
except ZeroDivisionError as ez:
    #print("Errore" + str(ez))
    #print(traceback.format_exc())
    printError(ez)
except Exception as e:
    printError(str(e))
finally:
    print("finalizzo")



