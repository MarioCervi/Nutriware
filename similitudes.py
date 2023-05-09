from hermetrics.hamming import Hamming # instalar con pip install hermetrics
import alimentos

# probando modulo hermetrics 

s1 = ["chocolate",
      "coca-cola",
      "caracoles",
      "conejo",
      "cacaolat",
      "arroz"]

busqueda_usuario = "actimel"

listadoAlimentos = []

for element in alimentos.alimentos2:

    s3 = len(alimentos.alimentos2) # ver la longitud del diccionario
    #print(s3)
    listado = (element["nombre"])
    listadoAlimentos.append(listado)
    

    #print("el listado es: "+listado) # 


print(listadoAlimentos)


ham = Hamming()
print("La palabra mas similar es: "+max(listadoAlimentos, key=lambda cadena:ham.similarity(cadena, busqueda_usuario)))