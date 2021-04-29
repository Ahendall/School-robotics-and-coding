
## This is my summative project for Coding & Robotics 7, Unit 2: Python.
For this project, We made a Digital Adventure Story.
I Chose to make mine an Choose Your Own Adventure (CYOA) Adaptation of ***Star Wars: Episode III - Revenge of the Sith***.
[You can download the .zip file of the project here](https://github.com/Ahendall/School-robotics-and-coding/raw/main/Unit%202%20-%20Python/%5BIMPORTANT%5D%20Summative%20Assignment/%5BIMPORTANT%5D%20Summative%20Assignment.zip).
A few things to note:
- The Audio in this project has not been volume-adjusted. So Some audio
files will be louder than others when you play it back
- When the program plays an audio file, it will take a second to load.
- You must type the option exactly as you see it (excluding letter cases)
- This requires [Python 3.9.4+](https://www.python.org/downloads/) to run properly. Please download it.
- This requires the *simpleaudio API* to run properly. To download it:
	1. Make sure you added Python 3.9.4 to PATH when installing.
	2. Run this command in your Command Prompt (Terminal or Command line if you are on a Unix System)
	![make sure pip command is the correct one for your platform](https://i.imgur.com/Yxpv6W3.png)


### Here are some of the issues I encountered while working on this.
***Audio file not found when Executing through VS Code***\
**Cause of issue:** VS Code's working directory isn't where the .py file is\
**Solution:** I was unable to fix this issue since I didn't know how properly to edit the launcher.json file.
At first, I used VS Code to edit the file, and IDLE to run it. Then, I just switched entirely
to Visual Studio 2019 Community Edition.


***Code only continues after audio finishes***\
**Cause of issue:** The *playsound* function from the *playsound* API makes the program wait
until the Audio finishes to continue it.\
**Solution:** used the *simpleaudio* API so that there were 2 functions. 1 for letting the code
continue while the audio was still playing (  **play()** and **wait_done()** ).


***Any random answer works on lines 301 & 359***\
**Cause of issue:** for *SOME MIRACULOUS REASON*, when I use *or* to handle multiple option choices
(mainly to let the user type the answer without an apostrophe),  the while loop that makes sure
the user types a valid answer, just doesn't function properly.\
**Solution:** Honestly just removed the *or* and the second options without the apostrophe.
