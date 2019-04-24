#!/usr/bin/python

# Richard Givens
# alterEXIF.py
# Copies an image, creates new GPS metadata, replaces existing data, and saves
# the image under a new file filename
# No part of this application was copied from other sources

import shutil, os, piexif, random
from PIL import Image

# Function for image input and copy -------------------------------------------
def copyImage():
# Select the source image
    print '''Input the parameters for the source and destination in this format:
user/directory/folder/filename.extension or folder/filename.extension\n'''
    print "Enter the filepath of the original image:"

    mainImagePath = raw_input()
# Input validation-------------------------------------------------------------
    while not os.path.isfile(mainImagePath):
        print "Invalid Input"
        mainImagePath = raw_input('''Enter a valid filepath for the image:
user/directory/folder/filename.extension or folder/filename.extension\n''')
    if os.path.isfile(mainImagePath):
                print "\nYou selected " + mainImagePath +"\n"

# Select the destination-------------------------------------------------------
    print "Enter the save path of the altered image:"

    alteredImagePath = raw_input()
# Input validation-------------------------------------------------------------
    while not os.path.isfile(alteredImagePath):
        print "Destination does not exist."
        alteredImagePath =raw_input('''Enter a valid save destination/filename\n
user/directory/folder/filename.extension or folder/filename.extension\n''')

    if os.path.isfile(mainImagePath):
        print "\nYou selected " + alteredImagePath +"\n Copying file.....\n"

    shutil.copy2(mainImagePath, alteredImagePath)

    if os.path.isfile(alteredImagePath):
        print "Image copied successfuly."
        return alteredImagePath
# -------------------------End of Function-------------------------------------

# Setting Variables for writing random GPS Data--------------------------------
randAlt     = random.randint(0,1000) # Arbitrary number, can be changed
randLong    = random.uniform(0,90)
randLat     = random.uniform(0,180)

degree      = int(randLong)
minute      = (randLong - degree) * 60
second      = (minute - int(minute)) * 60

minutes     = int(minute)
seconds     = int(second)
# Main GPS variables set-------------------------------------------------------
Longitude   = ((degree ,1), (minutes,1),(seconds,1))
# If longitude is set, then the variables are shifted for latitude-------------
if Longitude:
    degree      = int(randLat)
    minute      = (randLat - degree) * 60
    secconds    = (minute - int(minute))* 60

Latitude    = ((degree, 1),(minutes,1), (seconds,1))
Altitude    = (randAlt,1)
# Used for testing
#print Longitude
#print Latitude
#print Altitude

# Function to begin counstructng the EXIF data---------------------------------

#imagePath = 'alteredImages/cat.jpg'  used in testing function seperately
def setEXIF (Longitude,Latitude,randAlt):

    imagePath = copyImage()
    img = Image.open(imagePath)
# Get current exif data
    exif_dict = piexif.load(imagePath)
    exif_bytes = piexif.dump(exif_dict)

# Printing the default GPS data------------------------------------------------
    print "\nDefault GPS Data:\n"
    print exif_dict['GPS']
# Setting additional local variables-------------------------------------------
    EorW        = random.choice('E''W')
    NorS        = random.choice('N''S')
    UporDown    = random.choice(0, 1)

# Richard Givens
# CPSC 62800
# Week 4, Project 3
# alterEXIF.py
# Copies an image, creates new GPS metadata, replaces existing data, and saves
# the image under a new file filename
# No part of this application was copied from other sources

import shutil, os, piexif, random
from PIL import Image

# Function for image input and copy -------------------------------------------
def copyImage():
# Select the source image
    print '''Input the parameters for the source and destination in this format:
user/directory/folder/filename.extension or folder/filename.extension\n'''
    print "Enter the filepath of the original image:"

    mainImagePath = raw_input()
# Input validation-------------------------------------------------------------
    while not os.path.isfile(mainImagePath):
        print "Invalid Input"
        mainImagePath = raw_input('''Enter a valid filepath for the image:
user/directory/folder/filename.extension or folder/filename.extension\n''')
    if os.path.isfile(mainImagePath):
                print "\nYou selected " + mainImagePath +"\n"

# Select the destination-------------------------------------------------------
    print "Enter the save path of the altered image:"

    alteredImagePath = raw_input()
# Input validation-------------------------------------------------------------
    #while not os.path.exists(alteredImagePath):
        #print "Destination does not exist."
        #alteredImagePath =raw_input('''Enter a valid save destination/filename\n
#user/directory/folder/filename.extension or folder/filename.extension\n''')

    if os.path.exists(mainImagePath):
        print "\nYou selected " + alteredImagePath +"\n Copying file.....\n"

    shutil.copy2(mainImagePath, alteredImagePath)

    if os.path.isfile(alteredImagePath):
        print "Image copied successfuly."
        return alteredImagePath
# -------------------------End of Function-------------------------------------

# Setting Variables for writing random GPS Data--------------------------------
randAlt     = random.randint(0,1000) # Arbitrary number, can be changed
randLong    = random.uniform(0,90)
randLat     = random.uniform(0,180)

degree      = int(randLong)
minute      = (randLong - degree) * 60
second      = (minute - int(minute)) * 60

minutes     = int(minute)
seconds     = int(second)
# Main GPS variables set-------------------------------------------------------
Longitude   = ((degree ,1), (minutes,1),(seconds,1))
# If longitude is set, then the variables are shifted for latitude-------------
if Longitude:
    degree      = int(randLat)
    minute      = (randLat - degree) * 60
    secconds    = (minute - int(minute))* 60

Latitude    = ((degree, 1),(minutes,1), (seconds,1))
Altitude    = (randAlt,1)
# Used for testing
#print Longitude
#print Latitude
#print Altitude

# Function to begin counstructng the EXIF data---------------------------------

#imagePath = 'alteredImages/cat.jpg'  used in testing function seperately
def setEXIF (Longitude,Latitude,randAlt):

    imagePath = copyImage()
    img = Image.open(imagePath)
# Get current exif data
    exif_dict = piexif.load(imagePath)
    exif_bytes = piexif.dump(exif_dict)

# Printing the default GPS data------------------------------------------------
    print "\nDefault GPS Data:\n"
    print exif_dict['GPS']
# Setting additional local variables-------------------------------------------
    EorW        = random.choice('E''W')
    NorS        = random.choice('N''S')
    UporDown    = random.randint(0, 1)


    gps_ifd  = {piexif.GPSIFD.GPSVersionID: (2,2,0,0),
                piexif.GPSIFD.GPSLongitudeRef: EorW,
                piexif.GPSIFD.GPSLongitude: Longitude,
                piexif.GPSIFD.GPSLatitudeRef: NorS,
                piexif.GPSIFD.GPSLatitude: Latitude,
                piexif.GPSIFD.GPSAltitudeRef: UporDown,
                piexif.GPSIFD.GPSAltitude: Altitude,
                }
# Constructing new GPS data----------------------------------------------------

# Inserting the new GPS data back into the exif_dict---------------------------
    exif_dict['GPS'] = gps_ifd

# Printing new data so it can be visually compared to default data-------------
    print "\nModified GPS Data:\n"
    print exif_dict['GPS']
# Loading the data, saving and closing the image-------------------------------
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, imagePath)
    img.save(imagePath, "jpeg", exif = exif_bytes)
    print "\nImage modified"
    img.close()
# -------------------------End of Function-------------------------------------

setEXIF (Longitude,Latitude,Altitude)

