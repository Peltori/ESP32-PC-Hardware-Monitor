# ESP32 PC Hardware Monitor

A small ESP32-S3 project written in MicroPython that displays live hardware statistics from my desktop PC on a 128x64 SH1106 OLED display.  

The ESP32 periodically requests system information from my own FastAPI backend over Wi-Fi and displays the latest values on the OLED screen.  

## Features

- ESP32-S3 + MicroPython
- SH1106 OLED display
- Wi-Fi connectivity
- Automatic API polling
- CPU usage
- RAM usage
- GPU edge temperature
- GPU junction temperature
- GPU memory temperature
- ESP32 internal temperature
- Network error handling

## Dependencies

- MicroPython
- SH1106 MicroPython driver
- My custom FastAPI backend

The API used by this project is available [here](https://github.com/Peltori/ESP32-Hardware-Monitor-API)  


This project uses the SH1106 MicroPython driver by Radomir Dopieralski, Robert Hammelrath and Tim Weber (MIT License). [Link for the driver](https://github.com/robert-hh/SH1106)  
