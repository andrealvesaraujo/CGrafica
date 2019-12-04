import math

n=15  
m=15
r=3
	
vertices = []
faces =[] 
for j in range(0,n):
	phi= (2*math.pi*j)/(m-1)
	for i in range(0,m):
		teta= i*(math.pi/(n-1)) - math.pi/2 

		#B
		x = r*math.cos(teta)*math.cos(phi)
		y = r*math.sin(teta)
		z = r*math.cos(teta)*math.sin(phi)
		vertices = vertices + [[x,y,z]]

		#A
		x2 = r*math.cos(teta)*math.cos(phi+2*math.pi/(m-1))
		y2 = r*math.sin(teta)
		z2 = r*math.cos(teta)*math.sin(phi+2*math.pi/(m-1))
		
		vertices = vertices + [[x2,y2,z2]]

		
		#D
		x3 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi)
		y3 = r*math.sin(teta+math.pi/(n-1))
		z3 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi)
		
		vertices = vertices + [[x3,y3,z3]]


		#A
		x4 = r*math.cos(teta)*math.cos(phi+2*math.pi/(m-1))
		y4 = r*math.sin(teta)
		z4 = r*math.cos(teta)*math.sin(phi+2*math.pi/(m-1))
		
		vertices = vertices + [[x4,y4,z4]]


		#D
		x5 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi)
		y5 = r*math.sin(teta+math.pi/(n-1))
		z5 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi)
		
		vertices = vertices + [[x5,y5,z5]]

		#C
		x6 = r*math.cos(teta+math.pi/(n-1))*math.cos(phi+2*math.pi/(m-1))
		y6 = r*math.sin(teta+math.pi/(n-1))
		z6 = r*math.cos(teta+math.pi/(n-1))*math.sin(phi+2*math.pi/(m-1))
		
		vertices = vertices + [[x6,y6,z6]]


with open('esfera_resultado.ply', 'w') as f:
    
	f.write("ply\n")
	f.write("format ascii 1.0\n")
	f.write("comment zipper output\n")
	f.write("element vertex " + str(len(vertices)) + "\n")
	f.write("property float x\n")
	f.write("property float y\n")
	f.write("property float z\n")

	f.write("element face \n")
	f.write("property list uchar int vertex_indices\n")
	f.write("end_header\n")

	for i in range(0,len(vertices)):
		f.write(str(vertices[i][0]) +" " + str(vertices[i][1]) +" " + str(vertices[i][2]) + "\n")


'''ply
format ascii 1.0
comment zipper output
element vertex 8
property float x
property float y
property float z
element face 12
property list uchar int vertex_indices
end_header'''