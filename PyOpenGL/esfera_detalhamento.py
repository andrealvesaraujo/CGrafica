from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
 
import math

n=15  
m=15
r=3
	
 
def esfera():
	
	glBegin(GL_TRIANGLES)
	for j in range(0,n):
		phi= (2*math.pi*j)/(m-1)
		for i in range(0,m):
			teta= i*(math.pi/(n-1)) - math.pi/2 

			#B
			x = r*math.cos(teta)*math.cos(phi)
			y = r*math.sin(teta)
			z = r*math.cos(teta)*math.sin(phi)
			glColor3f(0,1,0)
			glVertex3fv([x,y,z])

			#A
			x2 = r*math.cos(teta)*math.cos(phi+2*math.pi/(m-1))
			y2 = r*math.sin(teta)
			z2 = r*math.cos(teta)*math.sin(phi+2*math.pi/(m-1))
			glColor3f(1,0,0)
			glVertex3fv([x2,y2,z2])

			
			#D
			x3 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi)
			y3 = r*math.sin(teta+math.pi/(n-1))
			z3 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi)
			glColor3f(0,0,1)
			glVertex3fv([x3,y3,z3])


			#A
			x4 = r*math.cos(teta)*math.cos(phi+2*math.pi/(m-1))
			y4 = r*math.sin(teta)
			z4 = r*math.cos(teta)*math.sin(phi+2*math.pi/(m-1))
			glColor3f(10,10,0)
			glVertex3fv([x4,y4,z4])


			#D
			x5 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi)
			y5 = r*math.sin(teta+math.pi/(n-1))
			z5 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi)
			glColor3f(10,0,10)
			glVertex3fv([x5,y5,z5])

			#C
			x6 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi+2*math.pi/(m-1))
			y6 = r*math.sin(teta+math.pi/(n-1))
			z6 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi+2*math.pi/(m-1))
			glColor3f(0,1,1)
			glVertex3fv([x6,y6,z6])


			
		
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
