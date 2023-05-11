from hermetrics.hamming import Hamming
import alimentos
import app

def mostrar_similitudes(alimento_introducido):

    busqueda_usuario = alimento_introducido # provisional hasta que se vincule con la busqueda del usuario real 

    listadoAlimentos = []

    for element in alimentos.alimentos: # Para conseguir un listado solo con los nombres 

        listado = (element["nombre"])
        listadoAlimentos.append(listado)
    
        #print(listadoAlimentos) # verificar listado de bbdd 

    ham = Hamming()

    similitudes = []

    for producto in listadoAlimentos:

        similitud = ham.similarity(producto, busqueda_usuario) # devuelve una cifra de similitud
        #print(similitud)
        similitudes.append((producto, similitud))
        #print(similitudes)

    # reverse=True porque sino se ordena automaticamente de menos similar a mas similar
    # similitudes muestra el nombre del producto y su cifra de similitud, nos interesa
    # solo la parte numerica para ordenarla

    similitudes_ordenadas = sorted(similitudes, key=lambda cifra_similitud: cifra_similitud[1], reverse=True) # ordenar de mayor similitud a menos


    tres_similares = 0
    mostrar_listado = []

    while tres_similares<3: # MOSTRAR LOS 3 PRODUCTOS MAS PARECIDOS AL INTRODUCIDO POR EL USUARIO

        mostrar_productos=(similitudes_ordenadas[tres_similares])
        print("PRODUCTO SIMILAR: ")
        print(mostrar_productos[0]) # para mostrar solo el nombre y no la cifra
        mostrar_listado.append(mostrar_productos[0])
        tres_similares +=1

    # devolver esto en un array a la llamada de app.py


#print(mostrar_listado)

    return mostrar_listado