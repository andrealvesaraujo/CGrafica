//https://processing.org/reference/
void setup(){
   size(500,500); // tamanho na tela
   
}


void draw(){

   background(200,100,100);
   translate(width/2,height/2);
   background(204);
  int s = second();  // Values from 0 - 59
  int m = minute();  // Values from 0 - 59
  int h = hour();    // Values from 0 - 23  
   int r=200;
   int n=12;
   float anguloRetaPrincipal= TWO_PI/n;
   float anguloRetaPequeno= TWO_PI/60;
  
   h=h%12;
  
   float Hx,Hy;
   float Mx,My;
   float Sx,Sy;
   Hx= (r-60) * cos(((h+m/60.0)*PI/6.0) - PI/2);
   Hy= (r-60) * sin(((h+m/60.0)*PI/6.0) - PI/2);
   
   Mx= (r-30) * cos(((m*PI)/30.0) - PI/2);
   My= (r-30) * sin(((m*PI)/30.0) - PI/2);
   
   Sx= (r-30) * cos(((s*PI)/30.0) - PI/2);
   Sy= (r-30) * sin(((s*PI)/30.0) - PI/2);
    
   ellipse(0,0,r*2,r*2);
   line(0,0,Hx,Hy);
   line(0,0,Mx,My);
   line(0,0,Sx,Sy);
   
   beginShape();
   
   for(int i=0;i<12;i++){
     float Px= r * cos(anguloRetaPrincipal*i-HALF_PI);
     float Py= r * sin(anguloRetaPrincipal*i-HALF_PI);     
     
     float Qx= (r-30) * cos(anguloRetaPrincipal*i-HALF_PI);
     float Qy= (r-30) * sin(anguloRetaPrincipal*i-HALF_PI);
     
     line(Px,Py,Qx,Qy);
     
     
   } 
   for(int i=0;i<60;i++){
     float Zx= r * cos(anguloRetaPequeno*i-HALF_PI);
     float Zy= r * sin(anguloRetaPequeno*i-HALF_PI);
     
     float Wx= (r-10) * cos(anguloRetaPequeno*i-HALF_PI);
     float Wy= (r-10) * sin(anguloRetaPequeno*i-HALF_PI);
     
     line(Zx,Zy,Wx,Wy);
     
   } 
   endShape(CLOSE);
   
}  
