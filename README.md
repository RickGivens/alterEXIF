# alterEXIF
A python application which copies images and loads randomized GPS data
by Richard Givens

ynopsis:
The program alterEXIF.py is an interactive Python script which copies an image
from a source destination, extracts the EXIF GPS dictionary, and inserts
modified values generated randomly.

Running the script:
1. From the Terminal or Command Line, navigate to the directory where alterEXIF
is stored.

2. Enter the command to start script, on Linux this will be ./alterEXIF.py.

3. The script will prompt you to enter the path for the source file, for best
results, enter the full path (/home/user/directory/folder/filename.extension).
If the source file is in the same user directory as alterEXIF, you may shorten
the command to read folder/fiilename.extension.

4. If the source file exists at the destination entered, the script will prompt
you to enter the save path for the file. If the source path does not exist, is
misspelled, or if the file itself does not exist as named, the script will
prompt you to reenter the filename.

5. It is important to create a destination folder in advance of running this
script. If the destination path does not exist, you will be prompted to enter a
valid path.

6. If the path exists, and the file is copied successfully, the script will
provide a confirmation message that the image has been copied.

7. The remainder of the script will fun automatically, reading the file and its
EXIF data, and displaying the encoded GPS data. Then, the script will generate
random values and replace the GPS data in the image, saving it under the same
filename as the copied image, replacing it and its EXIF data.

8. Once the randomized data is loaded into the image, the new EXIF data will
be displayed, confirming the GPS data is different from its original values. At
this point the script will close the image.

9. The new values will consist of a Longitude, Latitude, Altitude, LongitudeRef,
LatitudeRef, and ALtitudeRef.

Known Bugs and Limitations
1. If the user does not input the filename and extension, the program will error
out. This can be fixed in future versions by including exception handling.

2. Altering the EXIF data of any image may create graphical anomalies, distort-
ing the image from its original appearance. This is especially true of images
which contained no GPS data initially, but may occur in any particular image.

3. The denominator used in the randomized GPS data is always "1", a cursory
forensic analysis of the altered image may reveal that it has been altered.

4. There are multiple timestamp values within images, none were observed to be
present in GPS dictionaries, so those values are unaltered.

5. There is no checking of the randomized GPS coordinates, generated coordinates
could be in the middle of the ocean, in the air, below ground, or any other
possible location. The range of numbers is based on real world figures, however.

