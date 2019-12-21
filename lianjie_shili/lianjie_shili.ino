#include <SoftwareSerial.h>
SoftwareSerial softSerial(0,1); //定义软串口,rx为10号端口,tx为11号端口
int x;
int input1 = 9;  //定义输出引脚
int input2 = 8; //定义输出引脚
int input3 = 11; //定义输出引脚
int input4 = 12; //定义输出引脚
int PWMA=3;//定义使能端引脚(下同）
int PWMB=5;

int STBY = 10;




void setup()
{
pinMode(input1,OUTPUT);//下列配置各引脚为输出模式
pinMode(input2,OUTPUT);
pinMode(input3,OUTPUT);
pinMode(input4,OUTPUT);
pinMode(PWMA,OUTPUT);
pinMode(PWMB,OUTPUT);
digitalWrite(STBY, HIGH);
  softSerial.begin(9600); //初始化虚拟串口
  Serial.begin(9600); //初始化硬串口
  
}
String A_String = "";//定义用来存数据的字符串

void loop()
{
  left();
}

void left()
{
  analogWrite(PWMA,255);
  analogWrite(PWMB,100); 
  
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

void right()
{ 
  analogWrite(PWMB,255);
  digitalWrite(input1,LOW); 
  digitalWrite(input2,LOW);  
  digitalWrite(input3,HIGH); 
  digitalWrite(input4,LOW);   
}

