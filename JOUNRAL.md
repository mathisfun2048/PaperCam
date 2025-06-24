title: PaperCam

author: Arya C.

description: this project is to create a digital camera that emulates the feeling of a instant camera through the use of an e-ink display.

created: 06/22/2025


# June 22

## 12PM -> 1PM (1 hour)
So I'm in the middle of my LightBox project (which you should totally check out too!) and I got this idea of making a digital camera feel more like a instant camera! Right now I'm not really researching parts or anything (focusing more on LightBox) but I wanted to start this and add my sketch so I remember my train of thought!

![IMG_4878](https://github.com/user-attachments/assets/3b7688c1-9b4d-46a6-84b0-40c486144ab1)


# June 23

## 3:30PM -> 5:30PM, 6PM -> 10PM (6 hours)

Spent some time researching various compoennts! A goal I have for this project is to absolulty minimize costs, something I had not looked at before. Because of this, I tried a very minamalistic desing fro my PCB. Here are the fruits from my labor in one cool table!

| Section              | Item                                 | Part Number / Spec              | Qty | Buy Link                                                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------ | ------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Core**             |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | Raspberry Pi Zero 2 W                | SC1176                          | 1   | [microcenter](https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w)                                                                                                                         |
|                      | Camera Module 3 (12 MP)              | —                               | 1   | [microcenter](https://www.microcenter.com/product/662016/raspberry-pi-camera-3)                                                                                                                         |
|                      | 4.2″ E-Paper 400 × 300 SPI           | Waveshare                       | 1   | [amazon](https://www.amazon.com/dp/B074NR1SW2)                                                                                                                                                                                 |
|                      | microSD Card 32 GB C10               | SanDisk Ultra                   | 1   | [amazon](https://www.amazon.com/SanDisk-Extreme-microSDXC-Memory-Adapter/dp/B09X7C7LL1/ref=sr_1_3?crid=320Q8X6QER81K&dib=eyJ2IjoiMSJ9.3naLhKBzpmRn6meWWyu9XlJG1VLa490W4EmSbMc-GtFk4H8CO2HsG2JndqG9Lmb-5sAIWE0SnwaO3IdUJDbyMPEsZ3olB0wG-mSiad_NUvsy1Yi2glMM1SPDvHxFQuCyLfIdUAKxjmsG2PjXWB6W0rqAd3A3nxNsvap3qkAwAI4T71wwASTwPEx95JZfLch2xQkuBdod2J0ptqn5NEAzVTJ3aVEV5-Ys4spJEy-PZhjGymjhmN0fgMiYrWoOcbNs5vuzTeDBn3SbFIYVFLpCws8QQwcgXJa-IAfs1uOq9Vs.q3INFqkZmacYoFQ7fY3N6CuGDDqK2H0QGx_lNeRIqdA&dib_tag=se&keywords=64+gb+micro+sd&qid=1750746347&s=electronics&sprefix=64+gb+micro+sd%2Celectronics%2C134&sr=1-3) |
| **Power**            |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | 18650 Li-ion 2600 mAh                | W2655B                          | 1   | [microcenter](https://www.microcenter.com/product/659302/performance-tools-18650-li-ion-recharge-battery)                                                                     |
|                      | PowerBoost 1000 C           | Adafruit 1944                   | 1   | [adafruit](https://www.adafruit.com/product/2465?srsltid=AfmBOop7pYqBCCEfueczVoFC1WawLn-4JDxrWe6MvBLNL__PzA9LbI22)                                                                                                                                                                               |
|                      | Main Power Switch SPDT (TH)          |    805               | 1   | [adafruit](https://www.adafruit.com/product/805)                                                                                                                 |
| **User I/O**         |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | Shutter Button 12 mm (TH)            | Omron B3F-4055                  | 1   | [digikey](https://www.digikey.com/en/products/detail/omron-electronics-inc-emc-div/B3F-4055/31799)                                                                           |
| **Headers**          |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | GPIO Connector                       | I have one! | 1   | n/a                                                                                                                                                                                                                                                           |
| **Passives**         |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | Pull-up Resistor 10 kΩ ¼ W TH        | Yageo CF14JT10K0                | 1   | [digikey](https://www.digikey.com/en/products/detail/yageo/CF14JT10K0/732458)                                                                                                                     |
|                      | Decoupling Cap 0.1 µF 50 V radial    | KEMET C317C104M5U5TA            | 2   | [digikey](https://www.digikey.com/en/products/detail/kemet/C317C104M5U5TA/1816789)                                                                                                           |
|                      | Bulk Cap 10 µF 16 V radial tantalum  | KEMET T350A106K016AT            | 1   | [digikey](https://www.digikey.com/en/products/detail/kemet/T350A106K016AT/861299)                                                                                                             |
| **Mechanical / PCB** |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | Standoffs M2.5 × 10 mm               | Keystone 24331                  | 4   | [digikey](https://www.digikey.com/en/products/detail/keystone-electronics/24331/1532906)                                                                                               |
|                      | Screws M2.5 × 6 mm (nylon)           | Essentra 50M025045G004          | 4   | [digikey](https://www.digikey.com/en/products/detail/essentra-components/50M025045G004/11638842)                                                                               |
|                      | Custom PCB (2-layer 80 × 60 mm ENIG) | n/a                             | 1   | (JLCPCB / PCBWay whichever is cheaper)                                                                                                                                                                                                                                            |
