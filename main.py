#Editar imagenes con Python
from PIL import Image
from os import remove
import os

#listar documentos
directorio = os.getcwd() + "/Posted Series"
contenido = []


def listar():
	global contenido
	contenido = os.listdir(directorio)


def jpg(texto):
	textoNue = f"{directorio}\\{texto}"
	img = Image.open(textoNue)
	rgb_img = img.convert("RGB")
	indice = texto.find(".")
	rgb_img.save(f"{directorio}\\{texto[:indice+1]}.jpg", quality=95)


def convertir_imagen():
	for i in contenido:
		punto = i.find(".")
		if i[punto+1:] == "png":
			jpg(i)
			remove(f"{directorio}\\{i}")
		else:
			pass


def redimensionar():
	for i in contenido:
		img = Image.open(f"{directorio}\\{i}")
		new_img = img.resize((200,320))
		new_img.save(f"{directorio}\\{i}", quality=95)


def renombrar():
	for i in contenido:
		punto = i.find(".")
		punto = i[:punto+1]+"jpg"
		os.rename(f"{directorio}\\{i}", f"{directorio}\\{punto}")


if __name__ == "__main__":
	listar()
	convertir_imagen()
	listar()
	redimensionar()
	listar()
	renombrar()