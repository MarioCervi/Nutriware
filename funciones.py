from hermetrics.hamming import Hamming # Importante hacer pip install hermetrics 
from alimentos import alimentos
from flask import render_template

def resultado_busqueda(alimento, dict):
    for a in alimentos:
        if a["nombre"] == alimento:
            nutriscore = a["nutriscore"]
            alergenos = a["alergenos"]
            return render_template("resultados.html", nutriscore=nutriscore, alergenos=alergenos, a=alimento, dict=dict)
    return render_template("relacionados.html", dict2=dict)


def mostrar_similitudes(alimento_introducido):

    busqueda_usuario = alimento_introducido 

    listadoAlimentos = []

    for element in alimentos: # Para conseguir un listado solo con los nombres 

        listado = (element["nombre"])
        listadoAlimentos.append(listado)

    ham = Hamming()

    similitudes = []

    for producto in listadoAlimentos:

        if producto != busqueda_usuario: # No mostrar como similar el producto que acaba de introducir el usuario

            similitud = ham.similarity(producto, busqueda_usuario) # devuelve una cifra de similitud
            similitudes.append((producto, similitud))
           

    # reverse=True porque sino se ordena automaticamente de menos similar a mas similar
    # similitudes muestra el nombre del producto y su cifra de similitud, nos interesa solo la parte numerica para ordenarla

    similitudes_ordenadas = sorted(similitudes, key=lambda cifra_similitud: cifra_similitud[1], reverse=True) # ordenar de mayor similitud a menos

    tres_similares = 0
    mostrar_listado = []

    while tres_similares<3: # MOSTRAR LOS 3 PRODUCTOS MAS PARECIDOS AL INTRODUCIDO POR EL USUARIO

        mostrar_productos=(similitudes_ordenadas[tres_similares])
        # print("PRODUCTO SIMILAR: ") # para ver por la terminal
        # print(mostrar_productos[0]) # para mostrar solo el nombre y no la cifra
        mostrar_listado.append(mostrar_productos[0])
        tres_similares +=1
    return mostrar_listado