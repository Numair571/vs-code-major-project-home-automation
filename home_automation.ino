#include <ESP8266WiFi.h>
#include <ThingSpeak.h>

int bulb=D0;
int fan=D1;

unsigned long channel1=2332537;
unsigned long channel2=2270883;

char* ssid="numair";
char* password="123456789";

WiFiClient client;

void setup() {
  pinMode(bulb,OUTPUT);
  pinMode(fan,OUTPUT);
  Serial.begin(9600);
  WiFi.mode(WIFI_STA);
  Serial.print("Connecting...");
  WiFi.begin(ssid,password);
  while(WiFi.status()!=WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  Serial.println("Connected");
  ThingSpeak.begin(client);
}

void loop() {
  unsigned int bulbStatus=ThingSpeak.readIntField(channel1,1);
  unsigned int fanStatus=ThingSpeak.readIntField(channel2,1);
  Serial.print("Bulb Status: ");
  Serial.print(bulbStatus);
  Serial.print(",Fan Status: ");
  Serial.println(fanStatus);
  if(bulbStatus>0) {
    digitalWrite(bulb,1);
  } else {
    digitalWrite(bulb,0);
  }
  if(fanStatus>0){
    digitalWrite(fan,1);
  } else {
    digitalWrite(fan,0);
  }
  delay(4000);
}
