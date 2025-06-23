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

Spent some time researching various compoennts! The goal for this is to keap cost down adn keep it minimalistic. Spent the rest of the time formating everything in a BOM!

| Section        | Item                     | Part No. / Spec               | Qty | Notes                     | Buy Link                                                                                                                                                                                       |
| -------------- | ------------------------ | ----------------------------- | --- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core**       | Raspberry Pi Zero 2 W    | SC1176                        | 1   | Main controller           | [https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w](https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w)                                                           |
|                | Camera Module 3 (12 MP)  | —                             | 1   | HDR / AF                  | [https://www.microcenter.com/product/662016/raspberry-pi-camera-3](https://www.microcenter.com/product/662016/raspberry-pi-camera-3)                                                           |
|                | 4.2″ E-Paper Module      | Waveshare 400 × 300 SPI       | 1   | Display                   | [https://www.amazon.com/dp/B074NR1SW2](https://www.amazon.com/dp/B074NR1SW2)                                                                                                                   |
|                | microSD Card 32 GB C10   | SanDisk Ultra                 | 1   | Storage                   | [https://www.microcenter.com/product/675332/sandisk-32gb-ultra-microsdxc-class-10](https://www.microcenter.com/product/675332/sandisk-32gb-ultra-microsdxc-class-10)                           |
| **Power**      | 18650 Li-ion Cell        | W2655B (2600 mAh)             | 1   | Battery                   | [https://www.microcenter.com/product/659302/performance-tools-18650-li-ion-recharge-battery](https://www.microcenter.com/product/659302/performance-tools-18650-li-ion-recharge-battery)       |
|                | 18650 Holder (SMD)       | Keystone 1042                 | 1   | SMT tabs                  | [https://www.digikey.com/en/products/detail/keystone-electronics/1042/2745668](https://www.digikey.com/en/products/detail/keystone-electronics/1042/2745668)                                   |
|                | PowerBoost 1000 C        | Adafruit 2465                 | 1   | 5 V boost + charger       | [https://www.adafruit.com/product/2465](https://www.adafruit.com/product/2465)                                                                                                                 |
|                | Main Power Switch        | C\&K PCM12SMTR                | 1   | SPDT slide                | [https://www.digikey.com/en/products/detail/c-k/PCM12SMTR/1640112](https://www.digikey.com/en/products/detail/c-k/PCM12SMTR/1640112)                                                           |
| **User I/O**   | Shutter Button           | Omron B3F-4055                | 1   | 12 mm tact                | [https://www.digikey.com/en/products/detail/omron-electronics-inc-emc-div/B3F-4055/31799](https://www.digikey.com/en/products/detail/omron-electronics-inc-emc-div/B3F-4055/31799)             |
| **Connectors** | USB-C Receptacle         | GCT USB4080-03-A              | 1   | R/A SMT, in stock         | [https://www.digikey.com/en/products/detail/gct/USB4080-03-A/14659819](https://www.digikey.com/en/products/detail/gct/USB4080-03-A/14659819)                                                   |
|                | Hammer-Header Kit        | Pimoroni / Adafruit           | 1   | Solder-less Pi GPIO       | [https://www.adafruit.com/product/3413](https://www.adafruit.com/product/3413)                                                                                                                 |
| **Flash**      | Flash LED                | Luminus SST-20-WDS-B120-L3501 | 1   | 1 W, 5000 K               | [https://www.digikey.com/en/products/detail/luminus-devices-inc/SST-20-WDS-B120-L3501/15903651](https://www.digikey.com/en/products/detail/luminus-devices-inc/SST-20-WDS-B120-L3501/15903651) |
|                | MOSFET Driver            | AO3400A (SOT-23)              | 1   | N-ch load switch          | [https://www.digikey.com/en/products/detail/alpha-omega-semiconductor-inc/AO3400A/1855772](https://www.digikey.com/en/products/detail/alpha-omega-semiconductor-inc/AO3400A/1855772)           |
|                | Flash Bulk Cap           | Nichicon UWT0J471MNL1GS       | 1   | 470 µF 6.3 V              | [https://www.digikey.com/en/products/detail/nichicon/UWT0J471MNL1GS/589899](https://www.digikey.com/en/products/detail/nichicon/UWT0J471MNL1GS/589899)                                         |
|                | 10 kΩ × 4 Resistor Array | Bourns CAY16-103J4LF          | 1   | Pull-ups + gate pull-down | [https://www.digikey.com/en/products/detail/bourns-inc/CAY16-103J4LF/431579](https://www.digikey.com/en/products/detail/bourns-inc/CAY16-103J4LF/431579)                                       |
|                | Flash-Enable Switch      | C\&K JS102011SAQN             | 1   | ON/OFF gate               | [https://www.digikey.com/en/products/detail/c-k/JS102011SAQN/1640095](https://www.digikey.com/en/products/detail/c-k/JS102011SAQN/1640095)                                                     |
| **Passives**   | 0.1 µF Decouplers        | KEMET C0603C104J5RACTU        | 4   | Vcc filtering             | [https://www.digikey.com/en/products/detail/kemet/C0603C104J5RACTU/2199772](https://www.digikey.com/en/products/detail/kemet/C0603C104J5RACTU/2199772)                                         |
|                | 10 µF Tantalum           | KEMET T491A106K016AT7280      | 2   | Rail stability            | [https://www.digikey.com/en/products/detail/kemet/T491A106K016AT7280/8612808](https://www.digikey.com/en/products/detail/kemet/T491A106K016AT7280/8612808)                                     |
| **Mech.**      | Standoffs M2.5 × 10 mm   | Keystone 24331                | 4   | Mount Pi                  | [https://www.digikey.com/en/products/detail/keystone-electronics/24331/1532906](https://www.digikey.com/en/products/detail/keystone-electronics/24331/1532906)                                 |
|                | Screws M2.5 × 6 mm       | Essentra 50M025045G004        | 4   | Nylon pan-head            | [https://www.digikey.com/en/products/detail/essentra-components/50M025045G004/11638842](https://www.digikey.com/en/products/detail/essentra-components/50M025045G004/11638842)                 |
|                | Custom PCB               | 2-layer, 80 × 60 mm           | 1   | ENIG finish               | (JLCPCB / PCBWay)                                                                                                                                                                              |
