import serial  # подключаем библиотеку для последовательной связи
import time  # подключаем библиотеку чтобы задействовать функции задержки в программе

ArduinoSerial = serial.Serial('com3', 115200)  # создаем объект для работы с портом последовательной связи
time.sleep(1)


def switch(var):
    print("you entered", var)  # печатаем подтверждение ввода
    time.sleep(1)
    ArduinoSerial.write(var.encode())

