import turtle
import math
import random

# Configuración de la ventana
ANCHO = 800
ALTO = 600

# Configuración de la tortuga
VELOCIDAD_TORTUGA = 15

# Configuración de los objetivos
VELOCIDAD_OBJETIVOS = 10
MAX_OBJETIVOS = 6

# Configuración de los disparos
VELOCIDAD_DISPARO = 20

# Puntuación
puntuacion = 0

# Funciones de movimiento de la tortuga
def mover_arriba():
    tortuga.sety(tortuga.ycor() + VELOCIDAD_TORTUGA)

def mover_abajo():
    tortuga.sety(tortuga.ycor() - VELOCIDAD_TORTUGA)

def mover_izquierda():
    tortuga.setx(tortuga.xcor() - VELOCIDAD_TORTUGA)

def mover_derecha():
    tortuga.setx(tortuga.xcor() + VELOCIDAD_TORTUGA)

# Función de disparo
def disparar():
    global puntuacion
    if disparo.isvisible():
        return
    
    # Mover el disparo a la posición de la tortuga
    disparo.goto(tortuga.xcor(), tortuga.ycor())
    disparo.showturtle()
    
    # Calcular la distancia entre el disparo y los objetivos
    for objetivo in objetivos:
        distancia = math.sqrt(math.pow(disparo.xcor() - objetivo.xcor(), 2) +
                              math.pow(disparo.ycor() - objetivo.ycor(), 2))
        if distancia < 20:
            objetivo.hideturtle()
            objetivo.goto(ANCHO / 2 + random.randint(50, 200), random.randint(-ALTO / 2, ALTO / 2))
            puntuacion += 1
            actualizar_puntuacion()
    
    # Ocultar el disparo después de un tiempo
    pantalla.ontimer(lambda: disparo.hideturtle(), 500)

# Función de actualización de la puntuación
def actualizar_puntuacion():
    puntuacion_turtle.clear()
    puntuacion_turtle.write("Puntuación: {}".format(puntuacion), align="center", font=("Arial", 24, "bold"))

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.setup(ANCHO, ALTO)
pantalla.title("Juego Turtle")

# Crear la tortuga
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("green")
tortuga.penup()

# Crear los objetivos
objetivos = []
for _ in range(MAX_OBJETIVOS):
    objetivo = turtle.Turtle()
    objetivo.shape("circle")
    objetivo.color("red")
    objetivo.penup()
    objetivo.goto(ANCHO / 2 + random.randint(50, 200), random.randint(-ALTO / 2, ALTO / 2))
    objetivos.append(objetivo)

# Crear el disparo
disparo = turtle.Turtle()
disparo.shape("triangle")
disparo.color("blue")
disparo.penup()
disparo.hideturtle()

# Crear el texto de puntuación
puntuacion_turtle = turtle.Turtle()
puntuacion_turtle.penup()
puntuacion_turtle.goto(-ANCHO / 2 + 10, ALTO / 2 - 40)
puntuacion_turtle.color("black")
puntuacion_turtle.write("Puntuación: {}".format(puntuacion), align="left", font=("Arial", 24, "bold"))

# Configurar eventos de teclado
pantalla.onkeypress(mover_arriba, "Up")
pantalla.onkeypress(mover_abajo, "Down")
pantalla.onkeypress(mover_izquierda, "Left")
pantalla.onkeypress(mover_derecha, "Right")
pantalla.onkeypress(disparar, "space")
pantalla.listen()

# Bucle principal del juego
while True:
    for objetivo in objetivos:
        objetivo.setx(objetivo.xcor() - VELOCIDAD_OBJETIVOS)
        
        # Verificar colisión con la tortuga
        if objetivo.distance(tortuga) < 20:
            objetivo.goto(ANCHO / 2 + random.randint(50, 200), random.randint(-ALTO / 2, ALTO / 2))
            puntuacion -= 1
            actualizar_puntuacion()
    
    pantalla.update()

turtle.done()
