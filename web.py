# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server
import subprocess
# import Raspberry Pi gpio support into python
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

led = 18  # gpio number where the led is connected

# Tell the GPIO module to use gpio numbering used by cpu
GPIO.setmode(GPIO.BCM)
# Set gpio nr 18 to output mode
GPIO.setup(led, GPIO.OUT)
blinker = None
# Function that is ran when a http request comes in
def simple_app(env, start_response):
    global blinker 
    # set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/plain')] 
    start_response(status, headers)

    # What did the user ask for?
    if env["PATH_INFO"] == "/on":
        print("user asked for /on")
        GPIO.output(led, True)
        
        return "got on"
    elif env["PATH_INFO"] == "/off":
        print("user asked for /off")
        blinker.kill()
        GPIO.output(led, False)
        return "got off"
    
    elif env["PATH_INFO"] == "/blink":
        print("user asked for /blink")
        blinker = subprocess.Popen(["python", "blink.py"])
        return "OMG blinking!!"
    
    else:
        print("user asked for something else")
        return "Hello"            

# Create a small python server
httpd = make_server("", 8000, simple_app)
print "Serving on port 8000..."
print "You can open this in the browser http://192.168.1.xxx:8000 where xxx is your rpi ip aadress"
print "Or if you run this server on your own computer then http://localhost:8000" 
httpd.serve_forever()
