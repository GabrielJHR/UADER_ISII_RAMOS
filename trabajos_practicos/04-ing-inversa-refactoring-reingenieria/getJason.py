# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys

class Token():
    def setNumero(self, numero):
        self.numero = numero
    
    def setArchivo(self, archivo):
        try:
            with open(archivo, 'r') as (myfile):
                data = myfile.read()
            self.archivo = json.loads(data)
        except:
            print('No se pudo abrir el archivo')
            sys.exit(1)
    
    def getToken(self):
        try:
            return (str(self.archivo['token'+self.numero]))
        except:
            print('No se encontro el token')
            sys.exit(1)

    def getHelp(self):
        return """Para usar el programa se debe ingresar como argumento el nombre de un archivo y opcionalmente el numero de token que quiere obtener\n
        python getJason.py <nombre del archivo> <numero de token>"""

jsonToken = Token()

if(len(sys.argv) >= 1):
    if(sys.argv[1] == '-h'):
        print(jsonToken.getHelp())
        sys.exit(0)
    jsonToken.setArchivo(sys.argv[1])
else:
    print('Se debe ingresar un archivo')
    sys.exit(1)

if(len(sys.argv) == 3):
    jsonToken.setNumero(str(sys.argv[2]))
else:
    jsonToken.setNumero(str(input("Ingresa una posicion para el token: ")))

print(jsonToken.getToken())
# okay decompiling getJason-2.7.pyc