nombre="Juan"
edad=22
estatura=1.70
juega_futbol=False
print("Primer punto: ")
print(f"{nombre} , {edad} , {estatura} , {juega_futbol}")

#El limite de las variables float es que solamente se pueden aproximar, por ejemplo 1/3 nunca se podra expresar exactamente igual siendo un float, sin embargo se podra aproximar.

#Un entero no podra expresarse como un decimal porque solo se tomara la parte entera.
contador=0
numfinal=0
lista=list()
print("Tercer punto: ")
print("Ingrese un numero para sumar sus primeros pares")
n=int(input())
if n%2==0:
    while contador<n:
        contador=contador+2
        lista.append(contador)
    print(lista)
    c=len(lista)
    for x in range(c):
        numfinal=numfinal+lista[x]
    print(numfinal)
else:
    n=n-1
    while contador<n:
        contador=contador+2
        lista.append(contador)
    print(lista)
    c=len(lista)
    for x in range(c):
        numfinal=numfinal+lista[x]
    print(numfinal)
    