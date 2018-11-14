# encoding: utf-8
# module Script execute shell commands
# no doc

# imports
import os
import time, random
import subprocess as sp
from ErrorPrinting import printError
from subprocess import TimeoutExpired
import json

host = 'http://drupal8.docker.localhost:8000/rest/view/ws-json'
#host = '192.168.1.1'
occurrence = []
timeoutCounter = 0
data = {}
print('***** in execution  *****')

try:
    popen = sp.Popen(["curl", host], stdout=sp.PIPE)
    p = popen
    # wait in seconds i.e 0.05 sec
    p.wait(5e-2)
    """ 
    The communicate() method returns a tuple (stdoutdata, stderrdata). 
    Popen.communicate() interacts with process: Send data to stdin.
    Read data from stdout and stderr, until end-of-file is reached.
    Wait for process to terminate.
    """
    out = p.communicate()[0]

    #print("-->" + str(out))
    data = json.loads(out)
    for x in data:

        print(x)

except TimeoutExpired as te:
    printError(te, False, False)
except Exception as e:
    printError(e, False, True)
finally:
    {} #do nothing!

print('***** end *****')