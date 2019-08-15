//https://processing.org/reference/

// Fazer relogio analogico com horas,minutos,segundos
// Tem que ter linhas
// Ve caderno
// Circulo para cada ponteiro

void setup(){
   size(500,500); // tamanho na tela
   
}

// Loop implicito
void draw(){

   background(200,100,100);
   translate(width/2,height/2);
   background(204);
  int s = second();  // Values from 0 - 59
  int m = minute();  // Values from 0 - 59
  int h = hour();    // Values from 0 - 23
  line(s, 0, s, 33);
  line(m, 33, m, 66);
  line(h, 66, h, 100);
   int r=200;
   int n=12;
   //int n= (int) map(mouseX,0,width,3,20); //Rgra de 3 0-3 e width-20
   float angulo= TWO_PI/n;
   //ellipse(0,0,r*2,r*2);
   beginShape();
   for(int i=0;i<n;i++){
      
     //float x= r * cos(angulo*i);
     //float y= r * sin(angulo*i);
     float x= r * cos(angulo*i-HALF_PI);
     float y= r * sin(angulo*i-HALF_PI);
     //ellipse(x,y,5,5);
     vertex(x,y);       // Adiciona um vertice a forma
   } 
   endShape(CLOSE);
   
}  
