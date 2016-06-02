# -*- coding: utf-8 -*-
from persistencia import *
import codecs

moduloPersistencia = Persistencia()
tweets = moduloPersistencia.iteradorSeguimiento("#AlgoMásQueDeporte")
archivo = codecs.open('documentos.txt', 'w', 'utf8')
num = 0
max = 101
for k in tweets:
    print(num)
    num+=1
    texto = (str(k["text"])).replace("\n"," ")
    archivo.write(texto+"\n")
    if (num > max):
        break
archivo.close()
print("Fin")