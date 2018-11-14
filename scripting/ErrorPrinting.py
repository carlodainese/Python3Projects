import traceback

def printError( e ):
    print("Errore" + str(e))
    print(traceback.format_exc())
    return

def printError( e, ferr, ftrace ):
    if (ferr):
        print("Errore" + str(e))
    if(ftrace) :
        print(traceback.format_exc())
    return