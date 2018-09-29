import RPi.GPIO as GPIO
from twilio.rest import Client
import time

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
ldr = 7
led = 11
GPIO.setup(led, GPIO.OUT)
GPIO.setwarnings(False)

def rc_time (ldr):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(ldr) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        z = rc_time(ldr)
        print(z)
        if(z > 350000):
            GPIO.output(led,False)
            account_sid ="ACe25975102f07d5a312c2847d556b8371"
            auth_token = "8bab4e1079d943ab5537d6ee075bf2fe"
            client = Client(account_sid,auth_token)
            message = client.messages.create(body="Light is on",from_="+12523512228" ,to="+918960292897")
            print(message.sid)

        else:
            GPIO.output(led,True)
            
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
