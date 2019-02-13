# Irrigation Scheduler
'''
I need two 'timers'  one to switch the lights on from 8:00 to 21:00; 
the other to switch on the pump at 8:30 and 20:30 for about 3 minutes each time and then switch off.

'''

import sched, time
# import pifacedigitalio # the module or 'hat' on the pi.
# pfd = pifacedigitalio.PiFaceDigital() 
s = sched.scheduler(time.time, time.sleep)

def print_time(): print("From print_time", time.time())
def pump_on(): pfd.relays[1].value = 1 # pump on
def pump_off(): pfd.relays[1].value = 0 # pump off

def print_some_times():
     print(time.time())
     s.enter(5, 1, print_time)      #scheduler.enter(delay, priority, action, argument)
     s.enter(10, 1, print_time)
     s.run()
     print(time.time())

print_some_times()



'''
#alternative solution, multi threading

import time
from threading import Timer
def print_time():
	print "From print_time", time.time()

def print_some_times():
    print time.time()
    Timer(5, print_time, ()).start()
    Timer(10, print_time, ()).start()
   	time.sleep(11)  # sleep while time-delay events execute
    print time.time()

'''