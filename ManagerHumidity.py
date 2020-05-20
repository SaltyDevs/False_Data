import time
class Humidity:
    false_humidity = 40
    while True:
        if false_humidity==40:
            false_humidity = false_humidity+10
            time.sleep(1)
            print(false_humidity)
        if false_humidity==50:
            false_humidity = false_humidity+7
            time.sleep(1)
            print(false_humidity)
        if false_humidity==57:
            false_humidity = false_humidity-17
            time.sleep(1)
            print(false_humidity)