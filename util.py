def printTime(msg):
    x = datetime.datetime.now()
    print(msg+str(x))

def writeDsk(arq,msg):
    x = datetime.datetime.now()
    msg2w=msg+str(x)
    print(msg2w)
    filehandle = open(arq,'a')  
    filehandle.write(msg2w) 
    filehandle.close()  
