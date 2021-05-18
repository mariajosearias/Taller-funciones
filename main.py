frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
elemento->str-->elemento
Salidas
lista-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
 

#Realizar una funcion que retorne la copia de una lista que pasa por parametro 
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""
def copia_lista(lista):
  return lista.copy() 
#Realizar una funcion que retorne una lista de numeros enteros  
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""   
def numeros_enteros(lista):
  aux=[]
  aux_uno=[]
  for i in lista:
    aux.append(float(i))
  for i in aux:
    aux_uno.append(int(i))  
  return aux_uno

#Realiza una funcion que retorne una lista con los numeros pares
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""  
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux    
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""  
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista


#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista-list-->lista
letra-->str-->letra
Salidas
lista-list-->lista
"""  
def palabras_por_letra (lista,elemento):
  aux=[]
  for i in lista:
     if(i[0]==elemento):
      aux.append(i)
  return aux


#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamano
"""   
def tamano_lista(lista):
  for i in lista:
    print (len(lista))
     
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Salidas
"""  
def informacion_lista():
  pass
#Retornar una lista con los numero negativos  
"""
Entradas:
lista->list->lista
Salidas
lista->list->lista
"""  
def numeros_negativos(lista):
  aux=[]
  for i in lista:
    if(float(i)<0):
      aux.append(i)
  return aux    
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
def posicion_elemento(lista:list,elemento:str):
  for i in lista:
    if(i==elemento):
     p=lista.index(i)
     print (p)
     
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(lista,elemento):
  lista.append(elemento)
  return lista
#Realizar una funcion que cuente el numero de veces que se repite un elemento  
def repetir(lista,elemento):
  aux=[]
  for i in lista:
    aux.append(float(i))
  for i in aux:
    p=aux.count(elemento)
  return p 

frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
elemento->str-->elemento
Salidas
lista-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
 

#Realizar una funcion que retorne la copia de una lista que pasa por parametro 
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""
def copia_lista(lista):
  return lista.copy() 
#Realizar una funcion que retorne una lista de numeros enteros  
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""   
def numeros_enteros(lista):
  aux=[]
  aux_uno=[]
  for i in lista:
    aux.append(float(i))
  for i in aux:
    aux_uno.append(int(i))  
  return aux_uno

#Realiza una funcion que retorne una lista con los numeros pares
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""  
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux    
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""  
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista


#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista-list-->lista
letra-->str-->letra
Salidas
lista-list-->lista
"""  
def palabras_por_letra (lista,elemento):
  aux=[]
  for i in lista:
     if(i[0]==elemento):
      aux.append(i)
  return aux


#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamano
"""   
def tamano_lista(lista):
  for i in lista:
    print (len(lista))
     
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Salidas
"""  
def informacion_lista():
  pass
#Retornar una lista con los numero negativos  
"""
Entradas:
lista->list->lista
Salidas
lista->list->lista
"""  
def numeros_negativos(lista):
  aux=[]
  for i in lista:
    if(float(i)<0):
      aux.append(i)
  return aux    
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
def posicion_elemento(lista:list,elemento:str):
  for i in lista:
    if(i==elemento):
     p=lista.index(i)
     print (p)
     
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(lista,elemento):
  lista.append(elemento)
  return lista
#Realizar una funcion que cuente el numero de veces que se repite un elemento  
def repetir(lista,elemento):
  aux=[]
  for i in lista:
    aux.append(float(i))
  for i in aux:
    p=aux.count(elemento)
  return p 

if  _name_  ==  "_main_" :