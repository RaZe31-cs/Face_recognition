import serial  # подключаем библиотеку для последовательной связи
import time  # подключаем библиотеку чтобы задействовать функции задержки в программе

ArduinoSerial = serial.Serial('com3', 9600)  # создаем объект для работы с портом последовательной связи
# print(ArduinoSerial)
# time.sleep(2)  # ждем 2 секунды чтобы установилась последовательная связь
# a = ArduinoSerial.readline()
# ArduinoSerial.write('1')
# print(a)
# print(ArduinoSerial.readline())  # считываем данные из последовательного порта и печатаем их в виде строки
#
# while 1:  # бесконечный цикл
#     var = input()  # считываем данные от пользователя
#     print("you entered", var)  # печатаем подтверждение ввода
#     if var == '1':  # если значение равно 1
#         ArduinoSerial.write(1)  # передаем 1
#         print("LED turned ON")
#         time.sleep(1)
#
#     if (var == '0'):  # если значение равно 0
#         ArduinoSerial.write(0)  # передаем 0
#         print("LED turned OFF")
#         time.sleep(1)
