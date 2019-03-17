#  NAME:                  INFT-1004 Assignment Two
#  
#  Programmer 1:          Sean Clark
#    Student number:      c3269995
#  Date created:          16.4.2018
#
#  Description:
      # Function watermarkWithPicture: Main function for questions 1-4
        # Calls on:
          # Function: greyScale
          # Function: scaling
          # Function: overlayPic
          # Function: watermakrBasedOnLuminance
      # Function watermarkWithText: Main function for question 5
        # Calls on:
          # Function: watermarkWithTextMain
      # Function watermarkWithScaledPicture: Main function for question 6
        # Calls on:
          # Function: greyScale
          # Function: autoScalePicture
          # Function: overlayPicForAutoScale
#
      # Function greyScale: take in picture, return greyscale version
      # Function scaling: take in greyScale image and scale to user requirements
      # Function overlayPic: takes in scaled image and creates watermark on originalImage
      # Function watermarkBasedOnLuminance: blends images based on lumiance
      # Function: watermarkWithTextMain: creates text watermark 
      # Function autoScalePicture: Auto scales watermark image
#      
#  Issue 1: Question 4.
      # Function watermarkBasedOnLumiance: 
        # Does the opposite to the requirements of the Assignment. 
        # Makes darker pixels more tranparent and lighter ones not.
        # Unsure how to fix. 
#  Issue 2: Question 6. 
      # Function autoScaledPicture:
        # Successfully creates new watermark image to two thirds of the original image.
        # The issues is that it will only scales part of the watermark image before hitting an error.
        # Unsure how to fix.                 

  
def watermarkWithPicture(originalImage, watermarkImage, strength, scaleFactor):
# This function watermarks the original image with the watermark image.
# The strength of the watermark (0-100) is supplied and determines
# how transparent the watermark image will be. The watermark is
# scaled by using the specified scale factor (it could be smaller or larger)
#
# Requires tasks 1-3 to be completed. (Greyscale, Scaling, Simple blending)
# Will be improved by task 4. (Blending based on luminance)
#

  greyScalePicture = greyScale(watermarkImage)
  scaledImage = scaling(greyScalePicture, scaleFactor)
  overlayPic(originalImage, scaledImage, strength)
  watermarkBasedOnLuminance(originalImage, scaledImage, strength) 
  
def watermarkWithText(originalImage, listStrings, strength, fontSize):
# This function watermarks the original image with the text provied
# in a list of strings. To do this a watermark image is first created
# from the strings and then this is text-based image is used as the watermark
# The font size of text to be used can be specified (12-40)
# scaled to be the width of the original image
# Requires task 5 to be completed. (Creating a text image for watermark)
# Reuses the watermarkWithPicture function (tasks 1-4)
  
  watermarkWithTextMain(originalImage, listStrings, strength, fontSize)
  
  
def watermarkWithScaledPicture(originalImage, watermarkImage, strength):
# This function watermakes the original image with the watermark image
# The strength of the watermark (0-100) is supplied and determines
# how transparent the watermake image will be. The watermark it
# automatically scaled based on the side of the tow images.
#
# Reuqires tas 6 to be completed. (Automatic scaling of watermakr(
# Reuses the watermarkWithPicture function

  greyScalePicture = greyScale(watermarkImage)
  scaledImage = autoScalePicture(originalImage, greyScalePicture)
  overlayPicForAutoScale(originalImage, scaledImage, strength)
  
  
# Takes in watermarkImage and duplicates it
# Makes duplicated version grey scale based on luminance requirements of assignment 
# Returns new watermark image so other functions can use it
def greyScale(watermarkImage):

  #duplicate watermarkImage to preserve original
  greyScalePicture = duplicatePicture(watermarkImage)
  
  #Gets pixels
  for pixel in getPixels(greyScalePicture):
    #Gets red and creates new red color to match with assignment luminance numbers
    newRed = getRed(pixel) * 0.2121
    #Gets green and creates new green color to match with assignment luminance numbers
    newGreen = getGreen(pixel) * 0.7152
    #Gets blue and creates new blue color to match with assignment luminance numbers
    newBlue = getBlue(pixel) * 0.0722
    #Merges new colors
    luminance = newRed + newGreen + newBlue
    #Creates new colors
    setColor(pixel,makeColor(luminance,luminance,luminance))
  
  #repaint new picture
  repaint (greyScalePicture)
  #return new picture
  return (greyScalePicture)

 

# Scaling function for watermark image
# Takes in scaleFactor and decides if it should upscale or downscale
# Also if user enters 1 it will simpaly duplicate the image
# Error messages for if user tries to enter the number 0 or below
# Basic error message for if anything else goes wrong. Unlikely to ever be seen
def scaling(greyScalePicture, scaleFactor):

  #If scale argument is below 1
  #Will downscale image
  if (scaleFactor < 1) and (scaleFactor > 0):
    
    #duplicate picture from greyScale Function
    scaleWaterMark = duplicatePicture(greyScalePicture)
    
    #Gets height and width of picture from greyScale function. 
    height = getHeight(greyScalePicture)
    width = getWidth(greyScalePicture)
    
    #creates new image
    newWaterMarkImage = makeEmptyPicture(width/2,height/2)
    
    #gets new start point X,0
    startPointX = 0
    for newStartPointX in range(0,int(width/2)):
      #Gets new start point Y,0
      startPointY = 0
      for newStartPointY in range(0,int(height/2)):
        #Gets colors from picture from greyScaleFunction
        color = getColor(getPixel(greyScalePicture,startPointX,startPointY))
        #Sets new colors on newWaterMarkImage
        setColor(getPixel(newWaterMarkImage,newStartPointX,newStartPointY), color)
        #loops
        startPointY = startPointY + 2
      startPointX = startPointX + 2
      
    #Show newWaterMarkImage
    show(newWaterMarkImage)
    
    #Return newWaterMarkImage
    return(newWaterMarkImage)
    
  
  #If scale argument is above 1
  #Will upscale image
  elif (scaleFactor > 1):
  
    #duplicate image from greyScale function
    scaleWaterMark = duplicatePicture(greyScalePicture)
    
    #getHeight and Width from image in greyScale function
    height = getHeight(greyScalePicture)
    width = getWidth(greyScalePicture)
  
    #Create new image
    newWaterMarkImage = makeEmptyPicture(width*int(scaleFactor),height*int(scaleFactor))
  
    #Make function start at X,0
    for startPointX in range(0, width):
      #Make function start at Y,0
      for startPointY in range(0, height):
        #get pixels from image make in greyScale function
        WMpixels = getPixel(scaleWaterMark,startPointX,startPointY)
      
        #Select start point on new image
        for newStartPointX in range( startPointX * int(scaleFactor), startPointX * int(scaleFactor) + int(scaleFactor)):
          #Select start point on new image
          for newStartPointY in range( startPointY * int(scaleFactor), startPointY * int(scaleFactor) + int(scaleFactor)):
            #Paint upscaled image onto newWaterMarkImage
            WMtarget = getPixel(newWaterMarkImage,newStartPointX,newStartPointY)
            setColor(WMtarget,getColor(WMpixels))
  
    #show newWaterMarkImage
    show(newWaterMarkImage)
    #return newWaterMarkImage
    return newWaterMarkImage
  
  elif (scaleFactor == 1):
  
    #If user enters 1 (same size) just duplicates picture. 
    scaleWaterMark = duplicatePicture(greyScalePicture)
  
    newWaterMarkImage = scaleWaterMark
    
    return(newWaterMarkImage)
  
  elif (scaleFactor <= 0):
    
    #error message if user tries to scale below 0
    showWarning("Can not scale below 0. Please try again")
    
  else:
  
    #error message for if anything goes wrong.
    #Unlikley to be ever seen. 
    showWarning("Something went wrong. Please try again")
    

    
    
def overlayPicForAutoScale(originalImage, scaledImage, strength):
   pic1 = originalImage
   pic2 = scaledImage

#below will send a error message overlayif the scaled image is greater than the originalImage in width and height             
   if getHeight(pic2) > getHeight(pic1):
      heightError = "Try again the ScaledImage is greater than OriginalImage in height"
      print(heightError)  
   elif getWidth(pic2) > getWidth(pic1):
      widthError = "Try again ScaledImage is greater than OriginalImage in width"
      print(widthError)

#below will centre the scaledImage   
   else: 
      xMargin = (getWidth(pic1) - getWidth(pic2)) / 2
      yMargin = (getHeight(pic1) - getHeight(pic2)) / 2
      proportion = strength
#below will allow to create another function allowing for the blend
      pic3 = overlayPic2(pic1, pic2, xMargin, yMargin, proportion)
      show(pic3) 
    
       
             


#this function allows two images to be blended to a desired strength
def overlayPic(originalImage, scaledImage, strength):
   pic1 = originalImage
   pic2 = scaledImage

#below will send a error message overlayif the scaled image is greater than the originalImage in width and height             
   if getHeight(pic2) > getHeight(pic1):
      heightError = "Try again the ScaledImage is greater than OriginalImage in height"
      print(heightError)  
   elif getWidth(pic2) > getWidth(pic1):
      widthError = "Try again ScaledImage is greater than OriginalImage in width"
      print(widthError)

#below will centre the scaledImage   
   else: 
      xMargin = (getWidth(pic1) - getWidth(pic2)) / 2
      yMargin = (getHeight(pic1) - getHeight(pic2)) / 2
      proportion = strength
#below will allow to create another function allowing for the blend
      pic3 = overlayPic2(pic1, pic2, xMargin, yMargin, proportion)
      show(pic3)

#this function in executed in the previous function
#this function incorporates the base and the overlay out of a 100 
def overlayPic2(pic1, pic2, xStart, yStart, proportion):
     pic3 = duplicatePicture(pic1)
     overlay = (proportion) / 100.0                               
     base = (100-proportion) / 100.0   
     
     for x in range(0, getWidth(pic2)):
        for y in range(0, getHeight(pic2)):  
           pixel2 = getPixel(pic2, x, y)               
           pixel2Red   = getRed(pixel2)
           pixel2Green = getGreen(pixel2)
           pixel2Blue  = getBlue(pixel2) 
           
           pixel3 = getPixel(pic3, x+xStart, y+yStart)  
           pixel3Red   = getRed(pixel3)
           pixel3Green = getGreen(pixel3)
           pixel3Blue  = getBlue(pixel3)
                     
           newRed =   int(pixel2Red * overlay)   + int(pixel3Red * base)
           newGreen = int(pixel2Green * overlay) + int(pixel3Green* base)
           newBlue =  int(pixel2Blue * overlay)  + int(pixel3Blue * base)
           
           setRed(pixel3, newRed)
           setGreen(pixel3, newGreen)
           setBlue(pixel3, newBlue)

#below will return the save the image which is used in the previous function     
     return pic3
     

     
     
     
     
     
     
     
#this function creates a text on originalImage creating a new image called markedImage 
#then the markedImage is blended with the original image
#this function allows for a desired fontsize and strength     
def watermarkWithTextMain(originalImage, listStrings, strength, fontSize): 
  markedImage = duplicatePicture(originalImage)
  height = getHeight(originalImage)
  width = getWidth(originalImage)

#below is the text that is printed
  #listStrings = "--copyright 2018--"

#below is the style/font of the text
  newStyle = makeStyle(sansSerif, plain, fontSize)
  addTextWithStyle(markedImage, height/3, width/3, listStrings, newStyle)
  
  pic1 = originalImage
  pic2 = markedImage

#below is the desired position of the text, approx in centre
  xMargin = (getWidth(pic1) - getWidth(pic2)) / 2
  yMargin = (getHeight(pic1) - getHeight(pic2)) / 2
  proportion = strength
  
#below will allow to create another function allowing for the blend
  pic3 = test2(pic1, pic2, xMargin, yMargin, proportion) 
 
  show(pic3)
  

#this function in executed in the previous function
#this function incorporates the base and the overlay out of a 100 
def test2(pic1, pic2, xStart, yStart, proportion):
     pic3 = duplicatePicture(pic1)
     overlay = (proportion) / 100.0                               
     base = (100-proportion) / 100.0   
     
     for x in range(0, getWidth(pic2)):
        for y in range(0, getHeight(pic2)):  
           pixel2 = getPixel(pic2, x, y)               
           pixel2Red   = getRed(pixel2)
           pixel2Green = getGreen(pixel2)
           pixel2Blue  = getBlue(pixel2) 
           
           pixel3 = getPixel(pic3, x+xStart, y+yStart)  
           pixel3Red   = getRed(pixel3)
           pixel3Green = getGreen(pixel3)
           pixel3Blue  = getBlue(pixel3)
                     
           newRed =   int(pixel2Red * overlay)   + int(pixel3Red * base)
           newGreen = int(pixel2Green * overlay) + int(pixel3Green* base)
           newBlue =  int(pixel2Blue * overlay)  + int(pixel3Blue * base)
           
           setRed(pixel3, newRed)
           setGreen(pixel3, newGreen)
           setBlue(pixel3, newBlue)


#below will return the save the image which is used in the previous function        
     return pic3
     
#############################################
# Reference: Lecture Notes
# Purpose: overlay and base proportion pixels
# Date: 1 May 2018
# Source: Python documentation on lecture slides
# Author: Dr Keith Nesbitt
# Adaptation required: changed variable names 
#############################################
#############################################
# Reference: Textbook Introduction to Computing and Programming in Python
# Purpose: overlay and base proportion pixels
# Date: 1 May 2018
# Source: Textbook
# Author: Mark J. Guzdial and Barbara Ericson
# Adaptation required: changed variable names
#############################################

def watermarkBasedOnLuminance(originalImage, scaledImage, strength):
   #file = pickAFile()
   pic1 = originalImage
   #file = pickAFile()
   pic2 = scaledImage
   
   

   if getHeight(pic2) > getHeight(pic1):
      heightError = "ERROR: The Height of picture2 is greater than picture1"
      print(heightError)  
   elif getWidth(pic2) > getWidth(pic1):
      widthError = "ERROR: The width of picture2 is greater than picture1"
      print(widthError)
   
   else: 
      xMargin = (getWidth(pic1) - getWidth(pic2)) / 2
      yMargin = (getHeight(pic1) - getHeight(pic2)) / 2
      proportion = strength
      pic3 = watermarkBasedOnLuminancePartTwo(pic1, pic2, xMargin, yMargin, proportion, strength)
      show(pic3)
      
def watermarkBasedOnLuminancePartTwo(pic1, pic2, xStart, yStart, proportion, strength):
     pic3 = duplicatePicture(pic1)
     overlay = (proportion) / 100.0                               
     base = (100-proportion) / 100.0
     
     newPort = strength
     
     overlay2 = (proportion) / newPort 
     base2 = (100-proportion) / newPort
     
     newColor = makeColor(222,222,222)
     
     
     for x in range(0, getWidth(pic2)):
        for y in range(0, getHeight(pic2)):
             
                       
             pixel2 = getPixel(pic2, x, y)  
             pixel2Red   = getRed(pixel2)
             pixel2Green = getGreen(pixel2)
             pixel2Blue  = getBlue(pixel2) 
           
             pixel3 = getPixel(pic3, x+xStart, y+yStart)  
             pixel3Red   = getRed(pixel3)
             pixel3Green = getGreen(pixel3)
             pixel3Blue  = getBlue(pixel3)
                       
             newRed =   int(pixel2Red * overlay2)   + int(pixel3Red * base2)
             newGreen = int(pixel2Green * overlay2) + int(pixel3Green* base2)
             newBlue =  int(pixel2Blue * overlay2)  + int(pixel3Blue * base2)
           
             setRed(pixel3, newRed)
             setGreen(pixel3, newGreen)
             setBlue(pixel3, newBlue)

        
     return pic3
     show(pic3)
     
def autoScalePicture(originalImage, greyScalePicture):

  #Duplicate greyScalePicture
  autoScaledPicture = duplicatePicture(greyScalePicture)
  
  height1 = getHeight(originalImage)
  width1 = getWidth(originalImage)
  #To compare to check if image should be downscaled or upscaled
  height = getHeight(autoScaledPicture)
  width = getWidth(autoScaledPicture)
  
  
  
  #If height for greyscalePicture is smaller then the height for originalImage.
  if height <= height1:
  
    #Create empty picture that is two thirds the size of the originalImage
    autoWatermark = makeEmptyPicture((width1/3)*2,(height1/3)*2,black)
    #TEST TO COMPARE!
    ###################################Remove later
    show(originalImage)
    show(autoWatermark)
    ###################################Remove later
    
    #Process to move greyscalePicture to autoWaterMark
    #################################################################################
    #Currently only paints part of the new image. Needs more work
    ##################################################################################
    startX = 1
    for newStartX in range(1,getWidth(greyScalePicture)):
      startY = 1
      for newStartY in range(1,getHeight(greyScalePicture)):
        color = getColor(getPixel(greyScalePicture,startX,startY))
        setColor(getPixel(autoWatermark,newStartX,newStartY), color)
      startY = startY + 1
    startX = startX + 1
    
      
    show(autoWatermark)
    return(autoWatermark)
  
  #Error message for if watermarkPicture is to large. 
  #elif height > height1:
  
    #showWarning("The watermark image can not be higher then the original image")
