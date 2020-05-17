#! /usr/bin/python3
# -*-coding: utf-8 -*-

__doc__ = """
    modificque este modulo y añada su
    nombre en la lista de autores para
    saber los contribuyyentes del modulo
"""

__Autor__ = ["Desmon"]
__version__ = 2.1

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
            print("hi")
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

    for i in range(0, len(DataOput)):

        if str(estado) == "coding":
            DataOput[i] = int(DataOput[i]) + int(Number)
        elif str(estado) == "decoding":
            DataOput[i] = int(DataOput[i]) - int(Number)

        datosStr = datosStr + chr(DataOput[int(i)])

    try:
        del(Data, Number, i)
    except UnboundLocalError:
        pass

    return [datosStr, DataOput]

def Todos_Los_Cifrados(Datos, NumeroCrifradoCesar=4567):
    decimal = Convert_Decimal_Reverse_Str(str(Datos))
    hexa = Convert_Hexadecimal(decimal[1])
    binario = Convert_Binari(decimal[1])
    difc = Cifrado_Cesar_Simple(str(Datos), int(NumeroCrifradoCesar))
    reverse = Reverse_Str(str(Datos))

    try:
        del(datos, NumeroCrifradoCesar)
    except UnboundLocalError:
        del(NumeroCrifradoCesar)

    return [decimal, hexa, binario, difc, reverse]

if __name__ == "__main__":
    print(Todos_Los_Cifrados(str(input("introduce tus datos: "))))
    file = open(str(input("archivo a codificar: ")), "r")
    data = file.read()
    data = Todos_Los_Cifrados(str(data))
    print(data)
    file.close()
    file = open("oput.txt", "w")
    file.writelines(str(data))
    file.close()
