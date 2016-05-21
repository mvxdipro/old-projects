#tyutyunnykd_mohamedm2
#Import function to get red, green, blue values
from cImage import * 

import sys 


def grayscale(image): #Function converts to grayscale by averaging the three color values
    grayscaleIM = image.copy()
    numP = image.getNumPixels()

    for i in range (numP):
        apixel = image.getPixel1D(i)
        apixel.red = int((apixel.red + apixel.blue + apixel.green)/3)
        apixel.blue = int((apixel.red + apixel.blue + apixel.green)/3)
        apixel.green = int((apixel.red + apixel.blue + apixel.green)/3)
        grayscaleIM.setPixel1D(i, apixel)
    return grayscaleIM
    
def negate(image): #Function converts to negate by subtracting each color from 255, which turns dark to light and vice versa
    negateIM = image.copy()
    numP = image.getNumPixels()
    
    for i in range (numP):
        apixel = image.getPixel1D(i)
        apixel.red = int(255-apixel.red)
        apixel.blue = int(255-apixel.blue)
        apixel.green = int(255-apixel.green) 
        negateIM.setPixel1D(i, apixel)
    return negateIM
    
def saturatedRGB(r,g,b,k):#Function created by Sherri to adjust color values to saturated
    """ takes the red, green, and blue values for the color of a pixel as well
    as a k value that represents how much to saturate the color, then returns
    a list containing the saturated red, green, and blue values of the color"""
    vals = [.3*(1-k), .6*(1-k), .1+.9*k]
    newr =  scale((.3+.7*k)*r + .6*(1-k)*g + .1*(1-k)*b)
    newg = scale(.3*(1-k)*r + (.6+.4*k)*g + .1*(1-k)*b)
    newb = scale(.3*(1-k)*r + .6*(1-k)*g + (.1+.9*k)*b)
    return [int(newr),int(newg),int(newb)]
    
def scale(val):#Function created by Sherri to return k values 
    """ scales a value to be in the allowable color range for a pixel 0-255 """
    if val < 0:
        val = 0
    elif val > 255:
        val = 255
    return val
    
def saturate(image, k):#Function converts to saturate by using the saturatedRGB function 
    saturateIM = image.copy()
    numP = image.getNumPixels()
    
    for i in range (numP):
        apixel = image.getPixel1D(i)
        satValue = saturatedRGB(apixel.red, apixel.green, apixel.blue, k)
        apixel.red = satValue[0]
        apixel.green = satValue[1]
        apixel.blue =  satValue[2]
        saturateIM.setPixel1D( i, apixel)
    return saturateIM





def main ():
    
    oIm = FileImage(sys.argv[1]) #Assigns a variable to the image inputed from the command line
    win = ImageWin("image", oIm.getWidth()*2, oIm.getHeight()*2)# Creates a window twice the height and width to accommodate  all four images 
    oIm.draw(win)
    
    imGrayscale = grayscale(oIm) #Runs original image through gray scale
    imGrayscale.setPosition(oIm.getWidth()+1,0) #Places image top right 
    imGrayscale.draw(win)
    
    imNegate = negate(oIm) #Runs original image through negate function 
    imNegate.setPosition(0,oIm.getHeight()+1) #Places image bottom left
    imNegate.draw(win)
    
    imSaturate = saturate(oIm, scale(int(sys.argv[2]) )) #Runs original image through saturate function 
    imSaturate.setPosition(oIm.getWidth()+1 , oIm.getHeight()+1) #Places image bottom right
    imSaturate.draw(win)
    

    
    
    
    input("enter to quit")
main()
