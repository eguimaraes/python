import fitsJoinHf5 as fits
import hdf5JoinDataSet2 as hdf5
import plotMap as mapa



def test():
 arquivo=raw_input("Digite o nome do arquivo HDF5 de soma:")
 print("Lendo Arquivos Fits - Aguarde") 
 fits.join(arquivo)
 print("Montando Arquivo HDF5 - Aguarde") 
 hdf5.somar(arquivo)
 print("Preparando Mapa - Aguarde") 
 mapa.plot(arquivo)


test()



