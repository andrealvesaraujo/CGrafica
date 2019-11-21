from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
 
import math
import sys

xo= -3
xf= 3
yo= -3
yf= 3
nx=50.0
ny=50.0


def paraboloide(x,y):
	return (x**2 + y**2)*0.3
		
def paraboloide_hiperbolico(x,y):
 	return (x**2 - y**2)*0.3

def grid3D():
	deltaY=(yf-yo)/ny
	deltaX=(xf-xo)/nx	
	y=yo
	
	if( len(sys.argv) ==2):
		op = int (sys.argv[1]);
	else:
		op = 1
	while y< yf:
		x=xo
		glBegin(GL_QUAD_STRIP)
		while x<xf:
			glColor3f(1-abs(2.0*x)/(xf-xo),1-abs(2.0*y)/(yf-yo),0)
			if(op == 1):
				glVertex3f(x,y,paraboloide(x,y)) 
				glVertex3f(x,y+deltaY,paraboloide(x,y+deltaY))	
			else:
				glVertex3f(x,y,paraboloide_hiperbolico(x,y))
				glVertex3f(x,y+deltaY,paraboloide_hiperbolico(x,y+deltaY))
			
			x+=deltaX	
		glEnd()
		y+=deltaY
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,-1,0,0)
    grid3D()
    glutSwapBuffers()
    return
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Funcao 1")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,200.0)
glTranslatef(0.0,0.0,-20)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
