# test script light and water
import pifacedigitalio
import time 
pfd = pifacedigitalio.PiFaceDigital() 

print("Testing Mode")

while True:
	print("The relays are now ON")
	pfd.relays[0].value = 1 # lights on
	pfd.relays[1].value = 1 # pump on
	time.sleep(120) # keep this setting for one minute (60 seconds)
	
	print("The pump is now OFF")
	pfd.relays[1].value = 0 # pump off
	time.sleep(120) # keep this setting for one minute (60 seconds)

	print("The pump is now ON")
	pfd.relays[1].value = 1 # pump on
	time.sleep(240) # keep this setting for one minute (60 seconds)

	print("end of test")
	pfd.relays[1].value = 0 # pump off
	pfd.relays[0].value = 0 # lights on
	break









