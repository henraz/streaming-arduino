#include <Wire.h>
#include <BH1750.h>
#include <dht.h>

BH1750 lightMeter;

dht DHT;
#define DHT11_PIN 4

void setup() {
  Serial.begin(9600);
  Wire.begin();
  lightMeter.begin();
}

void loop() {
  uint16_t lux = lightMeter.readLightLevel();
  
  Serial.print(lux);
  Serial.print(",");
  
  Serial.print(DHT.temperature);
  Serial.print(",");
  Serial.println(DHT.humidity);

  delay(10000);
}
