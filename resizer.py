
##############################################
# # # LIBRERIAS # # #

from PIL import Image
import PIL
import os
import glob
import csv

##############################################
# # # CARGA DE IMAGENES # # # 

 # #Definición del directorio donde se alojarán las imágenes modificadas# #
path = "/home/haze/Documentos/PEV/Requerimientos/PagWEB/CARGA/output"

 # #Lectura por cada archivo presente en el directorio "files" y las guarda con el tamaño modificado# #
for filename in glob.glob('/home/haze/Documentos/PEV/Requerimientos/PagWEB/CARGA/files/*.*'):
	print(filename)	
	img = Image.open(filename).resize((320, 290))
	img.save('{}{}{}'.format(path,'/',os.path.split(filename)[1])) 

 # #Registro de los nombres de cada archivo saliente en "/output"# #
data=[]
with open('images.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    for filename in os.listdir("/home/haze/Documentos/PEV/Requerimientos/PagWEB/CARGA/output"):
        data.append(filename)
        writer.writerow(data)
        data=[]
writeFile.close()

###############################################

"""
El resultado es la lectura de todas las fotos disponibles desde sus formatos
originales y guardando u a unos de menor resolución, peso y dimensiones.
Además se almacena el nombre de cada imagen en una columna csv para su 
posterior uso 

"""
###############################################
print("Fin del Proceso")

