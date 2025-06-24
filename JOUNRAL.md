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

Spent some time researching various compoennts! A goal I have for this project is to absolulty minimize costs, something I had not looked at before. This was really, stupidly, hard because camera modules are so abundant... but I wanted to make one myself! I'm glad I was able to. Because of this, the PCB will be very minimalistic, but honestly, it might look better that way; it will fit the monocrome e-ink "instant" display. Here are the fruits from my labor in one cool table!

Shoutout to graphic for GPIO pins becasue this because it helped me so much!

![image](https://github.com/user-attachments/assets/60364239-c47b-45b0-b6e5-3b5d0b20a9df)



| Section              | Item                                 | Part Number / Spec              | Qty | Buy Link                                                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------ | ------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Core**             |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | Raspberry Pi Zero 2 W                | SC1176                          | 1   | [microcenter](https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w)                                                                                                                         |
|                      | Camera Module 3 (12 MP)              | —                               | 1   | [microcenter](https://www.microcenter.com/product/662016/raspberry-pi-camera-3)                                                                                                                         |
|                      | 4.2″ E-Paper 400 × 300 SPI           | Waveshare                       | 1   | [amazon](https://www.amazon.com/dp/B074NR1SW2)                                                                                                                                                                                 |
|                      | microSD Card 64 GB               | SanDisk                    | 1   | [amazon](https://www.amazon.com/SanDisk-Extreme-microSDXC-Memory-Adapter/dp/B09X7C7LL1/ref=sr_1_3?crid=320Q8X6QER81K&dib=eyJ2IjoiMSJ9.3naLhKBzpmRn6meWWyu9XlJG1VLa490W4EmSbMc-GtFk4H8CO2HsG2JndqG9Lmb-5sAIWE0SnwaO3IdUJDbyMPEsZ3olB0wG-mSiad_NUvsy1Yi2glMM1SPDvHxFQuCyLfIdUAKxjmsG2PjXWB6W0rqAd3A3nxNsvap3qkAwAI4T71wwASTwPEx95JZfLch2xQkuBdod2J0ptqn5NEAzVTJ3aVEV5-Ys4spJEy-PZhjGymjhmN0fgMiYrWoOcbNs5vuzTeDBn3SbFIYVFLpCws8QQwcgXJa-IAfs1uOq9Vs.q3INFqkZmacYoFQ7fY3N6CuGDDqK2H0QGx_lNeRIqdA&dib_tag=se&keywords=64+gb+micro+sd&qid=1750746347&s=electronics&sprefix=64+gb+micro+sd%2Celectronics%2C134&sr=1-3) |
| **Power**            |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | 18650 Li-ion 2600 mAh                | W2655B                          | 1   | [microcenter](https://www.microcenter.com/product/659302/performance-tools-18650-li-ion-recharge-battery)                                                                     |
|                      | PowerBoost 1000 C           | Adafruit 1944                   | 1   | [adafruit](https://www.adafruit.com/product/2465?srsltid=AfmBOop7pYqBCCEfueczVoFC1WawLn-4JDxrWe6MvBLNL__PzA9LbI22)                                                                                                                                                                               |
|                      | Main Power Switch SPDT (TH)          |    805               | 1   | [adafruit](https://www.adafruit.com/product/805)                                                                                                                 |
| **User I/O**         |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      |  12mm Square Tactile Button Switch             | 1010                 | 1   | [adafruit](https://www.digikey.com/en/products/detail/omron-electronics-inc-emc-div/B3F-4055/31799](https://www.adafruit.com/product/1010)                                                                           |
| **Headers**          |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | Raspberry Pi Header                     | 3907 | 1   | [adafruit](https://www.adafruit.com/product/3907)                                                                                                                                                                                                                                                           |
| **Passives**         |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | 10 kΩ Resistor      | 2784               | 1   | [adafruit](https://www.adafruit.com/product/2784)                                                                                                                     |
|                      | Decoupling 0.1 µF Ceramic Capacitor     | 753          | 2   | [adafruit](https://www.adafruit.com/product/753)                                                                                                           |
|                      | Bulk Cap 220uF 16V Electrolytic Capacitors  | KEMET T350A106K016AT            | 1   | [adafruit](https://www.adafruit.com/product/2192)                                                                                                             |
| **Mechanical / PCB** |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | Standoffs M2.5 × 10 mm  , Screws M2.5 × 6 mm              | 3299                | 8   | [adafruit](https://www.adafruit.com/product/3299)                                                                                               |
|                      | Custom PCB (2-layer 80 × 60 mm ENIG) | n/a                             | 1   | (JLCPCB / PCBWay whichever is cheaper)                                                                                                                                                                                                                                            |


# June 24

## 10PM -> 3:30AM
Okay so I dont know what I was thinking! So when I first made my BOM, I relied on a lot of Digikey because they have everything... and then I saw their shipping! So to optimize, I re-did my BOM with primarily adafruit to keep shipping costs down (the parts I buy from microcenter will be in-person so no shipping). I don't know why but getting in the zen of making the schematic, I was able to think more clearly about the parts and how to use the PCB as an effective canvas for connecting. I don't know why but with my past interactions with PCBs I tried to make it as flashy and complicated as possible, but with my goal of minimalism with this project, I think I appreciate it as being an effective way to wire everything togehter. I am looking forward to see how it all turns out. In the meantime, here is a picture of my schematic!
<img width="500" alt="Screenshot 2025-06-24 at 3 07 51 AM" src="https://github.com/user-attachments/assets/4aebd592-64fb-4ca1-aec4-a565e4054d58" />



