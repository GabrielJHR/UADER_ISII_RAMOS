1. Una vez descargado los programas se los ejecuto con el siguiente resultado.
    
    1.b Se ejecuto el comando ```./getJason.pyc ./sitedata.json``` y al hacerlo el programa se cierra sin mostrar ningun mensaje.

    Paso 1: En la carpeta del programa se encuentran los ejecutables y un archivo readme el cual indica como se tiene que utilizar el programa. Ademas el archivo con formato json de donde se van a extraer las claves.
    
    1.c Se instalo el paquete uncompyle6 con el comando ```pip install uncompyle6```.

    1.d Una vez instalado el paquete se ejecuto el comando ```uncompyle6 getJason.pyc > getJason.py``` para obtener su codigo fuente.
    ```python
    # uncompyle6 version 3.9.0
    # Python bytecode version base 2.7 (62211)
    # Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
    # Embedded file name: getJason.py
    # Compiled at: 2022-06-14 16:15:55
    import json, sys
    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]
    with open(jsonfile, 'r') as (myfile):
        data = myfile.read()
    obj = json.loads(data)
    print str(obj[jsonkey])
    # okay decompiling getJason.pyc
    ```

    1.e La diferencia es que el programa recibe dos argumentos, un archivo y una clave. Otra de las diferencias es que no tiene una documentacion cuando se le ingresa el argumento -h 

    1.f Se modifico el programa para que tenga el mismo funcionamiento que el programa original.
    ```python
    # uncompyle6 version 3.9.0
    # Python bytecode version base 2.7 (62211)
    # Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
    # Embedded file name: getJason.py
    # Compiled at: 2022-06-14 16:15:55
    import json, sys

    if(sys.argv[1] == '-h'):
        print('Para usar el programa se debe ingresar como argumento el nombre de un archivo y opcionalmente el numero de token que quiere obtener')
        print('python getJason.py <nombre del archivo> <numero de token>')
        sys.exit(0)

    if(len(sys.argv) >= 1):
        jsonfile = sys.argv[1]
    else:
        print('Se debe ingresar un archivo')
        sys.exit(1)

    if(len(sys.argv) == 3):
        jsonkey = str(sys.argv[3])
    else:
        jsonkey = str(input("Ingresa una posicion para el token: "))

    try:
        with open(jsonfile, 'r') as (myfile):
            data = myfile.read()
        obj = json.loads(data)
    except:
        print('No se pudo abrir el archivo')
        sys.exit(1)

    try:
        print(str(obj['token'+jsonkey]))
    except:
        print('No se encontro el token')
        sys.exit(1)

    # okay decompiling getJason-2.7.pyc
    ```

    1.g Se volvio a compilar el programa getJason.py con el comando ```python -m compileall getJason.py```

