from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# valores de transformación
tx = 0.3      # traslación en X
ty = 0.2      # traslación en Y
angulo = 45   # rotación
sx = 1.2      # escalación en X
sy = 1.2      # escalación en Y

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Guardamos la matriz original
    glPushMatrix()

    # 1. Traslación (mueve la figura)
    glTranslatef(tx, ty, 0.0)

    # 2. Rotación
    glRotatef(angulo, 0.0, 0.0, 1.0)

    # 3. Escalación
    glScalef(sx, sy, 1.0)

    # Color blanco
    glColor3f(1.0, 1.0, 1.0)

    # Dibujamos un cuadrado
    glBegin(GL_QUADS)
    glVertex2f(-0.2, -0.2)
    glVertex2f( 0.2, -0.2)
    glVertex2f( 0.2,  0.2)
    glVertex2f(-0.2,  0.2)
    glEnd()

    # Restauramos la matriz
    glPopMatrix()

    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1,1,-1,1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Transformaciones: Traslacion + Rotacion + Escalacion")

init()
glutDisplayFunc(display)
glutMainLoop()