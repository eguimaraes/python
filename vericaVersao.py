import comparara as comparar

f = open ('pergunta2a.csv')
fout=open ('pergunta2aOut.txt',"a")
fout.write("versaoAntiga;VersaoAtual;Status;Nr Comits\n")
dados =f.readline()
texto=[]
s=";"

while (len(dados)>0):
    dados = f.readline()
    if len(dados)>0:
        dadosProc=[]
        texto=dados.split(";")
        versaoAnterior=texto[1]
        versaoAtual=texto[0]
        status="teste"
        dadosProc.append(versaoAnterior)
        dadosProc.append(versaoAtual)
        dadosProc.append(comparar.comparar(versaoAnterior,versaoAtual))
        dadosProc.append(texto[2])
        print(s.join(dadosProc))
        fout.write(s.join(dadosProc)+"\n")

f.close()
fout.close()





    
