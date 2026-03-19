#Analisis de codigo 
# 1. El codigo nos muestra un arreglo numeros del 1 al 5 que nos va a imprimir el incremento de
# cada numero en la variable total, el resultado final es la suma de los numeros del 1 al 5, el resultado es 15
numeros= [1,2,3,4,5]
total=0
#for i in range(len(numeros)):
 #   total+=numeros[i]
    
for i in numeros:
    total+=i
print(total)