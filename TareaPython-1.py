nombre="Juan"
edad=22
estatura=1.70
juega_futbol=False
print("Primer punto: ")
print(f"{nombre} , {edad} , {estatura} , {juega_futbol}")

#El limite de las variables float es que solamente se pueden aproximar, por ejemplo 1/3 nunca se podra expresar exactamente igual siendo un float, sin embargo se podra aproximar.

#Un entero no podra expresarse como un decimal porque solo se tomara la parte entera.
print("Tercer punto: ")
print("Por favor ingrese un numero para aplicar la formula de los primeros n numeros pares")
n=int(input())
suma=n*(n+1)
print(f"El resultado aplicando la formula de la suma de los primeros n numeros pares es: {suma}")