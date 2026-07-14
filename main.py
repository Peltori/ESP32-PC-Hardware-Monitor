from machine import I2C, Pin
import sh1106
import network
import machine
import requests
import time
import esp32

from config import (
    WIFI_SSID,
    WIFI_PASSWORD,
    UPDATE_INTERVAL,
    API_URL
)


i2c = I2C(
    1,
    sda=Pin(9),
    scl=Pin(10)
)

display = sh1106.SH1106_I2C(128, 64, i2c)


def connect_wifi(ssid, password):
    wlan = network.WLAN()
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting...")
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            machine.idle()

    display_wifi(wlan)

    print(wlan.ipconfig("addr4"))
    print(wlan.ipconfig("gw4"))
    print(wlan.ifconfig())
    return wlan


def display_wifi(wlan):
    ip, mask = wlan.ipconfig("addr4")
    display.fill(0)

    display.text("WIFI CONNECTED", 0, 0)
    display.text(ip, 0, 10)
    display.text(mask, 0, 20)
    display.show()


def display_data(data, network, esp_temp):
    display.fill(0)

    display.text(f"CPU {data['cpu']}%", 0, 0)
    display.text(f"RAM {data['memory']}G", 0, 10)
    display.text(f"GPU {data['gpu_edge']}C", 0, 20)
    display.text(f"GPUJUNC {data['gpu_junction']}C", 0, 30)
    display.text(f"GPUMEM {data['gpu_memory']}C", 0, 40)
    display.text(f"NET {network} {esp_temp}C", 0, 50)

    display.show()


wlan = connect_wifi("WIFI_SSID", "WIFI_PASSWORD")
time.sleep(UPDATE_INTERVAL)



while True:
    try:
        response = requests.get(API_URL)
        data = response.json()
        response.close()
        network = "OK"

    except OSError:
        network = "ERR"
        
        data = {
            "cpu": "--",
            "memory": "--",
            "gpu_edge": "--",
            "gpu_junction": "--",
            "gpu_memory": "--",
        }
        
    esp_temp = round(esp32.mcu_temperature(), 1)
    display_data(data, network, esp_temp)
    time.sleep(UPDATE_INTERVAL)

