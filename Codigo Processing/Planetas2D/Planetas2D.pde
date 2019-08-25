float velocidadeTS = 0.0;
float velocidadeTL = 0.0;

float[] roda(float cx, float cy, float px, float py, float a )
{
  float _px = ((px-cx)*cos(a)-(py-cy)*sin(a))+cx;
  float _py = ((px-cx)*sin(a)+(py-cy)*cos(a))+cy;
  return new float[] { _px, _py };
}

void setup() 
{
  size(500,500);
}

void draw()
{
  background(200);
  
  float Sx=(width/2);
  float Sy=(height/2);
  float rSol=60;
  
  float Tx=100+rSol;
  float Ty=100-rSol;
  float rTerra=30;
  float anguloS_T=PI/4;
  
  translate(Sx,Sy);
  circle(0,0,rSol*2);
  
  float NovoT[]= roda(0,0,Tx,Ty,-(anguloS_T+velocidadeTS)); 
  circle(NovoT[0],NovoT[1],rTerra*2);
  
  float Lx=NovoT[0]+40;
  float Ly=NovoT[1]+40;
  float rLua=10;
  float anguloT_L=PI/4;
  
  float NovoL[]= roda(NovoT[0],NovoT[1],Lx,Ly,-(anguloT_L-velocidadeTL)); 
  circle(NovoL[0],NovoL[1],rLua*2);
   
  velocidadeTS+=0.01;
  velocidadeTL+=0.1;
}
