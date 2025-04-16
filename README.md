# IBA - IOT Workshop

### 🌟 Overview
This hands-on workshop introduces healthcare professionals to IoT and cloud technologies in modern healthcare through a practical patient monitoring system simulation. Participants will learn how connected medical devices work, explore cloud integration in healthcare, and understand security considerations in medical IoT systems.

![WhatsApp Image 2025-04-16 at 23 09 13](https://github.com/user-attachments/assets/b2615d2c-d955-4522-8044-af4600dbdf6e)

### 🎯 Learning Outcomes
- ✅ Understand the role of IoT and cloud technologies in modern healthcare
- ✅ Recognize key security risks and challenges in connected medical systems
- ✅ Explore real-world healthcare applications through interactive activities
- ✅ Learn best practices for ensuring system reliability and data safety

### 💻 Prerequisites
- Basic understanding of computer operations
- Laptop with internet access
- Administrator privileges to install software
------------------


## 🛠️ Workshop Instructions
### Install Wokwi Private Gateway
To ensure reliable connectivity during the workshop simulation we'll use the Wokwi Private Gateway. To use wokwi private gateway we'll need a paid Wokwi account.
**[NEED TO CHECK IF WE CAN GO WITH CLASSROOM ACCOUNT HERE OR WE GO WITH PUBLC GATEWAY]**

Download and run the appropriate release for your operating system from: https://github.com/wokwi/wokwigw/releases

If you see this the we are good and gateway is running on your system.

<img width="589" alt="Screenshot 2025-04-17 at 12 14 30 AM" src="https://github.com/user-attachments/assets/7ce54a2e-fe9f-4c36-94c1-a74e3d316b5c" />


### Simulation Setup
1. Open the Wokwi project: Patient Monitor Simulation: https://wokwi.com/projects/427997258929717249

2. On the top-left side, click on the drop-down arrow and the "**Save a copy**" then "**Save copy**" button to create a new copy for you. We are doing this so that our changes don't effect other participants.
<img width="723" alt="Screenshot 2025-04-16 at 11 48 15 PM" src="https://github.com/user-attachments/assets/e36c532d-bfb1-4541-a170-925a88f3ee2a" />
<br/><br/>
<img width="442" alt="Screenshot 2025-04-16 at 11 51 21 PM" src="https://github.com/user-attachments/assets/79d7a373-6a10-43bb-9450-a7a2d6fc7d20" />


3. Press `F1` or `Function + F1` and then type and select "Private Wokwi IoT Gateway" to enable the private IOT gateway that we setup before on our system.
<img width="829" alt="Screenshot 2025-04-17 at 12 01 50 AM" src="https://github.com/user-attachments/assets/5a1333d6-a8a2-4a5d-a14b-1ba93838b94b" />

5. Locate the patient information section in the code on the left-panel:
<img width="456" alt="Screenshot 2025-04-16 at 11 52 52 PM" src="https://github.com/user-attachments/assets/27be5bfc-3f30-4790-b5f7-1ce20174600d" />

Replace **John Doe** and **patient001** with your name and ID.

5. Click on the green "**Start the simulation**" button and the patient monitor system should start and you should be able to see simulated patient's vital data.

<img width="270" alt="Screenshot 2025-04-16 at 11 56 22 PM" src="https://github.com/user-attachments/assets/aa7407df-2b59-4fc7-bc09-7aea4ab68802" />
<br/><br/>
<img width="854" alt="Screenshot 2025-04-17 at 12 06 16 AM" src="https://github.com/user-attachments/assets/0a1c1e73-1d80-43df-ab06-ab7013c54c55" />
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
