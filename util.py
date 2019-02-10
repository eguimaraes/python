import datetime

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
    
    def carregarArquivo(arqIn):
    f = open(arqIn,"r")
    for x in f:
          print(x)   
            
def contaLinhas(arqIn):
   count = len(open(arqIn).readlines(  ))
   print(count)
