# 320_mvp
Music Visualizer for CS 320

MUSIC VISUALIZER GROUP 1
Ben Carroll, Jake Stephens, Hui Nguyen

to install dependencies:

mac:
pip install moviepy
brew install cython
brew install kivy
brew install ffmeg
pip install aubio

linux:
sudo apt-get install python-pip   
sudo pip install --upgrade pip     
sudo apt-get install ffmpeg         
sudo pip install moviepy            
sudo apt-get install python-kivy

clone our repo:
git clone https://github.com/faxmachine/320_mvp.git

If any of the above installation fails then try on this VM:
https://drive.google.com/a/umass.edu/file/d/0B9A5N8h8SE-FQlBsU3ZEZDBiSTA/view?usp=sharing

Once you are in the VM delete home/320_mvp and then clone the repo again in the home dir
git clone https://github.com/faxmachine/320_mvp.git

NOTE: when using virtual box you may have trouble with clicking the mouse and the keyboard.
go to the bottom right and on the mouse icon and turn off "mouse integration"
To access the terminal press CTRL+ALT+T

Running the application (for all systems):
navigate to 320_mvp/src/
python Gui.py
Use the test songs in 320_mvp/test_data/

NOTE: if you are on the VM use 320_mvp/test_data/BlueRondo.wav the vm does not have enough memory
for "mindseye" mp3

On Mac the music visualizer works on .mp3 and .wav
On linux it only works on .wav

RUNNING TESTS:
navigate to 320_mvp/src/ and enter the follwing on the command line
python GenerateFramesTest.py

for GUI tests run the following:
python test_runnable.py
the gui should open for when testing the GUI and will finish the test when the GUI is closed


test data info:
license: https://creativecommons.org/licenses/by-sa/4.0/
song: This or That by MindsEye

