from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
 
import math

n=50   
m=50
r=3
	
 
def esfera():
	vertices = []
	
	glBegin(GL_POINTS)
	for i in range(0,n):
		teta= i*(math.pi/(n-1)) - math.pi/2 
		for j in range(0,m):
			phi= (2*math.pi*j)/(m-1)

			x = r*math.cos(teta)*math.cos(phi)
			y = r*math.sin(teta)
			z = r*math.cos(teta)*math.sin(phi)
			
			glVertex3fv([x,y,z])
	glEnd()



       
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,1,0);
    esfera()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera Pontilhada")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
