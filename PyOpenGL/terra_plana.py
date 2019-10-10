from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
import math

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0

n=15  
m=15
r=3


texture = []

def LoadTextures():
    global texture
    texture = glGenTextures(2)

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='textura/terra_baixa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
	LoadTextures()
	glEnable(GL_TEXTURE_2D)
	glClearColor(0.0, 0.0, 0.0, 0.0)    
	glClearDepth(1.0)                  
	glDepthFunc(GL_LESS)               
	glEnable(GL_DEPTH_TEST)            
	glShadeModel(GL_SMOOTH)            

	glMatrixMode(GL_PROJECTION)
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

	glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1

    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
	global xrot, yrot, zrot, texture

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
	glLoadIdentity()                   

	glClearColor(0.5,0.5,0.5,1.0)            

	glTranslatef(0.0,0.0,-10.0)            

	glRotatef(xrot,1.0,0.0,0.0)          
	glRotatef(yrot,0.0,1.0,0.0)           
	glRotatef(zrot,0.0,0.0,1.0) 
	
	glScalef(1,0.01,1)
    
	glBindTexture(GL_TEXTURE_2D, texture[0])

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
			glTexCoord2f(1-float(j)/(n-1),1-float(i)/(m-1))
			glVertex3fv([x,y,z])

			
			#D
			x3 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi)
			y3 = r*math.sin(teta+math.pi/(n-1))
			z3 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi)
			glColor3f(0,0,1)
			glTexCoord2f(1-float(j)/(n-1),1-float(i+1)/(m-1))
			glVertex3fv([x3,y3,z3])

			#A
			x2 = r*math.cos(teta)*math.cos(phi+2*math.pi/(m-1))
			y2 = r*math.sin(teta)
			z2 = r*math.cos(teta)*math.sin(phi+2*math.pi/(m-1))
			glColor3f(1,0,0)
			glTexCoord2f(1-float(j+1)/(n-1),1-float(i)/(m-1))
			glVertex3fv([x2,y2,z2])

			#A
			x4 = r*math.cos(teta)*math.cos(phi+2*math.pi/(m-1))
			y4 = r*math.sin(teta)
			z4 = r*math.cos(teta)*math.sin(phi+2*math.pi/(m-1))
			glColor3f(10,10,0)
			glTexCoord2f(1-float(j+1)/(n-1),1-float(i)/(m-1))
			glVertex3fv([x4,y4,z4])


			#D
			x5 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi)
			y5 = r*math.sin(teta+math.pi/(n-1))
			z5 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi)
			glColor3f(10,0,10)
			glTexCoord2f(1-float(j)/(n-1),1-float(i+1)/(m-1))
			glVertex3fv([x5,y5,z5])

			#C
			x6 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi+2*math.pi/(m-1))
			y6 = r*math.sin(teta+math.pi/(n-1))
			z6 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi+2*math.pi/(m-1))
			glColor3f(0,1,1)
			glTexCoord2f(1-float(j+1)/(n-1),1-float(i+1)/(m-1))
			glVertex3fv([x6,y6,z6])
			
	glEnd()
    
	xrot  = xrot + 0.35                # X rotation
	#yrot = yrot + 0.30                # Y rotation
	#zrot = zrot + 0.2               # Z rotation

	glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 0.5
        dy = 0
        dz = 0   
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 0.5
        dz = 0   
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 0.5

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print "ESQUERDA"
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print "DIREITA"
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print "CIMA"
    elif tecla == GLUT_KEY_DOWN:
        print "BAIXO"

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Textura")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)

    glutSpecialFunc(teclaEspecialPressionada)

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()
