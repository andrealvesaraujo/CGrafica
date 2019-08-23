float[] roda(float cx, float cy, float px, float py, float a )
{
  float _px = ((px-cx)*cos(a)-(py-cy)*sin(a))+cx;
  float _py = ((px-cx)*sin(a)+(py-cy)*cos(a))+cy;
  return new float[] { _px, _py };
}
float maximo=6;
void koch(float x0,float y0,float xf,float yf,float nivel)
  {
    
    if(nivel == maximo)
    {
       beginShape();
      line(round(x0),round(y0),round(xf),round(yf));
      endShape(CLOSE);
    }
    else
    {
      float x1 = (1-(1/3.0))*x0 + (1/3.0)*xf;
      float y1 = (1-(1/3.0))*y0 + (1/3.0)*yf;
      float x3 = (1-(2/3.0))*x0 + (2/3.0)*xf;
      float y3 = (1-(2/3.0))*y0 + (2/3.0)*yf;
      float[] P= roda(x1,y1,x3,y3,-PI/3);
      koch(x1,y1,P[0],P[1],nivel+1);
      koch(P[0],P[1],x3,y3,nivel+1);
      koch(x0,y0,x1,y1,nivel+1);
      koch(x3,y3,xf,yf,nivel+1);
    }
  }

void setup() 
{
  size(500,500);
}

void draw()
{
  background(204);
  
  koch(0,height/2,width,height/2,4);
}
