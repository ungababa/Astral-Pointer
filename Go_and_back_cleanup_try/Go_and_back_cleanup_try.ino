const int stepX = 2;
const int dirX  = 5;

const int stepY = 3;
const int dirY  = 6;

const int enPin = 8;

float stepsPerRevolutionAz = 200;
float stepsPerRevolutionAzfin = 200;

float stepsAz = 0;
float stepsAzfin = 0;

float stepsPerRevolutionAl = 200;
float stepsPerRevolutionAlfin = 200;

float stepsAl = 0;
float stepsAlfin = 0;

void setup() 
{
  Serial.begin(9600);

  pinMode(stepX,OUTPUT);
  pinMode(dirX,OUTPUT);

  pinMode(stepY,OUTPUT);
  pinMode(dirY,OUTPUT);

  pinMode(enPin,OUTPUT);

  digitalWrite(enPin,LOW);
  digitalWrite(dirX,LOW);
  digitalWrite(dirY,HIGH);
}

void loop()
  {
  Serial.println("Enter Your Azimuth");
  while(Serial.available()==0)
  {

  }
  
  stepsAz=Serial.parseInt();
  
  if (stepsAz<361&&stepsAz>-1)
  {
    stepsAz= stepsAz-stepsAzfin;
    stepsAzfin=stepsAz+stepsAzfin;
    Serial.print("Your Azimuth is: ");
    Serial.println(stepsAz);
    stepsPerRevolutionAz = map(stepsAz, 0, 360, 0, 800);
    Serial.print("Your steps for Azimuth is ");
    Serial.println(stepsPerRevolutionAz);
  
    if(stepsPerRevolutionAz>0)
    {   
      pcwspinAz (stepX,dirX,stepsPerRevolutionAz);
    } 

    else if (stepsPerRevolutionAz<0)
    {  
      nccwspinAz (stepX,dirX,stepsPerRevolutionAz);
    }
  }

  else
  {
    Serial.println("Your number needs to be in between 0 and 360");
  }
  delay(1000);  

Serial.println("Enter Your Altitude");
  while(Serial.available()==0)
  {
  } 

  stepsAl=Serial.parseInt();
  if (stepsAl<91&&stepsAl>-46)
  {
    stepsAl= stepsAl-stepsAlfin;
    stepsAlfin=stepsAl+stepsAlfin;
    Serial.print("Your Altitude is: ");
    Serial.println(stepsAl);
    stepsPerRevolutionAl = map(stepsAl, 0, 360, 0, 640);
    Serial.print("Your steps for Altitude is ");
    Serial.println(stepsPerRevolutionAl);
  
    if(stepsPerRevolutionAl>0)
    {   
      pcwspinAl (stepY,dirY,stepsPerRevolutionAl);     
    }  

    else if (stepsPerRevolutionAl<0)
    {
      nccwspinAl (stepY,dirY,stepsPerRevolutionAl);  
      delayMicroseconds(1000);    
    }
  }
  else
  {
    Serial.println("Your number needs to be in between 0 and 90");
  }
  delay(1000); 
} 

void pcwspinAz(int step,int dir,float num)
{
  digitalWrite(dir,LOW);
  for(int x = 0; x < num; x++) 
  {
  digitalWrite(step,HIGH);
  delayMicroseconds(1000);

  digitalWrite(step,LOW);
  delayMicroseconds(1000);
  }
}

void nccwspinAz(int step, int dir, float num)
{
  digitalWrite(dir,HIGH);
  for(int x = 0; x > num; x--) 
  {
  digitalWrite(step,HIGH);
  delayMicroseconds(1000);

  digitalWrite(step,LOW);
  delayMicroseconds(1000);
  }
}

void pcwspinAl(int step,int dir,float num)
{
  digitalWrite(dir,HIGH);
  for(int x = 0; x < num; x++) 
  {
  digitalWrite(step,HIGH);
  delayMicroseconds(1000);

  digitalWrite(step,LOW);
  delayMicroseconds(1000);
  }
}

void nccwspinAl(int step, int dir, float num)
{
  digitalWrite(dir,LOW);

  for(int x = 0; x > num; x--) 
  {
  digitalWrite(step,HIGH);
  delayMicroseconds(1000);

  digitalWrite(step,LOW);
  delayMicroseconds(1000);
  }
}