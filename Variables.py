a = 5
b = 'David'
c = "Cabrera"
d = 10,5
e = '10'

#comentario de una sola linea

'''comentari
parrafo'''

print("Mi nombre es {} y mi apellido es {}". format(b,c))

print(int(e))

#dato = input('Cual es tu nombre ?: ')
#print(dato)

num1 = 1
num2 = 5

if num1 < num2:
    print('num1 es menor que num2')

if num1 < num2:
    print('num1 es menor que num2')
else:
    print('num1 no es menor de num2')

if num1 < num2:
    print('num1 es menor que num2')
elif num1 == num2:
    print('num1 es igual a num2')
else:
    print('num1 es mayor a num2')

x =1
while x <= 10:
    print(x)
    x = x + 1

z = 1
for z in range(1,10):
    print(z)

users = ['A', 'B', 'C']

for user in users:
    print(user)

def saludo():
    print('Hola Clase')
saludo()

def cuadrado(n):
    print(n*n)
    cuadrado(2)

def mi_nombre_(n):
    return 'su nombre es {} y apellido Cabrera'.format(n)
nom = mi_nombre_('David')
print(nom)


#tuplas
a = (1,2,'aaa', True, False, 10,5)

#EN TUPLAS NO SE PUEDEN CAMBIAR DATOS

#lISTAS
users = 'A', 'B', 'C'
users [1]
print(users)

#Diccionarios
alumnos = {'nombre' : 'David','apellido':'Cabrera','edad':24}
print(alumnos)


clase = [
    {'nombre' : 'David','apellido':'Cabrera','edad':24},
    {'nombre' : 'Esteban','apellido':'Zambrano','edad':23},
    ('David', '123')
]

print(clase)



import random

numero = random.randint(1, 10)

print(numero)

#raizc cuadrada

from math import sqrt

n = sqrt(9)

print(n)

