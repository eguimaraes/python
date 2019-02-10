def getPlotMeanVariance(arqIn,arqOutMean,arqOutStd):
    dados=carregarMedia(arqIn)
    for l in (dados):
        linhaDados=l.split(",")
        util.write2Dsk(arqOutMean+".txt",linhaDados[1]+"\n")
        variance=pow(float(linhaDados[2]),2)
        util.write2Dsk(arqOutStd+".txt",variance)
    salvarPLT(criarImg(np.loadtxt(arqOutMean+".txt")),arqOutMean+".png")
    salvarPLT(criarImg(np.loadtxt(arqOutStd+".txt")),arqOutStd+".png")


