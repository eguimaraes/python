import math as m
a=input('Digite algo para o teste: ')
print (a)

print ("Teste de Leitura de arquivos")
f = open ('myfile.txt')
dados = f.readline()
while (len(dados)>0):
    dados = f.readline()
    dados=dados.split()
    if len(dados)>0:
        print(dados[0])
        print(dados[1])
        print(dados[2])
    
f.close()

print ("Teste de Escrita de arquivos")

g = open ('tabuada2.txt','w')
g.close()


g = open ('tabuada2.txt','w')
t=input("digite um nr ")
print ("Vamos escrever a tabuada do "+t)
for i in range(11):
    a=i*int(t)
    print(t+" X "+str(i)+" = "+str(a)+"\n")
    g.write(t+" X "+str(i)+" = "+str(a)+"\n")
    
g.close()
valor=""
valores=valor.split(" ")
nr=""
texto=""
erro=""

while len(valor)==0 and len(valores)<2 or (nr=="" and texto==""):
    valor=input("digite um texto e um nr separdo por espaço ")
    valores=valor.split(" ")
    try:
        nr=int(valores[1])
        print("Numero= ",nr)
        texto=str(valores[0])        
        print("Texto= ",texto)
    except:
        nr=""
        texto=""
    
    nrW=0
    nrInt=0
    
    print("teste de leitura de aqruivos")   
    print("wombat.txt")   
    wb=open("wombat.txt")
    conteudo=wb.readlines()
    print(conteudo)
    for linha in conteudo:
        if "wombat" in linha:
           nrW=nrW+len(linha.split("wombat"))
        
    palavras=linha.split(" ")
    for palavra in palavras:
        try:
            nrInt=nrInt+int(palavra)
        except:
           "" 
    

    wb.close()
print("Nr wombat= ",nrW)
print("Nr Int somado= ",nrInt)


nrW=0
nrInt=0
    
print("teste de leitura de aqruivos")   
print("wombat.txt")   
wb=open("wombat.txt")
conteudo=wb.readline()
print(conteudo)
for line in wb:
  print (line)
  if "wombat" in linha:
      nrW=nrW+len(linha.split("wombat"))
  palavras=linha.split(" ")
  for palavra in palavras:
      try:
          nrInt=nrInt+int(palavra)
      except:
           "" 
    
wb.close()
print("Nr wombat= ",nrW)
print("Nr Int somado= ",nrInt)


mtr=open("matrizTeste.txt","w")
t=input("digite um nr ")
print ("Vamos escrever a tabuada do "+t)
for i in range(11):
    a=i*int(t)
    b=m.sqrt(a)
    mtr.write(str(i)+" "+str(t)+" "+str(a)+" "+str(b)+"\n")
    
mtr.close()

    
    

