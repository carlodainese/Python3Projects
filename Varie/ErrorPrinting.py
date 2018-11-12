import traceback

def printError( e ):
    print("Errore" + str(e))
    print(traceback.format_exc())
    return

def printError( e, ftrace ):
    print("Errore" + str(e))
    if(ftrace) :
        print(traceback.format_exc())
    return