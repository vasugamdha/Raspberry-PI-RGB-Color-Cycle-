import RPi.GPIO as GPIO         # Import Raspberry Pi GPIO library
import time                     # Import the sleep function from the time module

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# make pins into an output
ledR = GPIO.setup(17, GPIO.OUT) #Set pin for RED color
ledG = GPIO.setup(27, GPIO.OUT) #Set pin for GREEN color
ledB = GPIO.setup(22, GPIO.OUT) #Set pin for BLUE color

#Set up outputs as PWM @ 144Hz
freq = 144

ledR = GPIO.PWM(17, freq)
ledG = GPIO.PWM(27, freq)
ledB = GPIO.PWM(22, freq)

ledR.start(100)
ledG.start(0)
ledB.start(0)

#function to change the color

def setColorRGB(stepR, stepG, stepB):
    ledR.ChangeDutyCycle(stepR)
    ledG.ChangeDutyCycle(stepG)
    ledB.ChangeDutyCycle(stepB)
    #print("setColorRGB() called")


try:
    while True:                 # Run forever / infinity loop
        #initialize the pin color status [RED,GREEN,BLUE]
        RGBcolor = [100, 0, 0]

        for decColor in range(3):

            #incColour = decColour == 2 ? 0 : decColour + 1;

            # condition for changing pins
            if (decColor == 2):
                incColor = 0
            else:
                incColor = decColor + 1

            #Loop for changing intensity
            for i in range(0,100):
                RGBcolor[decColor] -= 1;
                RGBcolor[incColor] += 1;
                #print("RGBcolor for loop called")

                #calling setColorRGB function 
                setColorRGB(RGBcolor[0], RGBcolor[1], RGBcolor[2])
                time.sleep(0.01)

except KeyboardInterrupt:
    pass
    #stop the PWM
    ledR.stop(0) 
    ledG.stop(0)
    ledB.stop(0)
    #print("Code Stopped")
    
    #Restore default GPIO state
    GPIO.cleanup() 





