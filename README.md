# Well Log Micro:bit Project - K-12  students

This project demonstrates how to simulate and visualize a **well logs (Gamma Ray)** using BBC micro:bit devices, a robotic car, and a Python script.

---
## 👩‍🔬 Authors

This project was developed by:

- Dalma Cerro Arrieta  
- Mariella El Khoury
- Pallavi Sahu  
---

## 🌍 Why This Project Matters

Understanding subsurface rock properties is critical for applications such as:

- Hydrocarbon exploration  
- Groundwater assessment  
- CO₂ storage  

However, we **cannot directly see underground formations**. Instead, engineers rely on **indirect measurements** from well-logging tools and geophysical methods.

This project recreates that concept using a **physical and digital simulation**, helping students understand how subsurface data is acquired and interpreted.

---

## 🎯 Project Concept

This system mimics real subsurface exploration:

- A **robotic car** represents a *downhole logging tool*  
- A **3D model** represents the *subsurface formation*  
- **Radio communication** simulates *data transmission*  
- A **Python script** visualizes the data in real time  

👉 The goal is to transform a complex engineering concept into a **hands-on, intuitive learning experience**.

---

## 🔧 How to Use the Micro:bit Code

You can run the micro:bit programs in **two different ways**:

---

### 1️⃣ Using MakeCode (.hex file)

- Open: https://makecode.microbit.org/  
- Upload the `.hex` file from the **microbit_codes** folder  
- Flash it to your micro:bit  

- Then run the Python script in **visualization_code** to plot data in real time  

✅ Easiest option for beginners

---

### 2️⃣ Using Python (copy & paste)

- Open: https://python.microbit.org/  
- Copy and paste the `.py` code from the **microbit_codes** folder  
- Flash it to your micro:bit  

- Then run the Python script in **visualization_code** to plot data in real time  

✅ Recommended for learning and customization

---

## 📡 System Overview

- One micro:bit acts as a **controller (sender)**  
- One micro:bit acts as a **receiver (car)**  
- Data is transmitted via radio  
- The receiver sends data to the computer via USB  
- The Python script (`microbit_gr_log.py`) plots data in real time  

---

## ⚙️ Hardware Components

- BBC micro:bit (×2)  
- Motorized robotic car platform  
- Battery pack  
- Materials for 3D formation model (cardboard, paper, glue, etc.)

---

## 📶 Communication Framework

- Uses micro:bit radio (2.4 GHz)  
- Devices share the same radio group  
- Data transmitted as encoded values (e.g., position and GR)

---

## 🧪 Method

The system simulates a logging tool moving through a formation:

- The car moves through a constructed 3D “subsurface”  
- Position and measurement values (e.g., GR) are generated  
- Data is transmitted wirelessly  
- Python visualizes the signal as a **well log**

---

## 🧠 Conceptual Mapping

| Project Component        | Real-World Equivalent        |
|------------------------|-----------------------------|
| Robotic car            | Downhole logging tool       |
| 3D formation model     | Geological subsurface       |
| Radio signals          | Data transmission           |
| Python plot            | Surface acquisition system  |
| Paper textures/colors  | Different rock types        |

---

## 🚀 Results

- Real-time tracking of position and GR values  
- Successful wireless communication between devices  
- Live plotting of well-log data  
- Visualization of subsurface variability  

---

## 🔬 Scientific Significance

This project demonstrates a key principle:

> Subsurface rocks are not observed directly —  
> they are **inferred from measurements and data interpretation**.

---

## 🎓 Educational Impact

This project helps students understand:

- Subsurface exploration concepts  
- Data acquisition and transmission  
- Real-time visualization  
- Engineering thinking through physical simulation  

---
