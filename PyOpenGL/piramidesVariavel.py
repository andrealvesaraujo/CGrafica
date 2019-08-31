from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
 
import math
 


  
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5))
 
def piramideVariavel():
    pontos = []
    linhas = []
    faces = []
    n=8
    r=2
    a = 2*math.pi/n
    for i in range(0,n):
        x = r*math.cos(i*a)
        y = 0
        z = r*math.sin(i*a)
        pontos += [[x,y,z]]

    glBegin(GL_TRIANGLE_FAN)
    central=(0,0,0)
    glColor3f(0,0,1)
    glVertex3fv(central)
    i=0
    for ponto in pontos:
        glColor3fv(cores[i%len(cores)])
        glVertex3fv(ponto)
        i+=1    
    glVertex3fv(pontos[0])    
    glEnd()
    
    
    j=0
    topo=(0,5,0)
    for j in range(0,n):
        faces += (topo,j,j+1)
        if ((j+1) == n):
            faces+=(topo,j,0)
    

    #i=0     
    #glBegin(GL_TRIANGLES)   
    #for face in faces:
     #   glColor3fv(cores[i])
      #  for v in face:
       #     glVertex3fv(pontos[v])
       # i+=1
    #glEnd()

 
def desenha():

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glTranslatef(0,0,0)
    glRotatef(2,1,0,0);
    #piramideFixo()
    piramideVariavel()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
