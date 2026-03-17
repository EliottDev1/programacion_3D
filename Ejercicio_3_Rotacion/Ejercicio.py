from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Aquí definimos el ángulo de rotación
# Se puede cambiar por 30, 45, 90 o 180 para ver cómo rota la figura
angulo = 180

def display():
    # Limpia la pantalla antes de dibujar
    glClear(GL_COLOR_BUFFER_BIT)

    # Guardamos la matriz actual para no afectar otros objetos
    glPushMatrix()

    # Aplicamos la rotación usando el ángulo definido
    # El último valor (1.0) indica que la rotación es sobre el eje Z
    glRotatef(angulo, 0.0, 0.0, 1.0)

    # Comenzamos a dibujar la figura
    # En este caso un triángulo
    glBegin(GL_TRIANGLES)

    # Primer vértice del triángulo
    glVertex2f(-0.2, -0.2)

    # Segundo vértice
    glVertex2f(0.2, -0.2)

    # Tercer vértice
    glVertex2f(0.0, 0.2)

    # Terminamos de dibujar la figura
    glEnd()

    # Restauramos la matriz original
    glPopMatrix()

    # Muestra lo que se dibujó en pantalla
    glFlush()


# Inicializamos GLUT
glutInit()

# Configuramos el modo de visualización
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

# Tamaño de la ventana
glutInitWindowSize(600, 600)

# Creamos la ventana
glutCreateWindow(b"Rotacion 2D")

# Color de fondo (negro)
glClearColor(0.0, 0.0, 0.0, 1.0)

# Indicamos que función se encargará de dibujar
glutDisplayFunc(display)

# Iniciamos el ciclo principal del programa
glutMainLoop()