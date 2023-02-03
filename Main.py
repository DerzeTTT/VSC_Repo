import math;
import time;

import mouse;

for i in range(360):
    
    angle = i/200;
    X,Z = math.sin(angle)*10, math.cos(angle)*10;

    mouse.move(X,Z, absolute=True);

    time.sleep(.05);