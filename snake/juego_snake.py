import turtle
import time
import random

posponer = 0.1


#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego de la serpiente")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Cabeza serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Segmentos o cuerpo de la serpiente
segment = []

def arriba():
    head.direction = "up"
def abajo():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"


def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")

while True:
    wn.update()

    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        #Curpo de la serpiente
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segment.append(new_segment)

    #mover el cuerpo de la serpiente
    total_seg = len(segment)
    for index in range(total_seg -1,0,-1):
        x = segment[index -1].xcor()
        y = segment[index -1].ycor()
        segment[index].goto(x,y)

    if total_seg > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)
    


    mov()
    time.sleep(posponer)