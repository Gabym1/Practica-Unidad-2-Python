numeros = [5,10,15,20,25]
#Funcion para calcular el promedio de la lista 
def calcular_promedio(numeros):
    #variable total para guardar la suma de toda la lista
     total = sum(numeros)
     #variable promedio para guardar el resultado de la division del total de la suma 
     # y dividirlo entre la longitud (len) de la lista numeros 
     promedio = total / len(numeros)
     return promedio
 #Funcion para indicar el numero maximo 
def encontar_maximo(numeros):
    #variable maximo para guardar el resultado de la funcion 
     maximo = max(numeros)
     return maximo
 #Funcion para indicar el numero minimo
def encontrar_minimo(numeros):
    #variable minimo para guardar el resultado de la funcion
     minimo = min(numeros)
     return minimo  
#mandamos a llamar las variables en la que guardamos los resultados de las funciones
promedio = calcular_promedio(numeros)
maximo = encontar_maximo(numeros)   
minimo = encontrar_minimo(numeros)
#imprimimos 
print("El promedio es:", promedio)  
print("El máximo es:", maximo)
print("El mínimo es:", minimo)