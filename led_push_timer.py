from machine import Timer, Pin
from utime import sleep_ms
pin22_led = Pin(22, Pin.OUT)
pin4_button = Pin(4, Pin.IN, Pin.PULL_UP)
button_pres = False
print(pin4_button.value())
def button(Timer):
    global button_pres
    
    if pin4_button.value() == False:
        button_pres = True
    else:
        button_pres = False


timer = Timer(0)
timer.init(period = 50, mode = Timer.PERIODIC, callback = button)

while True:
    if button_pres == True:
        pin22_led.on()
        button_pres= False
        sleep_ms(100)
    else:
        pin22_led.off()