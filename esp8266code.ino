#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const char* ssid = "Parking System";
const char* password = "12345678";

ESP8266WebServer server(80);

#define SENSOR_1 5    
#define SENSOR_2 4   
#define SENSOR_3 13   
#define SENSOR_4 12

LiquidCrystal_I2C lcd(0x27, 16, 2);

void handleStatus() {
  String json = "{";
  json += "\"sensor_1\":\"" + String(digitalRead(SENSOR_1) ? "occupied" : "OK") + "\",";
  json += "\"sensor_2\":\"" + String(digitalRead(SENSOR_2) ? "occupied" : "OK") + "\",";
  json += "\"sensor_3\":\"" + String(digitalRead(SENSOR_3) ? "occupied" : "OK") + "\",";
  json += "\"sensor_4\":\"" + String(digitalRead(SENSOR_4) ? "occupied" : "OK") + "\"";
  json += "}";
  server.send(200, "application/json", json);
}

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  Serial.println("SoftAP Started");
  Serial.println(WiFi.softAPIP());

  pinMode(SENSOR_1, INPUT);
  pinMode(SENSOR_2, INPUT);
  pinMode(SENSOR_3, INPUT);
  pinMode(SENSOR_4, INPUT);

  Wire.begin(0, 2);
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("System Ready");

  server.on("/status", handleStatus);
  server.begin();
}

void loop() {
  server.handleClient();

  bool s1 = digitalRead(SENSOR_1);
  bool s2 = digitalRead(SENSOR_2);
  bool s3 = digitalRead(SENSOR_3);
  bool s4 = digitalRead(SENSOR_4);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("1:");
  lcd.print(s1 ? "OCC" : "OK ");
  lcd.print(" 2:");
  lcd.print(s2 ? "OCC" : "OK ");

  lcd.setCursor(0, 1);
  lcd.print("3:");
  lcd.print(s3 ? "OCC" : "OK ");
  lcd.print(" 4:");
  lcd.print(s4 ? "OCC" : "OK ");

  delay(1000);
}