from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Valores de traslación
tx = 0.1
ty = 0.3

def display():
    # Limpia la pantalla
    glClear(GL_COLOR_BUFFER_BIT)

    #la matriz actual
    glPushMatrix()

    # Aplicamos la traslación (movemos la figura)
    glTranslatef(tx, ty, 0.0)

    # Color blanco para la figura
    glColor3f(1.0, 1.0, 1.0)

    # Comenzamos a dibujar un cuadrado
    glBegin(GL_QUADS)

    # Vértices del cuadrado
    glVertex2f(-0.2, -0.2)
    glVertex2f( 0.2, -0.2)
    glVertex2f( 0.2,  0.2)
    glVertex2f(-0.2,  0.2)

    # Terminamos la figura
    glEnd()

    # Restauramos la matriz original
    glPopMatrix()

    # Mostramos el resultado en pantalla
    glFlush()

def init():
    # Color de fondo negro
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Configuración de la proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Área de dibujo en 2D
    gluOrtho2D(-1, 1, -1, 1)

    # Volvemos al modo de modelo
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == "__main__":
    # Inicializa GLUT
    glutInit()

    # Configuración de pantalla
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Tamaño de la ventana
    glutInitWindowSize(600, 600)

    # Crear la ventana
    glutCreateWindow(b"Traslacion 2D - Cuadrado")

    # Inicializar configuración
    init()

    # Función que dibuja la figura
    glutDisplayFunc(display)

    # Ejecutar el programa
    glutMainLoop()