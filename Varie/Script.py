# encoding: utf-8
# module Script execute shell commands
# no doc

# imports
import os
import subprocess
from ErrorPrinting import printError
from subprocess import TimeoutExpired

#host = 'vlsiapacphp001.intra.infocamere.it'
host = '192.168.1.1'
timelist = []
try:
    p = subprocess.Popen(["ping", "-c 1", host], stdout=subprocess.PIPE)
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
    tokens = str(out).split(' ')
    # print(tokens)
    for x in tokens:
        if (x.find('time') > -1):
            timelist.append(x)
            #print(x)
            break
except TimeoutExpired as te:
    printError(te, True)
except Exception as e:
    printError(e, False)
finally:
    for x in timelist:
        print(x)
    print('exit')


