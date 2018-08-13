
import  turtle


lado1 = input('ingrese valor del cuadrado: ')


window = turtle.Screen()

#Inicia el dibujo
square = turtle.Turtle()


for z in range(1,8):
    # dibuja
    square.forward(int(lado1))
    square.left(50)







#Mantiene el dibujo en pantalla
turtle.mainloop()