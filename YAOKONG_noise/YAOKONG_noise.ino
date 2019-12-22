#include <SoftwareSerial.h>
SoftwareSerial softSerial(0,1); //定义软串口,rx为10号端口,tx为11号端口
int x;
int input1 = 9;  //定义输出引脚
int input2 = 8; //定义输出引脚
int input3 = 11; //定义输出引脚
int input4 = 12; //定义输出引脚
int PWMA=3;//定义使能端引脚(下同）
int PWMB=5;

int noise = 13;

int STBY = 10;                 




void setup()
{
pinMode(input1,OUTPUT);//下列配置各引脚为输出模式
pinMode(input2,OUTPUT);
pinMode(input3,OUTPUT);
pinMode(input4,OUTPUT);
pinMode(PWMA,OUTPUT);
pinMode(PWMB,OUTPUT);
pinMode(noise,OUTPUT);
digitalWrite(STBY, HIGH);
  softSerial.begin(9600); //初始化虚拟串口
  Serial.begin(9600); //初始化硬串口
  
}
String A_String = "";//定义用来存数据的字符串

void left()
{
  analogWrite(PWMA,160);
  analogWrite(PWMB,255); 
  
  digitalWrite(input1,HIGH); 
  digitalWrite(input2,LOW);  
  digitalWrite(input3,HIGH); 
  digitalWrite(input4,LOW);   
}

void right()
{
  analogWrite(PWMA,255);
  analogWrite(PWMB,160); 
  
  digitalWrite(input1,HIGH); 
  digitalWrite(input2,LOW);  
  digitalWrite(input3,HIGH); 
  digitalWrite(input4,LOW);   
}


void stop1()
{
 
  digitalWrite(input1,LOW); 
  digitalWrite(input2,LOW);  
  digitalWrite(input3,LOW); 
  digitalWrite(input4,LOW);   
}



void stright()
{ 
  analogWrite(PWMA,255);
  analogWrite(PWMB,255); 
  
  digitalWrite(input1,HIGH); 
  digitalWrite(input2,LOW);  
  digitalWrite(input3,HIGH); 
  
  digitalWrite(input4,LOW);   
}

void bright()
{
  analogWrite(PWMA,255);
  analogWrite(PWMB,160); 
  
  digitalWrite(input1,LOW); 
  digitalWrite(input2,HIGH);  
  digitalWrite(input3,LOW); 
  digitalWrite(input4,HIGH);   
}

void bleft()
{ 
  analogWrite(PWMA,160);
  analogWrite(PWMB,255); 
  
  digitalWrite(input1,LOW); 
  digitalWrite(input2,HIGH);  
  digitalWrite(input3,LOW); 
  digitalWrite(input4,HIGH);   
}

void bstright()
{ 
  analogWrite(PWMA,255);
  analogWrite(PWMB,255); 
  
  digitalWrite(input1,LOW); 
  digitalWrite(input2,HIGH);  
  digitalWrite(input3,LOW); 
  
  digitalWrite(input4,HIGH);   
}


void nbleft()
{   
    analogWrite(PWMA,160);
    analogWrite(PWMB,255); 
  
    digitalWrite(input1,HIGH); 
    digitalWrite(input2,LOW);  
    digitalWrite(input3,HIGH); 
    digitalWrite(input4,LOW);

    delay(1000);
  
    analogWrite(PWMA,255);
    analogWrite(PWMB,160); 
  
    digitalWrite(input1,LOW); 
    digitalWrite(input2,HIGH);  
    digitalWrite(input3,LOW); 
    digitalWrite(input4,HIGH);
  
    delay(1000);
}
void nbright()
{   
    analogWrite(PWMA,255);
    analogWrite(PWMB,160); 
  
    digitalWrite(input1,HIGH); 
    digitalWrite(input2,LOW);  
    digitalWrite(input3,HIGH); 
    digitalWrite(input4,LOW);

    delay(1000);
  
    analogWrite(PWMA,160);
    analogWrite(PWMB,255); 
  
    digitalWrite(input1,LOW); 
    digitalWrite(input2,HIGH);  
    digitalWrite(input3,LOW); 
    digitalWrite(input4,HIGH);
  
    delay(1000);
}

void soundon()
{
  digitalWrite(noise,HIGH);
}

void soundoff()
{
  digitalWrite(noise,LOW);
}


void loop()
{
  
  
  
  if (softSerial.available() > 0) //判断软串口是否接收到openmv数据，然后读取，然后在串口监视器打印
  {
    if(softSerial.peek() != '\n')
    {
      A_String += (char)softSerial.read();//把串口读的单个字符逐加到字符串
    }
    else
    {
      softSerial.read();
     
      
       x=A_String.toInt();//把字符串转成int类型存放
   
       if(x==1)//坐标和阈值进行判断
       {
        Serial.println("1");//串口打印数字1
          Serial.println(x);//串口打印坐标
         left();//左转
       }
       else if(x==3)
       {
         Serial.println("3");//串口打印数字2
          Serial.println(x);//串口打印坐标
          right();//右转
       }
       else if(x==2)
       {
         Serial.println("2");//串口打印数字2
          Serial.println(x);//串口打印坐标
          stright();
       }
       else if(x==4)
       {
         Serial.println("4");//串口打印数字2
          Serial.println(x);//串口打印坐标
          bleft();
       }         
       else if(x==5)
       {
         Serial.println("5");//串口打印数字2
          Serial.println(x);//串口打印坐标
          bstright();   
       }    
       else if(x==6)
       {
         Serial.println("6");//串口打印数字2
          Serial.println(x);//串口打印坐标
          bright();  
       }             
       else if(x==7)
       {
         Serial.println("7");//串口打印数字2
          Serial.println(x);//串口打印坐标
          nbleft();
       }       
       else if(x==9)
       {
         Serial.println("9");//串口打印数字2
          Serial.println(x);//串口打印坐标
          nbright();
       }
       else if(x==10)
       {
         Serial.println("10");//串口打印数字2
          Serial.println(x);//串口打印坐标
          soundon();
       }
       else if(x==11)
       {
         Serial.println("11");//串口打印数字2
          Serial.println(x);//串口打印坐标
          soundoff();          
       }       
       else
       {
        stop1();//停转
       }
       A_String = "";//重置字符串
    }
  }
}
