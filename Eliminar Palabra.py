#Desarrolar un programa que elimine una palabra que forme parte de una cadena de caracteres
#REQUERIMIENTOS
#La cadena debera ser solicitada por teclado
#La palabra a eliminar debera ser solicitada por teclado

string = input ("Introduce una frase: ")
palabra = input ("Introduce palabra a eliminar: ")
substring = ""

indice = string.find(palabra)
substring = string[0 : indice] + string[indice + len(palabra) + 1 :]

print (f"caena resultante: {substring}")