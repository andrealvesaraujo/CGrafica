from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

import math

def esfera(r,n,m):
	
	glBegin(GL_TRIANGLES)
	for j in range(0,n):
		phi= (2*math.pi*j)/(m-1)
		for i in range(0,m):
			teta= i*(math.pi/(n-1)) - math.pi/2 

			#B
			x = r*math.cos(teta)*math.cos(phi)
			y = r*math.sin(teta)
			z = r*math.cos(teta)*math.sin(phi)
			glNormal3fv([x/r,y/r,z/r])
			glVertex3fv([x,y,z])

			#A
			x2 = r*math.cos(teta)*math.cos(phi+2*math.pi/(m-1))
			y2 = r*math.sin(teta)
			z2 = r*math.cos(teta)*math.sin(phi+2*math.pi/(m-1))
			glNormal3fv([x2/r,y2/r,z2/r])
			glVertex3fv([x2,y2,z2])

			
			#D
			x3 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi)
			y3 = r*math.sin(teta+math.pi/(n-1))
			z3 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi)
			glNormal3fv([x3/r,y3/r,z3/r])
			glVertex3fv([x3,y3,z3])


			#A
			x4 = r*math.cos(teta)*math.cos(phi+2*math.pi/(m-1))
			y4 = r*math.sin(teta)
			z4 = r*math.cos(teta)*math.sin(phi+2*math.pi/(m-1))
			glNormal3fv([x4/r,y4/r,z4/r])
			glVertex3fv([x4,y4,z4])


			#D
			x5 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi)
			y5 = r*math.sin(teta+math.pi/(n-1))
			z5 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi)
			glNormal3fv([x5/r,y5/r,z5/r])
			glVertex3fv([x5,y5,z5])

			#C
			x6 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi+2*math.pi/(m-1))
			y6 = r*math.sin(teta+math.pi/(n-1))
			z6 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi+2*math.pi/(m-1))
			glNormal3fv([x6/r,y6/r,z6/r])
			glVertex3fv([x6,y6,z6])			
		
	glEnd()
	
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    esfera(2,10,10)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
	glViewport(0,0,w,h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,float(w)/float(h),0.1,50.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
	mat_ambient = (0.0, 0.0, 1.0, 1.0)
	mat_diffuse = (0.0, 0.5, 0.5, 1.0)
	mat_specular = (1.0, 1.0, 1.0, 1.0)
	mat_shininess = (50,)
	light_position = (5.0, 5.0, 5.0, 0.0)
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_SMOOTH)

	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_MULTISAMPLE)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,600)
	glutCreateWindow("Esfera Iluminada")
	init()
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutTimerFunc(50,timer,1)
	glutMainLoop()

main()


