# This code  scales images up or down, and blurs images.
#mohamedm2_tyutyunnykd
     
     
from cImage import *
import sys

def scale(image, s): #This function scales the image up or down
    
    if s < 1: #if the scale is less than 1, it is scaling down
        ew = int(image.getWidth() )
        el = int(image.getHeight() )
        
        newim = EmptyImage(int(image.getWidth() * s) , int(image.getHeight() *s)) #Coping from big to small image  
        for y in range(0, image.getHeight(), int(1/s)):
            for x in range(0, image.getWidth(), int(1/s)):
                p = image.getPixel(x,y)
                newim.setPixel(int(x*s),int(y*s),p)
                          
    else: #if the scale is greater than 1, it is scaling up
        
        newim = EmptyImage(round(image.getWidth() * s) , round(image.getHeight() *s)) #Copying from small to big image
        for y in range(int(newim.getHeight())):
            counter = 0 #Keeps track of the distance from (0,0)
            for x in range(newim.getWidth()): 
                p = image.getPixel(round(counter), int(y/s)) 
                newim.setPixel(x, y, p)
                counter += (1/s)
                if round(counter) >= image.getWidth(): #If the image goes beyond the width, it stops
                    break             
    return newim
    
def blur(image, radius): # This function blurs the image 
    newim = EmptyImage(int(image.getWidth()), int(image.getHeight()))
    for y in range(int(image.getHeight())):
        for x in range(int(image.getWidth())): #Goes through all pixel positions 
            # Variable hold total color value for each color
            Red = 0 
            Green = 0
            Blue = 0
            counter = 0
            #Goes through the pixels only in the picture 
            for vertical in range(int(y-radius), int(radius+y)):
                for hor in range(int(x-radius), int(radius+x)):
                    if vertical >= 0 and vertical < int(image.getHeight()):
                      if hor >= 0 and hor < image.getWidth():
                        # Adds up the color values of the pixels in the grid  
                        p = image.getPixel(hor,vertical)
                        Red+= p.red
                        Green+= p.green
                        Blue+= p.blue
                        counter+=1
            #Sets the new color value to the average            
            p.red = int(Red/counter)
            p.green = int(Green/counter)
            p.blue = int(Blue/counter)
            newim.setPixel(x,y,p)
    return newim

    



        

def main ():
    #Original image 
    oIm = FileImage(sys.argv[1])
    Nscale = float(sys.argv[2])
    rad = float(sys.argv[3])
    windowW = oIm.getWidth()
    windowL =  oIm.getHeight()
    #Creates a window frame that all the pictures can fit in
    if Nscale > 2:
        windowW = windowW *(1+Nscale)
        windowL = windowL * Nscale
    else:
        windowW = windowW * (1+ Nscale)
        windowL = windowL * 2 
        
    win = ImageWin("image", windowW , windowL)
    
    oIm.draw(win)

    
    scaledimage = scale(oIm, float(sys.argv[2]))
    scaledimage.setPosition(oIm.getWidth()+1, 0)
    scaledimage.draw(win)
    
    bluredimage = blur(oIm, rad)
    bluredimage.setPosition(0, oIm.getHeight()+1)
    bluredimage.draw(win)
    
    
    
    input("enter to quit")
main()
        
        
    
