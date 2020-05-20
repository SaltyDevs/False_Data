import time
class Temperature:
    false_temperature = 15 
    while True:
        if false_temperature==15:
            false_temperature = false_temperature+5
            time.sleep(1)
            print(false_temperature)
        if false_temperature==20:
            false_temperature = false_temperature+3
            time.sleep(1)
            print(false_temperature)
        if false_temperature==23:
            false_temperature = false_temperature-8
            time.sleep(1)
            print(false_temperature)
            