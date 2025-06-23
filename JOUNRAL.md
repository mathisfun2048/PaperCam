title: PaperCam

author: Arya C.

description: this project is to create a digital camera that emulates the feeling of a instant camera through the use of an e-ink display.

created: 06/22/2025


# June 22

## 12PM -> 1PM (1 hour)
So I'm in the middle of my LightBox project (which you should totally check out too!) and I got this idea of making a digital camera feel more like a instant camera! Right now I'm not really researching parts or anything (focusing more on LightBox) but I wanted to start this and add my sketch so I remember my train of thought!

![IMG_4878](https://github.com/user-attachments/assets/3b7688c1-9b4d-46a6-84b0-40c486144ab1)


# June 23

## 3:30PM -> 5:00PM (2 hours)

Spent some time making a BOM!

| Section                      | Component               | Part Number / Spec                    | Qty | Notes                        | Easy-US Source / Link                                                                                        |
| ---------------------------- | ----------------------- | ------------------------------------- | --- | ---------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Core Components**          |                         |                                       |     |                              |                                                                                                              |
|                              | Raspberry Pi Zero 2 W   | SC1176 (RPi Zero 2 W)                 | 1   | Main controller              | [Micro Center](https://www.microcenter.com/product/646257/raspberry-pi-zero-2-w)                             |
|                              | Camera Module 3 (12 MP) | –                                     | 1   | Autofocus HDR                | [Micro Center](https://www.microcenter.com/product/705365/raspberry-pi-camera-module-3)                      |
|                              | 4 .2″ e-Paper Module    | Waveshare 400 × 300 SPI               | 1   | Larger display               | [Amazon](https://www.amazon.com/dp/B074NR1SW2)                                                               |
|                              | microSD Card 32 GB C10  | SanDisk Ultra                         | 1   | Image storage                | [Micro Center](https://www.microcenter.com/product/638846/sandisk-ultra-plus-32gb-microsd)                   |
| **Power Management**         |                         |                                       |     |                              |                                                                                                              |
|                              | 18650 Li-ion 2500 mAh   | –                                     | 1   | Rechargeable cell            | [Micro Center](https://www.microcenter.com/product/485687/inland-18650-37v-2200mah-li-ion-battery)           |
|                              | 18650 Holder            | Keystone 1042                         | 1   | SMT tabs                     | [Digi-Key](https://www.digikey.com/en/products/detail/keystone-electronics/1042/613262)                      |
|                              | PowerBoost 1000 C       | Adafruit 2465                         | 1   | 5 V boost + charger          | [Adafruit](https://www.adafruit.com/product/2465)                                                            |
|                              | Main Power Switch       | C\&K PCM12SMTR                        | 1   | SPDT slide                   | [Digi-Key](https://www.digikey.com/en/products/detail/ck-switches/PCM12SMTR/1813562)                         |
| **User Interface**           |                         |                                       |     |                              |                                                                                                              |
|                              | Shutter Button          | Omron B3F-4055                        | 1   | 12 mm tact                   | [Digi-Key](https://www.digikey.com/en/products/detail/omron-electronics-inc-emc-div/B3F-4055/100661)         |
|                              | Status LED              | Wurth 150080GS75000 (0805 green)      | 1   | External 330 Ω resistor used | [Digi-Key](https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/150080GS75000/5465904)           |
| **Connectivity & Interface** |                         |                                       |     |                              |                                                                                                              |
|                              | USB-C Receptacle        | Amphenol 12401548E4#2A                | 1   | Right-angle                  | [Digi-Key](https://www.digikey.com/en/products/detail/amphenol-icc-fci/12401548E4%23A/10258977)              |
|                              | Hammer Header Kit       | Pimoroni/Adafruit                     | 1   | Low-profile Pi GPIO          | [Adafruit](https://www.adafruit.com/product/3413)                                                            |
| **Flash System**             |                         |                                       |     |                              |                                                                                                              |
|                              | Flash LED               | Luminus SST-20-WDS-B120-L3501         | 1   | 1 W, 5000 K                  | [Digi-Key](https://www.digikey.com/en/products/detail/luminus-devices-inc/SST-20-WDS-B120-L3501/12153024)    |
|                              | MOSFET Driver           | AO3400A (SOT-23)                      | 1   | Switches LED                 | [Digi-Key](https://www.digikey.com/en/products/detail/yangzhou-jiechuang-electronic-co-ltd/AO3400A/14131254) |
|                              | Bulk Capacitor          | Nichicon UWT0J471MNL1GS 470 µF 6 .3 V | 1   | Flash surge buffer           | [Digi-Key](https://www.digikey.com/en/products/detail/nichicon/UWT0J471MNL1GS/3936157)                       |
|                              | Gate Pull-down          | 10 kΩ 0603                            | 1   | Keeps LED off at boot        | [Digi-Key](https://www.digikey.com/en/products/detail/yageo/RC0603JR-0710KL/727615)                          |
|                              | Flash Enable Switch     | C\&K JS102011SAQN                     | 1   | Hardware flash ON/OFF        | [Digi-Key](https://www.digikey.com/en/products/detail/ck-switches/JS102011SAQN/613125)                       |
| **Passive Components**       |                         |                                       |     |                              |                                                                                                              |
|                              | Pull-ups                | Yageo RC0603JR-0710KL 10 kΩ           | 2   | Button inputs                | [Digi-Key](https://www.digikey.com/en/products/detail/yageo/RC0603JR-0710KL/727615)                          |
|                              | Current-limit Resistor  | Yageo RC0603JR-07330RL 330 Ω          | 1   | Status LED series            | [Digi-Key](https://www.digikey.com/en/products/detail/yageo/RC0603JR-07330RL/726769)                         |
|                              | 0 .1 µF Decouplers      | KEMET C0603C104J5R                    | 4   | Local Vcc filtering          | [Digi-Key](https://www.digikey.com/en/products/detail/kemet/C0603C104J5RACTU/411165)                         |
|                              | 10 µF Tantalum          | KEMET T491A106K016AT7280              | 2   | Rail stability               | [Digi-Key](https://www.digikey.com/en/products/detail/kemet/T491A106K016AT7280/8513162)                      |
| **PCB & Mechanical**         |                         |                                       |     |                              |                                                                                                              |
|                              | Custom PCB              | 2-layer 80 × 60 mm                    | 1   | ENIG finish                  | (PCB fab of choice)                                                                                          |
|                              | Standoffs M2 .5 × 10 mm | Keystone 24331                        | 4   | Mount Pi                     | [Digi-Key](https://www.digikey.com/en/products/detail/keystone-electronics/24331/1094544)                    |
|                              | Screws M2 .5 × 6 mm     | Essentra 50M025045G004                | 4   | For standoffs                | [Digi-Key](https://www.digikey.com/en/products/detail/essentra-components/50M025045G004/7327811)             |


