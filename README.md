# PaperCam: My Thought Process Behind This Project
![IMG_4878](https://github.com/user-attachments/assets/3b7688c1-9b4d-46a6-84b0-40c486144ab1)
![IMG_4885](https://github.com/user-attachments/assets/347e1d17-facd-4b39-9e84-b688bc39aaf7)

## Description and Exigence

This is my third attempt at hardware design, and it's been so much fun!

The concept arose when I came across ads for disposable cameras for summer camps on YouTube. I remembered the nostalgia of taking instant pictures and the intrinsic joy they bring, but within the context of instant cameras being 1) expensive and 2) harmful to the environment. I want to bridge this gap by creating a digital camera that feels like an instant camera. 

The first thing I think of with instant photography is not knowing exactly how the picture is going to turn out; rather, just taking it and hoping for the best. That's why instead of opting for an LCD display, I chose an E-Ink display. Not only does it use significantly less power, but it can also show an instant snapshot *after* taking the picture, mimicking the feeling of instant photography. 

Another goal I had for this project was to intentionally keep things minimalistic. In a world where technology can have so many features, I wanted to create something simple with one purpose: taking a picture. There's this one Japanese brand (Muji!) that I have been enthralled with for the past 7 years, mainly due to their product's simplicity. Keeping this in mind, I was very mindful of which parts I needed to use. The only user inputs, really, are a power switch and a capture button, nothing excessive but enough to take a picture. Moreover, the e-ink display shows a glimpse of the photo after it has been taken, not necessarily the most detailed, but accurate enough to capture the likeness of whatever is being captured. I hope that this camera will encourage me to try to create memories instead of the best "picture" I hope this camera will let me be less preoccupied with how things look but rather will force me to capture things authentically. 


Here is everything I sourced. A identical version can be found in the BOM tab at the bottom of the README. 

NOTE: I know some items can be found cheaper through other retailars: the only problem is that my parents will only let me buy from the retailors below. If the cost goes above the allocated cost for my project, I will hapilly pay out of my own pocket. I am grateful to have the opportunity to build this, and I cannot do so if I don't buy the parts from the retailors below. 




| item                                       | quantity | cost   | source      | link                                                                                                                                                                                                             |
| ------------------------------------------ | -------- | ------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Raspberry Pi Zero 2 W                      | 1        | 14.99  | microcenter | [https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w](https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w)                                                                             |
| Camera                                     | 1        | 29.25  | adafruit    | [https://www.adafruit.com/product/5657](https://www.adafruit.com/product/5657)                                                                                                                                   |
| e-ink display                              | 1        | 34.99  | amazon      | [https://www.amazon.com/dp/B074NR1SW2](https://www.amazon.com/dp/B074NR1SW2)                                                                                                                                     |
| 64gb SD Card                               | 1        | 0      | myself      | n/a                                                                                                                                                                                                              |
| LiPo Batter 2200mAh                        | 1        | 9.95   | adafruit    | [https://www.adafruit.com/product/1781](https://www.adafruit.com/product/1781)                                                                                                                                   |
| powerboost 1000c                           | 1        | 19.95  | adafruit    | [https://www.adafruit.com/product/2465?srsltid=AfmBOop7pYqBCCEfueczVoFC1WawLn-4JDxrWe6MvBLNL__PzA9LbI22](https://www.adafruit.com/product/2465?srsltid=AfmBOop7pYqBCCEfueczVoFC1WawLn-4JDxrWe6MvBLNL__PzA9LbI22) |
| SPDT Switch                                | 1        | 0.95   | adafruit    | [https://www.adafruit.com/product/805](https://www.adafruit.com/product/805)                                                                                                                                     |
| 12mm Button                                | 1        | 5.95   | adafruit    | [https://www.adafruit.com/product/1010](https://www.adafruit.com/product/1010)                                                                                                                                   |
| Header for RPi                             | 1        | 1.75   | adafruit    | [https://www.adafruit.com/product/3907](https://www.adafruit.com/product/3907)                                                                                                                                   |
| 0.1uF Ceramic Capacitor                    | 2        | 1.95   | adafruit    | [https://www.adafruit.com/product/753](https://www.adafruit.com/product/753)                                                                                                                                     |
| 220uF Electrolytic Capacitor               | 1        | 2.95   | adafruit    | [https://www.adafruit.com/product/2192](https://www.adafruit.com/product/2192)                                                                                                                                   |
| Screws M2.5 × 6 mm \* 5, M2.5 x 10 mm \* 4 | 9        | 16.95  | adafruit    | [https://www.adafruit.com/product/3299](https://www.adafruit.com/product/3299)                                                                                                                                   |
| Custom PCB                                 | 1        | 8.6    | JCLPCB      | [https://jlcpcb.com](https://jlcpcb.com/)                                                                                                                                                                        |
| Total Cost                                 |          | ~148 |





## Schematic and PCB Design

I saw that with this project, spending all this time curating the BOM allowed my schematic and PCB design process to be significantly smoother. I was able to organically decide where components go such that the product can fulfill its purpose without having anything excess. I feel this starked my approach in my Hackpad design, where I flooded the PCB with an LED matrix, OLED, and encoder when perhaps the keys would have sufficed. The design of this project has been meditative, and I am grateful for that. One way I referenced this creative meditation in the design itself is through the inclusion of graphic design motifs I designed during the pandemic. The graphic design kept me sane then through its meditative nature, and I wanted to reference that simple creativity in the silkscreen. I will say that the silkscreen aesthetic starks the clean minimalistic nature of the CAD, and that is intentional: my graphic design motifs, in all their chaos, are a part of me and do not necessarily need to be advertised. To the user, I want the product to be simple elegant, and perfect for capturing memories. 

### Schematic
<img width="500" alt="Screenshot 2025-07-02 at 2 20 03 AM" src="https://github.com/user-attachments/assets/fe7cd2d6-a77b-40ad-bfdb-a26076c50a17" />


### PCB on Kicad

<img width="500" alt="Screenshot 2025-07-02 at 2 41 27 AM" src="https://github.com/user-attachments/assets/dc6a78cb-b4b1-40bd-a981-ad8babd808c8" />



## Firmware

After I designed the PCB, I started on the firmware, the design of which garnered me the most personal growth. While I was able to exercise my research and design skills to a significantly larger extent in this project compared to Hackpad or Gamepad, the software designed for this is something I have never done before. I have never had multiple software files interact with each other in a product before. For instance, I started this project initially with just a runtime firmware, but then realized I needed to use shell too to initiate my code and the file structure and use the system to restart my Python code should it crash. I spent quite a bit coding, but I saw myself getting faster at it which amazed me. I started learning how to code maybe 2 years ago, and I am really proud of what I've been able to do here. 


Everything associated with the firmware can be found in the firmware directory. It has its own specialized README that explains what each file does. 

## CAD

After I was done with the code, I saved the hardest for last: CAD. I've never been good at CAD, but this project allowed me to show my style. When I did graphic design, I specialized in minimalistic designs which were meant to be abstract and aesthetically pleasing. I was highly influenced by the Bauhaus movement, and I am so glad I was able to incorporate that part of my personal style into this project. In keeping line with the "minimal" mindset, I wanted the design to be a simplified square Instax. That's why on the exterior form it almost looks like a kid's toy-- that is intentional. I don't want anything to distract from my camera being used to capture memories, even if it looks a tad blocky (I personally think it looks pretty cool). Making it look seamless on the outside was not easy, though. I utilized a top-case, bottom-case design where my PCB will screw into the bottom case before the top case is applied and the whole thing is screwed together. This required me to be able to hide my mounting screws inside the structure--the inside is much more chaotic than the clean exterior. For stability, I chose to indent the inside a tad so that the top case slides on and has a sense of rigidity. This is enhanced by the view-finder which acts as a "pole" holding everything together. I wanted my camera to not feel like something inherently precious, but rather something that can be taken places and used as a camera to capture memories. The only real adoration I have for it is the phrase "PaperCAM v1" on the user side of it. I want to remind myself that when I use this, it is something that I built and not something I simply bought. I want to remind myself that I have the agency to create things. 

Because everything is on a PCB this time, no fun illustrated wiring diagram :(. However, I did annotate the bellow images for y'all! 


![IMG_4890](https://github.com/user-attachments/assets/0de2c53a-df90-465f-b570-c2ee36b6b91e)
![IMG_4891](https://github.com/user-attachments/assets/f9abefa7-d42a-410f-b8df-b35b7bad67cc)
![IMG_4889](https://github.com/user-attachments/assets/d71f95ad-a440-4938-a158-893c6b4a3320)
![IMG_4886](https://github.com/user-attachments/assets/a980a5a1-af7f-42df-b10f-2d5d13d2a7e3)



## BOM

NOTE: I know some items can be found cheaper through other retailars: the only problem is that my parents will only let me buy from the retailors below. If the cost goes above teh allocated cost for my project, I will hapilly pay out of my own pocket. I am grateful to have the opportunity to build this, and I cannot do so if I don't buy the parts from the retailors below. 




| item                                       | quantity | cost   | source      | link                                                                                                                                                                                                             |
| ------------------------------------------ | -------- | ------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Raspberry Pi Zero 2 W                      | 1        | 14.99  | microcenter | [https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w](https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w)                                                                             |
| Camera                                     | 1        | 29.25  | adafruit    | [https://www.adafruit.com/product/5657](https://www.adafruit.com/product/5657)                                                                                                                                   |
| e-ink display                              | 1        | 34.99  | amazon      | [https://www.amazon.com/dp/B074NR1SW2](https://www.amazon.com/dp/B074NR1SW2)                                                                                                                                     |
| 64gb SD Card                               | 1        | 0      | myself      | n/a                                                                                                                                                                                                              |
| LiPo Batter 2200mAh                        | 1        | 9.95   | adafruit    | [https://www.adafruit.com/product/1781](https://www.adafruit.com/product/1781)                                                                                                                                   |
| powerboost 1000c                           | 1        | 19.95  | adafruit    | [https://www.adafruit.com/product/2465?srsltid=AfmBOop7pYqBCCEfueczVoFC1WawLn-4JDxrWe6MvBLNL__PzA9LbI22](https://www.adafruit.com/product/2465?srsltid=AfmBOop7pYqBCCEfueczVoFC1WawLn-4JDxrWe6MvBLNL__PzA9LbI22) |
| SPDT Switch                                | 1        | 0.95   | adafruit    | [https://www.adafruit.com/product/805](https://www.adafruit.com/product/805)                                                                                                                                     |
| 12mm Button                                | 1        | 5.95   | adafruit    | [https://www.adafruit.com/product/1010](https://www.adafruit.com/product/1010)                                                                                                                                   |
| Header for RPi                             | 1        | 1.75   | adafruit    | [https://www.adafruit.com/product/3907](https://www.adafruit.com/product/3907)                                                                                                                                   |
| 0.1uF Ceramic Capacitor                    | 2        | 1.95   | adafruit    | [https://www.adafruit.com/product/753](https://www.adafruit.com/product/753)                                                                                                                                     |
| 220uF Electrolytic Capacitor               | 1        | 2.95   | adafruit    | [https://www.adafruit.com/product/2192](https://www.adafruit.com/product/2192)                                                                                                                                   |
| Screws M2.5 × 6 mm \* 5, M2.5 x 10 mm \* 4 | 9        | 16.95  | adafruit    | [https://www.adafruit.com/product/3299](https://www.adafruit.com/product/3299)                                                                                                                                   |
| Custom PCB                                 | 1        | 8.6    | JCLPCB      | [https://jlcpcb.com](https://jlcpcb.com/)                                                                                                                                                                        |
| Total Cost                                 |          | ~148 |


## Parting Words

If you've made it so far, thank you. This project has been really personal for me, I don't know why. In the process, I've discovered more of what I value in design and feel that I have been able to refine my personal style. Because of this project, I think I finally feel confident with CAD. In the coding portions, I learned that I can be an actual DEV and not someone who just does practice problems for some test.

Hackclub and Highway, thank you so much for the opportunity to design and hopefully implement this project. 

Until next time,
Arya









