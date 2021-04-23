def sumar(listaNumeros):
    suma = 0;
    for n in listaNumeros:
        suma += n**3
    return suma
print(sumar([2,7,5,4,9,3,6,8,1,10]))
