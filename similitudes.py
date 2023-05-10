from hermetrics.hamming import Hamming
import alimentos

busqueda_usuario = "ajos" # provisional hasta que se vincule con la busqueda del usuario real 

listadoAlimentos = []

for element in alimentos.alimentos2: # Para conseguir un listado solo con los nombres 

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


tres_repeticiones = 0

while tres_repeticiones<3: # MOSTRAR LOS 3 PRODUCTOS MAS PARECIDOS AL INTRODUCIDO POR EL USUARIO

    mostrar_productos=(similitudes_ordenadas[tres_repeticiones])
    print("PRODUCTO SIMILAR: ")
    print(mostrar_productos)
    tres_repeticiones +=1