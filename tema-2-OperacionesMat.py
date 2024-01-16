num1=20
num2=4
print("el resultado de la suma es", (num2 + num1))
print("el resultado de la resta es", (num2 - num1))
print("el resultado de la multiplicacion es", (num2 * num1))
print("el resultado de la division es ", (num2 / num1))
print("el resultado de la division exacta es ", (num2 // num1))
print("el resultado de la potencia es", (num2 ** num1))

#concatencion en python

texto1 = "hola"
texto2 = "mundo"
textofinal = texto1+ " " + texto2
print(textofinal)

print("El saludo es: %s %s " %(texto1, texto2))
saludoFinal = "Saludo {} {}", format(texto1, texto2)
print(saludoFinal)

saludoFinal2= "saludo 2: {y} {x}", format(y=texto1, x=texto2)
print(saludoFinal2)