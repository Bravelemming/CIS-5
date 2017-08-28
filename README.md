# CIS-5
python and GPIO functions!

Jack Daniel Kinne
CIS 5

------------------- Download an OS -------------------

Download a Raspberry pi "raspbian Wheezy" operating system.

Link here: 
<a href="https://www.raspberrypi.org/downloads/">Wheezy</a>


Once downloaded, you'll need to unzip it.  

------------------- Unzip the OS -------------------

If you use windows, you can find an unzipper 
here:
http://www.7-zip.org/

If you use linux (ubuntu), you already have an unzipper, which is called "unzip."  Other unzippers can be found at the software center.
A totally not necessary manual and documentation can be found 
at: 
http://zlib.net/manual.html

------------------- Image the OS -------------------

When you are ready to mount your operating system on the SD card, congratulations!

You can run Win32 Disk Imager from windows.
Link here:
http://sourceforge.net/projects/win32diskimager/

You can run Disk Image Mounter from Linux, searchable through ubuntu software center.

Guide if you need more help, 
here:
https://www.raspberrypi.org/documentation/installation/installing-images/



------------------- Overclock the Pi -------------------

Follow this guide, 
here:
https://www.raspberrypi.org/documentation/configuration/config-txt.md

The down and dirty version:
1. pop open the file folder location for the SD card (should be named "boot").
**important note: when you access this file on windows two things will happen.  you need to open it with a normal text file.  if you open it with a microsoft document, don't.  you'll get messed up code.
**Second thing: you won't see the line breaks when you modify the code.  Not that important, but NOT EASY.  You only need to delete the FIRST hash ("#") to enable features.  
***strongly recommend you just modify with linux, less problems.
2. open the file marked "config.txt"
3. Find the line "#arm_freq=700"
4.  Change the line to: "arm_freq=900"
5.  Make sure to mark your change by adding a comment with #, recommend something like: "#Jack was here."

congratulations!  you've just overclocked your Pi.



------------------- Configure the Audio -------------------

follow this guide
Here:
https://www.raspberrypi.org/documentation/configuration/audio-config.md

Short version:
set your audio output to 1, which will switch to analogue (headphone jack.)
1.  go to the command line
2.  type this: "amixer cset numid=3 1"
*.  worth noting; HDMI output is 2.


------------------- Play Mp3 Files -------------------

follow this guide
Here:
https://www.raspberrypi.org/documentation/usage/audio/

short version:

1.  navigate to the file location
2.  try this first: "omxplayer example.mp3"
3.  input over headphone jack : "omxplayer -o local example.mp3"
4.  input over HDMI : "omxplayer -o hdmi example.mp3"


------------------- Play video files -------------------


Guide
Here:
https://www.raspberrypi.org/documentation/usage/video/

short version:

1. omxplayer example.mp4


---------------             end       -------------------

