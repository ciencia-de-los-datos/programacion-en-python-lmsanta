"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# leer y tranformar archivo
with open("data.csv","r") as file:
    data = file.readlines()
data = [row.replace('\t','|').replace('\n','') for row in data]
data = [row.split("|") for row in data]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    result_1=0
    for i in data:
        result_1= result_1 + int(i[1])
    result_1

    return result_1

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    # importar libreria necesaria
    from collections import Counter

    list_2 = sorted(list(Counter([i[0] for i in data]).items()))

    return list_2


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    list_3 = [(i[0], int(i[1])) for i in data]

    letter_sum = {}

    for letter, num in list_3:
        if letter in letter_sum:
            letter_sum[letter] += num
        else:
            letter_sum[letter] = num

    result_3 = sorted(list((letter, letter_sum[letter]) for letter in letter_sum))

    return result_3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter
    
    list_4 = sorted(list(Counter([i[1] for i in [i[2].split('-') for i in data]]).items()))

    return list_4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    list_5 = [(i[0], int(i[1])) for i in data]

    dict_5 = {}

    for item in list_5:
        letter, num = item
        if letter not in dict_5:
            dict_5[letter] = [num, num]
        else:
            dict_5[letter][0] = max(dict_5[letter][0], num)
            dict_5[letter][1] = min(dict_5[letter][1], num)

    result_5 = sorted([(letter, num[0], num[1]) for letter, num in dict_5.items()])

    return result_5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    list_6 = [(i[4]) for i in data]

    dict_6 = {}

    for row in list_6:
        for item in row.split(','):
            key, value = item.split(':')
            if key not in dict_6:
                dict_6[key] = [int(value)]
            else:
                dict_6[key].append(int(value))

    result_6 = sorted([(key,min(dict_6[key]),max(dict_6[key]))  for key in dict_6])

    return result_6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    list_7 = [(int(i[1]), i[0]) for i in data]

    dict_7 = {}

    for item in list_7:
        key, value = item
        if key not in dict_7:
            dict_7[key] = [value]
        else:
            dict_7[key].append(value)

    result_7 = sorted(list(dict_7.items()))

    return result_7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    list_8 = [(int(i[1]), i[0]) for i in data]

    dict_8 = {}

    for item in list_8:
        key, value = item
        if key not in dict_8:
            dict_8[key] = [value]
        elif value in dict_8[key]:
            pass
        else:
            dict_8[key].append(value)

    result_8 = sorted(list((key,sorted(dict_8[key])) for key in dict_8))

    return result_8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    list_9 = [(i[4]) for i in data]

    dict_9 = {}

    for row in list_9:
        for item in row.split(','):
            key, value = item.split(':')
            if key not in dict_9:
                dict_9[key] = 1
            else:
                dict_9[key] += 1

    result_9= {key: value for key, value in sorted(dict_9.items())}

    return result_9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    list_10 = [(i[0],len((i[1]).split(',')),len((i[2]).split(','))) for i in [(i[0], i[3], i[4]) for i in data]]

    return list_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    list_11 = [(i[1],i[3]) for i in data]

    dict_11 = {}

    for row in list_11:
        list_keys = row[1].split(',')
        value = int(row[0])

        for key in list_keys:
            if key not in dict_11.keys(): 
                dict_11[key] = value
            else:
                dict_11[key] = dict_11[key] + value

    result_11= {key: value for key, value in sorted(dict_11.items())}

    return result_11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    list_12 = [[i[0],i[4].split(',')] for i in data]

    dict_12 = {}

    for letra, lista in list_12:
        suma = 0
        for valor in lista:
            suma += int(valor.split(':')[1])
        if letra in dict_12:
            dict_12[letra] += suma
        else:
            dict_12[letra] = suma

    dict_12 = dict(sorted(dict_12.items()))

    return dict_12
