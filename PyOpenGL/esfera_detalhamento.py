from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
 
import math

n=10   
m=10
r=3
	
 
def esfera():
	circ2 = [] 	
	for i in range(0,n):
		teta= i*(math.pi/(n-1)) - math.pi/2 
		circ1 = []
		for j in range(0,m):
			phi= (2*math.pi*j)/(m-1)

			x = r*math.cos(teta)*math.cos(phi)
			y = r*math.sin(teta)
			z = r*math.cos(teta)*math.sin(phi)
			
			circ1 += [[x,y,z]]

		circ2+=[circ1]
	
    
	glBegin(GL_TRIANGLES)
	for i in range(0,len(circ2)):
		a= circ2[i]
		for j in range(-1,len(a)):
			glVertex3fv(a[j])
		
	glEnd()


       
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,1,0);
    esfera()
    glutSwapBuffers()
    return;
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera Diferente")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
