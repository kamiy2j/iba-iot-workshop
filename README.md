# Connected healthcare: IoT, Cloud, and Security in digital age
<p>With IoT in healthcare, every heartbeat becomes a data point in a  
<span style="color:red;">revolutionary</span> new way to live, heal, and thrive.</p>

### 🌟 Overview
This hands-on workshop introduces healthcare professionals to IoT and cloud technologies in modern healthcare through a practical patient monitoring system simulation. Participants will learn how connected medical devices work, explore cloud integration in healthcare, and understand security considerations in medical IoT systems.
<br/><br/>
<img width="700" alt="Flow Diagram" src="https://github.com/user-attachments/assets/12f38044-a82e-4fc1-b680-0c1477b0b9eb" />
<br/><br/>

### 🎯 Learning Outcomes & Workshop Outline
<img width="800" alt="Screenshot 2025-04-21 at 3 41 20 AM" src="https://github.com/user-attachments/assets/f841bd70-836b-455b-9fc4-8081aeceb07f" />

### 💻 Prerequisites
- Fundamental knowledge of computer operations and navigation
- Laptop running Windows OS with a stable internet connection
- Administrator-level privileges to install and configure the required software
------------------


## 🛠️ Workshop Instructions
### Wokwi Account
For our patient monitoring system simulation, we will leverage Wokwi—a powerful online electronics simulator specifically designed for the rapid prototyping and testing of IoT projects.

1. Visit https://wokwi.com/ and create a new account. *(If you don't get email from Wokwi, check in Spam/Junk folder)*
<img width="679" alt="Screenshot 2025-04-21 at 3 41 20 AM" src="https://github.com/user-attachments/assets/3e486e22-fe23-4647-add9-f21aca4ffe46" />
<br/><br/>
2. Join our dedicated classroom using this link: [link here]
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

### Complete Wokwi Setup - Video:
https://github.com/user-attachments/assets/09888734-9163-4787-9000-62bf610b04ed

***Watch on Youtube: https://youtu.be/vSUDStJtLzY***
<br/>

### 🖥️ Server Setup
Now that your patient monitoring device is operational, let's set up the server infrastructure to collect, store, and visualize the vital signs data:

1. **Install Docker Desktop**
   - Download Docker Desktop from: https://www.docker.com/products/docker-desktop/
   - Follow the installation instructions for Windows
   - Ensure Docker is running before proceeding to the next step

2. **Download Workshop Files**
   - Download the workshop files from: [link to workshop files]
   - Extract the ZIP file to a convenient location on your computer
   - Open a command prompt in the extracted folder

3. **Start the Server Infrastructure**
   - Run the following command to start all required services:
     ```
     docker-compose up -d
     ```
   - This will initialize:
     - EMQX (MQTT broker) - Receives data from patient monitoring devices
     - InfluxDB - Time-series database for storing medical data
     - Telegraf - Data collection agent
     - Grafana - Visualization platform for medical dashboards

4. **Verify Services**
   - EMQX Dashboard: http://localhost:18083 (Username: admin, Password: public)
   - InfluxDB Interface: http://localhost:8086 (Username: admin, Password: adminpass)
   - Grafana Dashboard: http://localhost:3000 (Username: admin, Password: admin)

5. **Connect Your Patient Monitor**
   - Your simulated patient monitor will automatically connect to the MQTT broker
   - Data flow: Patient Monitor → MQTT → InfluxDB → Grafana
   - The MQTT topic format is: `medical/{patient_id}/vitals`

### 📊 Data Visualization
Access your personalized patient dashboard:

1. Open Grafana at http://localhost:3000
2. Log in with username `admin` and password `admin` (you'll be prompted to change this on first login)
3. Navigate to Dashboards → Patient Monitoring
4. Select your patient ID from the dropdown to view your personalized dashboard



For this workshop, we've simplified some security aspects, but in a production environment, these considerations would be fully implemented.
## 🛡️ Compliance

Ensuring compliance with international and local regulations is a critical component of our healthcare IoT system. This section outlines how our Wokwi simulation and infrastructure align with key standards:

### 📋 Key Regulatory Standards

- **ISO 27001**  
  International standard for information security management. It ensures data confidentiality, integrity, and availability — especially crucial for transmitting patient data over networks.

- **ISO 27799**  
  Tailored for healthcare, this standard extends ISO 27001 by addressing the specific security needs of medical environments like hospitals and clinics.

- **HIPAA (Health Insurance Portability and Accountability Act)**  
  U.S. regulation protecting patient health information (PHI). It emphasizes encryption, audit logging, and strict access controls.

- **GDPR (General Data Protection Regulation)**  
  European regulation that champions user data privacy and consent. Essential if any patient-identifiable information is involved.

- **HL7 & FHIR**  
  Standards for exchanging healthcare information electronically. They facilitate smooth, secure integration with hospital databases.

### 🧩 Compliance in Practice: Our Wokwi IoT Project

- **🔐 Secure Transmission**  
  Patient vitals and other sensor data are transmitted via TLS-encrypted channels, fulfilling ISO 27001 and HIPAA transmission security mandates.

- **📄 Audit Logging & Data Integrity**  
  Every data packet is timestamped and logged in the cloud, enabling traceability in line with HIPAA and GDPR requirements.

- **🔑 Role-Based Access Control (RBAC)**  
  Access to Grafana dashboards is limited based on user roles (e.g., doctors, admins), enforcing ISO 27799 and HIPAA’s least privilege principle.

- **🕵️ Anonymization by Design**  
  Even simulated datasets are anonymized to uphold GDPR’s privacy-by-design philosophy.

- **📊 Real-Time Alerts & Monitoring**  
  Grafana alerts on abnormal vitals are logged, enabling proactive risk management and ongoing compliance auditing.

### 📚 Reference Documentation
For deeper understanding of the technologies used in this workshop, refer to these official resources:

#### MQTT & EMQX
- [MQTT Essentials](https://www.hivemq.com/mqtt-essentials/) - Comprehensive guide to MQTT protocol
- [EMQX Documentation](https://www.emqx.io/docs/en/v5.0/) - Official documentation for the EMQX MQTT broker
- [MQTT in Healthcare](https://www.emqx.com/en/solutions/industries/healthcare-and-life-sciences) - Use cases for MQTT in healthcare applications

#### Time-Series Databases & InfluxDB
- [InfluxDB Documentation](https://docs.influxdata.com/influxdb/v2.7/) - Official InfluxDB documentation
- [InfluxDB University](https://university.influxdata.com/) - Free training courses on time-series data

#### Visualization & Grafana
- [Grafana Fundamentals](https://grafana.com/tutorials/grafana-fundamentals/) - Getting started with Grafana
- [Grafana Dashboard Creation](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/) - Guide to building effective dashboards

#### IoT Security
- [OWASP IoT Security Guide](https://owasp.org/www-project-iot-security-testing-guide/) - Security best practices for IoT
- [NIST Guide to Industrial IoT Security](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) - Comprehensive security framework
- [FDA Guidance on Medical Device Cybersecurity](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity) - Regulatory guidance for medical IoT

#### ESP32 & Embedded Development
- [ESP32 Technical Reference](https://docs.espressif.com/projects/esp-idf/en/latest/) - Official ESP32 documentation
- [Arduino for ESP32](https://docs.arduino.cc/hardware/esp32) - Using Arduino framework with ESP32
- [Wokwi Documentation](https://docs.wokwi.com/) - Guide to using the Wokwi simulator

<hr><hr>

## 📝 Workshop Feedback
We value your thoughts on this Connected Healthcare IoT workshop! Your feedback helps us improve future sessions and develop new content tailored to your needs.
Please complete our short feedback form:

[➡️ Connected Healthcare Workshop Feedback Form](https://forms.gle/NaMjqJR8X3hsSaDb8)

Your responses will help us:

- Assess the effectiveness of the workshop content
- Identify areas for improvement
- Plan future workshop topics

Thank you for participating!
<br/>
## 🧑‍💻 Our Workshop Team
**Dr. Faisal Iradat** - ***Stack Overlord***

Guided our student team throughout the workshop development, providing mentorship and technical direction.

**Kamran Shahid** - ***Wokwi Whisperer***

Responsible for designing and implementing the Wokwi-based patient monitoring simulation system.

**Ammar & Ahmer** - ***Cloud Commanders***

Led the development of cloud connectivity solutions and MQTT broker configuration.

**Maaz** - ***Viz Wizard***

Created the Grafana dashboards and visualization components.

**Moeen & Siddique** - ***Compliance Crusader***

[Did some complaince stuff]
