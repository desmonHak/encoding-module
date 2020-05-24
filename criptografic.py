#! /usr/bin/python3
# -*-coding: utf-8 -*-
import base64

from time import localtime
from random import randint, sample
from criptogrfic import *
from string import ascii_lowercase, ascii_uppercase, digits

__doc__ = """
    modificque este modulo y añada su
    nombre en la lista de autores para
    saber los contribuyyentes del modulo
"""

__Autor__ = "Desmon"
__description__ = 'este modulo ofrce encriptaciones'
__copyright__ = ["Desmon"]
__version__ = 2.2
__license__ = 'Apache 2.0'
__title__ = 'criptografic'

def Convert_Decimal_Reverse_Str(data):
    datosDecimal = []
    datosDecimalStr = ''

    for i in str(data):

        decimal = ord(i)
        datosDecimal.append(decimal)
        datosDecimalStr =  str(decimal) + " " + str(datosDecimalStr)

    try:
        del(data, decimal, i)
    except UnboundLocalError:
        pass
    return [datosDecimalStr, datosDecimal]



def Reverse_Str(data):
    data = list(data)
    dataOput = []
    longitud = len(data) - 1
    for i in data:
        d = data[longitud]
        longitud -= 1

        dataOput.append(d)
    separador = ""

    lista3 = [separador.join(dataOput)]

    try:
        del(d, longitud, i, dataOput, data)
    except UnboundLocalError:
        pass

    return str(lista3[0])


def Desconvert_Decimal(dataDecimal):
    datosDescodificados = []
    datosDescodificadosStr = ""


    dataDecimal[0]

    for i in dataDecimal:

        decimal = str(chr(int(i)))
        datosDescodificados.append(decimal)
        datosDescodificadosStr = str(datosDescodificadosStr) + str(decimal)

    del(dataDecimal, decimal, i)
    return [datosDescodificadosStr, datosDescodificados]


def Convert_Hexadecimal(dataDecimal):
    datosHexadecimales = []
    datosHexadecimalesStr = ''

    for i in dataDecimal:
        decimal = hex(i)
        decimalList = list(decimal)
        if len(decimalList) == 3:
            decimalList.pop(0)
        elif len(decimalList) == 4:
            decimalList.pop(0)
            decimalList.pop(0)

        _str = ""

        for b in decimalList:
            _str += "".join(str(b))

        datosHexadecimales.append(_str)

        datosHexadecimalesStr = str(datosHexadecimalesStr) +" "+ str(decimal)

    try:
        del(dataDecimal, decimal, i, _str, b, decimalList)
    except UnboundLocalError:
        pass

    return [datosHexadecimalesStr, datosHexadecimales]



def Convert_Binari(dataDecimal):
    datosHexadecimales = []
    datosHexadecimalesStr = ''

    for i in dataDecimal:
        decimal = bin(int(i))
        decimalList = list(decimal)
        decimalList.pop(0)
        decimalList.pop(0)
        _str = ""
        for b in decimalList:
            _str += "".join(str(b))
        datosHexadecimales.append(_str)
        datosHexadecimalesStr = str(datosHexadecimalesStr) + str(_str)

    try:
        del(dataDecimal, decimal, i, decimalList, _str)
    except UnboundLocalError:
        pass

    return [datosHexadecimalesStr, datosHexadecimales]


def Cifrado_Cesar_Simple(Data, Number, estado="coding"):
    DataOput = Convert_Decimal_Reverse_Str(str(Data))[1]
    datosStr = ''
    datosListStr = []

    if int(Number) < 0:
        Number = int(Number) * -1

    for i in range(0, len(DataOput)):

        if str(estado) == "coding":
            DataOput[i] = int(DataOput[i]) + int(Number)
        elif str(estado) == "decoding":
            DataOput[i] = int(DataOput[i]) - int(Number)

        if int(i) < 0:
            i = int(i) * -1

        datosStr = datosStr + chr(DataOput[int(i)])
        datosListStr.append(str( chr(DataOput[int(i)])))

    try:
        del(Data, Number, i)
    except UnboundLocalError:
        pass

    return [datosStr, DataOput, datosListStr]


def Encript_1(data, helping="no", MaxRandom="no"):

    if data == '':
        print("la cadena introducida no contenia caracteres y se finalizo el script")
        exit(0)

    if str(helping) == "no":
        pass
    elif str(helping) == "yes":
        print("esta funcion usa un cifrado cesar, se obtiene la\nlongitud del mensaje y se le suma un valor aleatorio\neste valor numerico se usara para sumarlo al valor ascii del los caracteres\nademas usa una funcion que voltea las palabras")
    else:
        pass

    data = Reverse_Str(str(data))
    if str(MaxRandom) == "no":
        longitud = len(data)+int(randint(0, int(randint(0, 10000))))
    else:
        longitud = len(data)+int(randint(0, int(MaxRandom)))

    dataOput = Cifrado_Cesar_Simple(data, int(longitud), estado="coding")

    del data, helping, MaxRandom
    return (dataOput[0], dataOput[1], dataOput[2], {"clave":int(longitud)})

def Decrypt_1(data, clave):

    if data == '':
        print("la cadena introducida no contenia caracteres y se finalizo el script")
        exit(0)

    data = Reverse_Str(str(data))

    dataOput = Cifrado_Cesar_Simple(data, int(clave), estado="decoding")

    del data, clave, dataOput[2]

    return [dataOput[0], dataOput[1]]

def Encript_2(data, conjunto="no", TypeOput="None" ,ValueMax=5631, ValueMini=5024, hashMax=32):

    randonString = ascii_lowercase+ascii_uppercase
    randonStringAll = randonString  +digits

    if data == "":
        raise Exception("\033[1;31m<Data-0> You should inputs the data, why you input None\033[1;37m")


    dataD = list(data)
    longitud = len(dataD)


    try:
        leterFynalli = dataD[int(longitud)]
    except IndexError:
        leterFynalli = dataD[int(longitud) - 1]
    leterInicial = dataD[0]
    del dataD


    if str(leterFynalli) == str(leterInicial) or longitud == 1:
        leterFynalli = str("".join(sample(str(randonString), 1)))
        leterInicial = str("".join(sample(str(randonString), 1)))
    elif str(leterFynalli) == " ":
        leterFynalli = str("".join(sample(str(randonString), 1)))
    elif str(leterInicial) == " ":
        leterFynalli = str("".join(sample(str(randonString), 1)))
    else:
        pass



    if int(longitud) > 100:
        longitud = randint(0, int(longitud)-1)
    elif int(longitud) < 10:
        longitud = randint(0, 99)
    else:
        pass


    while True:
        _time = localtime()
        second = randint(0, _time[5])  # 0
        minuts = randint(0, _time[4])  # 0
        hora = randint(0, _time[3])    # 0
        dataTime = str(hora)+ str(second)+ str(minuts)

        if len(list(dataTime)) > 3:
            break


    del(_time)

    hashing = str(dataTime)+ str(longitud)+ str(leterFynalli)+ str(ord(str(leterFynalli)))+ str(leterInicial)+ str(ord(str(leterInicial)))
    del hora, second, minuts, longitud, leterFynalli, leterInicial

    randomeNumber = len(list(hashing))

    hashing += str(randomeNumber)
    del randomeNumber

    if int(hashMax) > len(list(hashing)):
        hashing +=  str(randint(0, 4)) # 0-4 [yes], 5-9 [no]
    else:
        hashing +=  str(randint(5, 9))

    while True:
        if int(hashMax-1) > len(list(hashing)):
            hashing += str("".join(sample(str(randonStringAll), 1)))
        else:
            break
    del randonStringAll

    def _conjuntoNo(data, hashing=str(hashing), TypeOput=str(TypeOput)):

        _multixor = int(randint(int(randint(0, 9600)), 9706))
        _Longitud = len(list(hashing)) * int(_multixor) / 150
        hashing += str(chr(_multixor))
        del _multixor

        dataOput = Cifrado_Cesar_Simple(str(data), int(_Longitud), estado="coding")
        dataOput[0] = Reverse_Str(dataOput[0])

        del _Longitud

        if TypeOput == "None" or TypeOput == "none":
            hashing = hashing.encode()
        elif TypeOput == "base85":
            hashing = base64.b85encode(hashing.encode())
        elif TypeOput == "base64":
            hashing = base64.b64encode(hashing.encode())
        elif TypeOput == "base32":
            hashing = base64.b32encode(hashing.encode())
        elif TypeOput == "base16":
            hashing = base64.b16encode(hashing.encode())
        elif TypeOput == "encodebytes":   #base64.decodestring
            hashing = base64.encodebytes(hashing.encode())
        elif TypeOput == "urlsafe_b64encode":
            hashing = base64.urlsafe_b64encode(hashing.encode())
        elif TypeOput == "reverse_str":
            hashing = Reverse_Str(str(hashing)).encode()
        else:
            raise Exception("\033[1;31m<Codificacion-Error> Codificacion Invalid!, opcions: base85, base64, base32, base16, encodebytes, urlsafe_b64encode, reverse_str\033[1;37m")

        return (dataOput[0], dataOput[2], hashing.decode())

    del hashing

    def _conjuntoYes(data, conjunto="no", TypeOput="None" ,ValueMax=5631, ValueMini=5024, hashMax=32):
        dataOputRaw = []
        dataStr = ""
        dataHashsing = []
        for i in list(data):
            hashing = Encript_2(str(i), conjunto=conjunto, TypeOput=TypeOput, ValueMax=ValueMax, ValueMini=ValueMini, hashMax=hashMax)
            dataOputRaw.append([str(hashing[0]), str(hashing[2])])
            dataStr += str(hashing[0])
            dataHashsing.append(str(hashing[2]))
            del hashing
        return (dataOputRaw, dataStr, dataHashsing)

    if str(conjunto) == "no":
        dataOput = _conjuntoNo(str(data))
        hashing = str(dataOput[1])
    elif str(conjunto) == "yes":
        dataOput = _conjuntoYes(str(data))
    else:
        raise Exception("\033[1;31m<Argument-Error> Argument Invalid, Encript_2(data, ('no' or 'yes'))\033[1;37m")

    return dataOput


def Todos_Los_Cifrados(Datos, NumeroCrifradoCesar=4567):
    decimal = Convert_Decimal_Reverse_Str(str(Datos))
    hexa = Convert_Hexadecimal(decimal[1])
    binario = Convert_Binari(decimal[1])
    difc = Cifrado_Cesar_Simple(str(Datos), int(NumeroCrifradoCesar))
    reverse = Reverse_Str(str(Datos))
    encript_1 = Encript_1(str(Datos))
    encript_2 = Encript_2(str(Datos), conjunto="yes", hashMax=64)

    try:
        del(datos)
    except UnboundLocalError:
        pass

    return '{"datos en decimal":'+str(decimal)+'\n"datos en hexadecimal":'+str(hexa)+'\n"datos en binario":'+str(binario)+'\n"datos aplicando un cifrado cesar con el digito por defecto":' + str(NumeroCrifradoCesar) + ':'+str(difc)+'\n"datos volteados":'+str(reverse)+'\n"datos aplicandoles la funcion Encript_1:"'+str(encript_1)+'\n"datos aplicandoles la funcion Encript_2":'+str(encript_2)+'\n}'


if __name__ == "__main__":
    print(Todos_Los_Cifrados(str(input("introduce tus datos: "))))
    #file = open(str(input("\n\n\archivo a codificar: ")), "r")
    #data = file.read()
    #data = Todos_Los_Cifrados(str(data))
    #print(data)
    #file.close()
    #file = open("oput.txt", "w")
    #file.writelines(str(data))
    #file.close()
