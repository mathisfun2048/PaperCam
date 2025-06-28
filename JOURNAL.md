---
title: "PaperCam"
author: "Arya CC"
description: "this project is to create a digital camera that emulates the feeling of a instant camera through the use of an e-ink display."
created_at: "06/22/2025"
---
total hours so far: 27 hours


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
|                      | Camera              | —                               | 1   | [adafruit](https://www.adafruit.com/product/5657)                                                                                                                         |
|                      | 4.2″ E-Paper 400 × 300 SPI           | Waveshare                       | 1   | [amazon](https://www.amazon.com/dp/B074NR1SW2)                                                                                                                                                                                 |
|                      | microSD Card 64 GB               | SanDisk                    | 1   | [amazon](https://www.amazon.com/SanDisk-Extreme-microSDXC-Memory-Adapter/dp/B09X7C7LL1/ref=sr_1_3?crid=320Q8X6QER81K&dib=eyJ2IjoiMSJ9.3naLhKBzpmRn6meWWyu9XlJG1VLa490W4EmSbMc-GtFk4H8CO2HsG2JndqG9Lmb-5sAIWE0SnwaO3IdUJDbyMPEsZ3olB0wG-mSiad_NUvsy1Yi2glMM1SPDvHxFQuCyLfIdUAKxjmsG2PjXWB6W0rqAd3A3nxNsvap3qkAwAI4T71wwASTwPEx95JZfLch2xQkuBdod2J0ptqn5NEAzVTJ3aVEV5-Ys4spJEy-PZhjGymjhmN0fgMiYrWoOcbNs5vuzTeDBn3SbFIYVFLpCws8QQwcgXJa-IAfs1uOq9Vs.q3INFqkZmacYoFQ7fY3N6CuGDDqK2H0QGx_lNeRIqdA&dib_tag=se&keywords=64+gb+micro+sd&qid=1750746347&s=electronics&sprefix=64+gb+micro+sd%2Celectronics%2C134&sr=1-3) |
| **Power**            |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | 18650 Li-ion 2600 mAh                | W2655B                          | 1   | [microcenter](https://www.microcenter.com/product/659302/performance-tools-18650-li-ion-recharge-battery)                                                                     |
|                      | PowerBoost 1000 C           | Adafruit 1944                   | 1   | [adafruit](https://www.adafruit.com/product/2465?srsltid=AfmBOop7pYqBCCEfueczVoFC1WawLn-4JDxrWe6MvBLNL__PzA9LbI22)                                                                                                                                                                               |
|                      | Main Power Switch SPDT (TH)          |    805               | 1   | [adafruit](https://www.adafruit.com/product/805)                                                                                                                 |
| **User I/O**         |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      |  12mm Square Tactile Button Switch             | 1010                 | 1   | [adafruit](https://www.adafruit.com/product/1010)                                                                           |
| **Headers**          |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | Raspberry Pi Header                     | 3907 | 1   | [adafruit](https://www.adafruit.com/product/3907)                                                                                                                                                                                                                                                           |
| **Passives**         |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      | 10 kΩ Resistor      | 2784               | 1   | [adafruit](https://www.adafruit.com/product/2784)                                                                                                                     |
|                      | Decoupling 0.1 µF Ceramic Capacitor     | 753          | 2   | [adafruit](https://www.adafruit.com/product/753)                                                                                                           |
|                      | Bulk Cap 220uF 16V Electrolytic Capacitors  | 2192            | 1   | [adafruit](https://www.adafruit.com/product/2192)                                                                                                             |
| **Mechanical / PCB** |                                      |                                 |     |                                                                                                                                                                                                                                                              |
|                      |  Screws M2.5 × 6 mm * 5, M2.5 x 10 mm * 4              | 3299                | 8   | [adafruit](https://www.adafruit.com/product/3299)                                                                                               |
|                      | Custom PCB (2-layer 110 × 110 mm ENIG) | n/a                             | 1   | (JLCPCB / PCBWay whichever is cheaper)                                                                                                                                                                                                                                            |


# June 24

## 10PM -> 3:30AM (5.5 hours)

Okay so I dont know what I was thinking! So when I first made my BOM, I relied on a lot of Digikey because they have everything... and then I saw their shipping! So to optimize, I re-did my BOM with primarily adafruit to keep shipping costs down (the parts I buy from microcenter will be in-person so no shipping). I don't know why but getting in the zen of making the schematic, I was able to think more clearly about the parts and how to use the PCB as an effective canvas for connecting. I don't know why but with my past interactions with PCBs I tried to make it as flashy and complicated as possible, but with my goal of minimalism with this project, I think I appreciate it as being an effective way to wire everything togehter. I am looking forward to see how it all turns out. In the meantime, here is a picture of my schematic!
<img width="100" alt="Screenshot 2025-06-24 at 3 07 51 AM" src="https://github.com/user-attachments/assets/4aebd592-64fb-4ca1-aec4-a565e4054d58" />
<img width="500" alt="Screenshot 2025-06-25 at 6 33 33 AM" src="https://github.com/user-attachments/assets/593ba8b3-8116-4231-9fe3-35cd7a39fe0d" />

## 3:30AM -> 4:30AM (1 hour)

Learning experience: plan footprints! So I found out that Kicad does not nativly support my footprints as the symbols are, so I needed to spend a hot minute going through the datasheets for each of my components to select the appropriate footprints. This is what I ended up with: 

<img width="500" alt="Screenshot 2025-06-24 at 4 41 56 AM" src="https://github.com/user-attachments/assets/05f17668-ff6f-443e-86f7-866d9b6e9ede" />


Very excited to start building the PCB now!


## 3PM -> 4PM (1 hour)

Started desinging the PCB!


<img width="500" alt="Screenshot 2025-06-24 at 3 19 32 PM" src="https://github.com/user-attachments/assets/aff2bcb5-9054-4ecf-9fe5-941d2667d66d" />

could not finish this in 1 session; I had work. 

# June 25

## 12AM -> 3AM (3 hours)

Finished with the PCB design! Very excited to see this in person :)

### PCB on Kicad
<img width="100" alt="Screenshot 2025-06-25 at 3 04 05 AM" src="https://github.com/user-attachments/assets/4b7af1d3-0de7-4e19-95a3-312d08e8627d" />
<img width="100" alt="Screenshot 2025-06-25 at 6 34 42 AM" src="https://github.com/user-attachments/assets/00f25166-3e46-4d0e-a5a7-a67c079341f5" />
<img width="500" alt="Screenshot 2025-06-25 at 12 37 25 PM" src="https://github.com/user-attachments/assets/5292b68c-6ea1-4185-b883-7ea34965145c" />


### Front Virtualization
<img width="100" alt="Screenshot 2025-06-25 at 3 04 50 AM" src="https://github.com/user-attachments/assets/0664384a-d36c-4135-a59f-b075da2cdb97" />
<img width="100" alt="Screenshot 2025-06-25 at 6 36 08 AM" src="https://github.com/user-attachments/assets/58d790ab-df49-490f-9635-c0f29274f387" />
<img width="500" alt="Screenshot 2025-06-25 at 12 37 53 PM" src="https://github.com/user-attachments/assets/ddadd9a8-ed75-42f7-a518-3ab2ecc0739a" />



### Back Virtualiation
<img width="100" alt="Screenshot 2025-06-25 at 3 05 29 AM" src="https://github.com/user-attachments/assets/0aacd035-b9d0-45a4-a065-c76e1856e4e7" />
<img width="100" alt="Screenshot 2025-06-25 at 6 37 18 AM" src="https://github.com/user-attachments/assets/863d66a2-5e76-4f48-aa27-7f0693e4a21a" />
<img width="500" alt="Screenshot 2025-06-25 at 12 38 31 PM" src="https://github.com/user-attachments/assets/295289ba-b150-479c-88e3-9459ae74d27c" />


Now onto software!


## 3AM -> 8AM (5 hours)

quick updated: I connected the LBO to pin 37 so I can get a low-battery notification!

okay so I finished the software!!!!!! 

This was significantly more complicated than coding my hackpad.... that took some intense coding.... yikes

I dont know what screenshots to attach here because, well, everything is just text. 

If you want to see a full software reveal, hit the software directory in this repo! There'll be a handy dandy repo there that will explain what each of the 3 files does!

Some things I learned: embeded design is really stupidly hard! If the internet did not exist, I have no clue how I could have found everything I needed. Thankfully, because the goal of my project is minimalism, the code wasn't too too complex but honestly, this was my first time dealing with software with multiple files working together. It was very fun learning how to do this, and I'm glad I gained this skill. 

Final stop: CAD case. 

## 8AM -> 1PM (4 hours)

I'm glad I'm getting better at cad! For this project, I had no inspo (gasp) I did the whole thign by myself, which I am really really proud of. My goal of minimalism probably helped--I want my final product to look like a glorified box which is easier to design haha. Anyways, I ventured with a new CAD software today: shapr3D. I normally use my IPad to sketch, so it was cool to be able to do 3D models on it--it felt a lot more natural than working CAD through fusion. I will post pictures when finished!

OKAY IM FINALLY DONE!!!
![IMG_4890](https://github.com/user-attachments/assets/ac54484e-111d-4471-9d1a-0d8462c254b3)

The design philosophy behind this is simplicity: I wanted the facade to be reminicent of a square instax camera, so I used a similar bulky square mootif as the central design. To add some variety, I included curved floureshes to both add visual contrast and make it easier to hold (no sharp corners!). 

Inside, the design is a tad bit more complicated. With numerous hidden screw holes, everything will be in place without harming the external facade. The "blocky" aesthetic I wanted to achieve is enhanced by the frame's rigidity afforded by the inlaid interlocking square and viewfinder. 

On the sides, there are access points to charge the device and swap out the sd card. 

## 1PM -> 2PM (1 hour)

I spent this time tidying this document up and adding all other documentation onto this repo! I hope you had fun reading this!

# I belive I have everything prepped for this project, including a Custom PCB, Custom Firmware, Custom Case, and associated components. The next step for me is to order my components and build this thing! Very excited

# One quick (and big) thank you to hack club for motivating me to do this project. Its ben an amazing run--thank you!




















