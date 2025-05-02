# 🚗 Smart Parking Status System using ESP8266 + Kivy GUI

A real-time smart parking monitoring system using **ESP8266**, **IR sensors**, and a beautiful **Kivy-based Python GUI**. This project provides a visual interface for tracking the status of parking slots over Wi-Fi.
[
[![Parking System Demo](https://img.youtube.com/vi/96bWFbphz6U/0.jpg)](https://youtu.be/96bWFbphz6U)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Kivy](https://img.shields.io/badge/Kivy-2.2.1-green.svg)](https://kivy.org/)
[![ESP8266](https://img.shields.io/badge/ESP8266-Arduino-orange.svg)](https://arduino-esp8266.readthedocs.io/)

---

## 📦 Features

- 🚦 **IR sensor**-based parking slot monitoring.
- 🌐 **ESP8266** sends real-time data via Wi-Fi.
- 📱 **Kivy GUI app** displays live parking slot status.
- 🔴 Red = Occupied | 🟢 Green = Free | ⚪ Gray = Not Connected.

---

## 🧰 Tech Stack

| Component   | Technology               |
|------------|--------------------------|
| Microcontroller | ESP8266 (NodeMCU)       |
| Sensors     | Infrared (IR) Sensors     |
| Communication | HTTP over Wi-Fi (GET)     |
| Frontend GUI | Python + Kivy             |
| Backend Logic | Arduino C++ (ESP8266 code) |

---

## 🚀 Getting Started

### 1. Flash the ESP8266

- Upload `esp8266code.ino` to your ESP8266 board using Arduino IDE.
- Connect IR sensors to GPIOs as defined in your `.ino` file.
- Set your ESP to Access Point (AP) mode or connect it to a local Wi-Fi.

### 2. Run the Python GUI

```bash
pip install kivy requests
python main.py
