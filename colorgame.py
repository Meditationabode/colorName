from PIL import ImageGrab
import ctypes
import time
import sys

x_start = 1071
y_start = 463
x_end = 1568
y_end = 959
level = 2

T = 1
while (T<1200):
    
    if (T>=2):level = 3
    if (T>=3):level = 4
    if (T>=4):level = 5
    if (T>=6):level = 6
    if (T>=8):level = 7
    if (T>=11):level = 8
    if (T>=17):level = 9


    print("T=",T)
    size = (int)((x_end - x_start)/level)
    x_sample =(int) (x_start + size/2)
    y_sample = (int) (y_start + size/2)

    if (T<20): time.sleep(0.3)
    else: time.sleep(0.02)
    colorChanged = 0
    oldColor = (0,0,0)

    firstColor = oldColor
    secondColor = oldColor
    firstX=0; fisrtY=0; secondX=0; secondY=0


    image = ImageGrab.grab()
    x=0;y=0
    for y in range(y_sample, y_end, size):
        for x in range(x_sample, x_end, size):
            
            #ctypes.windll.user32.SetCursorPos(x,y)
            #time.sleep(1)
            color = image.getpixel((x, y))
            if color == (167,67,67):
                sys.exit(0)
            if color != oldColor:
                colorChanged +=1
                oldColor = color
                if colorChanged == 1:
                    firstColor = color
                    firstX=x
                    firstY=y

                if colorChanged == 2:
                    
                    secondColor = color
                    secondX=x; secondY=y
                
                if colorChanged > 2:
                    if color == firstColor:
                        x=secondX; y=secondY
                    else:
                        x=firstX; y=firstY

                    ctypes.windll.user32.SetCursorPos(x,y), ctypes.windll.user32.mouse_event(2,0,0,0,0), ctypes.windll.user32.mouse_event(4,0,0,0,0)
                    T+=1
                    break
        if colorChanged > 2:
            break
        if (x>x_sample and y>y_sample):
           ctypes.windll.user32.SetCursorPos(x,y), ctypes.windll.user32.mouse_event(2,0,0,0,0), ctypes.windll.user32.mouse_event(4,0,0,0,0)
           ctypes.windll.user32.SetCursorPos(firstX,firstY), ctypes.windll.user32.mouse_event(2,0,0,0,0), ctypes.windll.user32.mouse_event(4,0,0,0,0)

#2:1
#3:1
#4:1
#5:2
#6:2
#7:3
#8:6
