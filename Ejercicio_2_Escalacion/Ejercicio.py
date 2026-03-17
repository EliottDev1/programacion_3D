import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Valores de escalación uniforme
sx = 1.3
sy = 1.3

# Valores de escalación no uniforme
sx2 = 1.8
sy2 = 0.7

def display():
    # Limpia la pantalla antes de dibujar
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # TRIÁNGULO CON ESCALACIÓN UNIFORME
    glPushMatrix()

    # Movemos el triángulo hacia la izquierda
    glTranslatef(-0.5, 0.0, 0.0)

    # Escalación uniforme (crece igual en X y Y)
    glScalef(sx, sy, 1.0)

    # Color blanco para la figura
    glColor3f(1.0, 1.0, 1.0)

    # Dibujamos el triángulo
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.2, -0.2)  # vértice inferior izquierdo
    glVertex2f( 0.2, -0.2)  # vértice inferior derecho
    glVertex2f( 0.0,  0.2)  # vértice superior
    glEnd()

    # Restauramos la matriz original
    glPopMatrix()


    # TRIÁNGULO CON ESCALACIÓN NO UNIFORME 
    glPushMatrix()

    # Movemos el triángulo hacia la derecha para que no se encime
    glTranslatef(0.6, 0.0, 0.0)

    # Escalación no uniforme (cada eje cambia diferente)
    glScalef(sx2, sy2, 1.0)

    # Color blanco
    glColor3f(1.0, 1.0, 1.0)

    # Dibujamos otro triángulo
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.2, -0.2)
    glVertex2f( 0.2, -0.2)
    glVertex2f( 0.0,  0.2)
    glEnd()

    # Restauramos la matriz
    glPopMatrix()

    # Muestra el resultado en la ventana
    glFlush()


def init():
    # Color de fondo negro
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Configuración de la proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Área de dibujo en 2D
    gluOrtho2D(-1, 1, -1, 1)

    # Regresamos al modo de modelo
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# Inicializa GLUT
glutInit(sys.argv)

# Configuración de la ventana
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

# Tamaño de la ventana
glutInitWindowSize(600, 600)

# Crear la ventana
glutCreateWindow(b"Escalacion uniforme y no uniforme")

# Inicializar configuración
init()

# Función que dibuja en pantalla
glutDisplayFunc(display)

# Ejecuta el programa
glutMainLoop()