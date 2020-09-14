import os
import time

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()     

while True:
        print("Temperatura Medida="+measure_temp())
        time.sleep(5)
