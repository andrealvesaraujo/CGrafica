//https://processing.org/reference/

float a =0 ;

void setup(){
   size(500,500); // tamanho na tela
   //rectMode(CENTER);
}

// Loop implicito
void draw(){
  
    /*
    background(200);
   translate(width/2,height/2); // Define o ponto de origem da tela
   int w=80;
   int h=100; // termos em Rosa é variavel global
   rect(mouseX,mouseY,w,h); // Fazer retangulo(x,y,largura,altura) 
   */
   background(200);
   translate(width/2,height/2);
   int r=200;
   int n=4;
   //int n= (int) map(mouseX,0,width,3,20); //Rgra de 3 0-3 e width-20
   float angulo= TWO_PI/n;
   //ellipse(0,0,r*2,r*2);
   beginShape();
   for(int i=0;i<n;i++){
      
     //float x= r * cos(angulo*i);
     //float y= r * sin(angulo*i);
     //float x= r * cos(angulo*i-HALF_PI);
     //float y= r * sin(angulo*i-HALF_PI);
     float x= r * cos(angulo*i-a);
     float y= r * sin(angulo*i-a);
     //ellipse(x,y,5,5);
     vertex(x,y);       // Adiciona um vertice a forma
   } 
   endShape(CLOSE);
   
   a +=0.01;
}  
