import RPi.GPIO as GPIO
from time import sleep
from flask import Flask

app = Flask(__name__)


in1 = 24
in2 = 23
en = 25
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1 , GPIO.OUT)
GPIO.setup(in2 , GPIO.OUT)
GPIO.setup(en , GPIO.OUT)

GPIO.output(in1 , GPIO.LOW)
GPIO.output(in2 , GPIO.LOW)
p=GPIO.PWM(en , 1000)


p.start(75)
print("INTRODUEIX UNA TECLA")
print("\n")

'''
while(1):
    x=input()
    
    if x=='r':
        print("run")
        GPIO.output(in1 , GPIO.HIGH)
        GPIO.output(in2 , GPIO.LOW)
        
    elif x=='s':
        print("stop")
        GPIO.output(in1 , GPIO.LOW)
        GPIO.output(in2 , GPIO.LOW)
        
    elif x=='f':
        print("FWD")
        GPIO.output(in1 , GPIO.HIGH)
        GPIO.output(in2 , GPIO.LOW)
        
    elif x=='b':
        print("BWD")
        GPIO.output(in1 , GPIO.LOW)
        GPIO.output(in2 , GPIO.HIGH)
        
    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
    
    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)

'''
@app.route('/backward')
def backward():
        print("backward")
	GPIO.output(in1 , GPIO.LOW)
        GPIO.output(in2 , GPIO.HIGH)
	return "RUNNING BACKWARD"

@app.route('/forward')
def forward():
	print("forward")
	GPIO.output(in1 , GPIO.LOW)
	GPIO.output(in2 , GPIO.LOW)
	return "RUNNING FORWARD"

@app.route('/run')
def run():
	print("run")
	GPIO.output(in1 , GPIO.HIGH)
        GPIO.output(in2 , GPIO.LOW)
	return "ROBOT RUNNING"

@app.route('/stop')
def stop():
        print("stop")
	GPIO.output(in1 , GPIO.LOW)
	GPIO.output(in2 , GPIO.LOW)
	return "STOPPING"

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	print("server started :)")
