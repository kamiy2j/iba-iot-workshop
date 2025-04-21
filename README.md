# Connected healthcare: IoT, Cloud, and Security in digital age

### 🌟 Overview
This hands-on workshop introduces healthcare professionals to IoT and cloud technologies in modern healthcare through a practical patient monitoring system simulation. Participants will learn how connected medical devices work, explore cloud integration in healthcare, and understand security considerations in medical IoT systems.
<br/><br/>
<img width="700" alt="Screenshot 2025-04-21 at 3 41 20 AM" src="https://github.com/user-attachments/assets/b2615d2c-d955-4522-8044-af4600dbdf6e" />
<br/><br/>

### 🎯 Learning Outcomes & Workshop Outline
<img width="800" alt="Screenshot 2025-04-21 at 3 41 20 AM" src="https://github.com/user-attachments/assets/f841bd70-836b-455b-9fc4-8081aeceb07f" />

### 💻 Prerequisites
- Fundamental knowledge of computer operations and navigation
- Laptop running Windows OS with stable internet connection
- Administrator-level privileges to install and configure required software
------------------


## 🛠️ Workshop Instructions
### Wokwi Account
For our patient monitoring system simulation, we'll leverage Wokwi—a powerful online electronics simulator specifically designed for rapid prototyping and testing of IoT projects.

1. Visit https://wokwi.com/ and create a new account. *(If you don't get email from Wokwi, check in Spam/Junk folder)*
<img width="679" alt="Screenshot 2025-04-21 at 3 41 20 AM" src="https://github.com/user-attachments/assets/3e486e22-fe23-4647-add9-f21aca4ffe46" />
<br/><br/>
2. Join our dedicated classroom using this link: https://wokwi.com/classroom/join?code=yLQ9TsuZn4
<br/><br/>
<img width="629" alt="Screenshot 2025-04-21 at 1 36 34 PM" src="https://github.com/user-attachments/assets/89651f44-05ac-44e0-b807-7e5cef9a5a72" />
<br/><br/>
<img width="626" alt="Screenshot 2025-04-21 at 1 36 42 PM" src="https://github.com/user-attachments/assets/49dffe10-1065-4bae-bab7-9b5e9600f892" />
<br/><br/>

### Install Wokwi Private Gateway
To ensure reliable connectivity during the workshop simulation, we'll use the Wokwi Private Gateway. 

1. Download the gateway application (***wokwigw.exe***) from: https://drive.google.com/file/d/1BgdI2S2ggcG5d6DtUcaOdjBLsbAlhyiJ/view?usp=sharing
2. Run the downloaded file. You should see this confirmation screen indicating successful installation:
<br/><br/>
<img width="589" alt="Wokwi Gateway Running" src="https://github.com/user-attachments/assets/7ce54a2e-fe9f-4c36-94c1-a74e3d316b5c" />
<br/><br/>
*Additional gateway information is available at https://github.com/wokwi/wokwigw (not required for the workshop)*
<br/><br/>

### Simulation Setup
Now let's set up your personal patient monitoring system:

1. Open our Wokwi project template: https://wokwi.com/projects/427997258929717249

2. Create your own copy by clicking the dropdown arrow in the top-left corner, then ***Save a copy*** followed by ***Save copy***. This ensures your changes won't affect other participants.
<img width="723" alt="Screenshot 2025-04-16 at 11 48 15 PM" src="https://github.com/user-attachments/assets/e36c532d-bfb1-4541-a170-925a88f3ee2a" />
<br/><br/>
<img width="442" alt="Screenshot 2025-04-16 at 11 51 21 PM" src="https://github.com/user-attachments/assets/79d7a373-6a10-43bb-9450-a7a2d6fc7d20" /><br/><br/>


3. Enable the private gateway by pressing `F1 (or Function + F1)`, then typing and selecting ***Private Wokwi IoT Gateway***.
<img width="829" alt="Screenshot 2025-04-17 at 12 01 50 AM" src="https://github.com/user-attachments/assets/5a1333d6-a8a2-4a5d-a14b-1ba93838b94b" />

4. Personalize your simulation by finding the patient information section in the code editor:<br/><br/>
<img width="456" alt="Screenshot 2025-04-16 at 11 52 52 PM" src="https://github.com/user-attachments/assets/27be5bfc-3f30-4790-b5f7-1ce20174600d" /><br/><br/>
Replace **John Doe** and **patient001** with your name and ID.<br/><br/>

5. Launch your simulation by clicking the green "Start the simulation" button. Your patient monitoring dashboard will initialize and display vital signs.

<img width="270" alt="Screenshot 2025-04-16 at 11 56 22 PM" src="https://github.com/user-attachments/assets/aa7407df-2b59-4fc7-bc09-7aea4ab68802" />
<br/><br/>
<img width="1051" alt="Screenshot 2025-04-21 at 4 00 18 AM" src="https://github.com/user-attachments/assets/ce9260ef-ddb2-4588-8b1e-9a8e142a8980" />
<br/><br/>
These are the different sensors, where you can increase or decrease the simulated vital signs just by moving these knobs clock or anti-clock wise.
<br/><br/>
<img width="436" alt="Screenshot 2025-04-21 at 4 01 43 AM" src="https://github.com/user-attachments/assets/6f7fad5b-038b-4db1-92e9-acfb108cc5dc" />
<br/><br/>

### Hardware Components:
The simulation includes these components:
- ESP32 microcontroller
- TFT display for ECG and vital signs
- DHT22 temperature sensor
- Various analog inputs simulating:
	- Heart rate sensor
	- Blood pressure sensors
	- Oxygen level sensor
	- Glucose sensor
