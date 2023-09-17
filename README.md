# GGST Replay Autorecorder

A python script to automatically record and stitch replays from Guilty Gear Strive. Uses OBS hotkeys and **requires setup before running**.

## Setup

Here are the steps to set up this script:
1. Make sure you have OBS [installed](https://obsproject.com/download) and [set up](https://obsproject.com/kb/game-capture-setup-guide).
2. In OBS, go to Settings > Hotkeys, and set the hotkey "Start Recording" to ',' (comma) and "Stop Recording" to '.' (period).
3. Still in OBS, go to Settings > Output, and click on the Recording tab at the top. Under the recording tab, change the file path to be the "temp" folder in this directory.  The individual clipped games will go into this temp folder.
4. Now, when you are ready to begin recording the replays, open Guilty Gear Strive and navigate to the Replays menu. Navigate to either the Saved Replays or Search tab (if you use the search tab, make the search before starting). Put the selection over the replay you want to start with, without selecting it, and open the script. One additional thing you may want to check is the settings inside of the replay playback, for if you want to turn the input viewer or something similar off.
5. When the script opens, it will prompt you for the number of replays you want to record. As soon as you enter the number, you'll have 5 seconds to select Guilty Gear Strive as the main window. Then, the script will run until it has recorded all of the replays, after which it will compile them into one video. Then, it will close.

#### Important Notes
- **The program doesn't clear the temp folder by default**. Make sure to clear out the temp folder after each run of the script. 
- The output video will be saved as "output.mp4" in this folder.  It will override any other output.mp4 that was here before it, so make sure that you move or rename the output before you run the script again.
- Make sure that you leave Guilty Gear Strive as the active window the entire time. The script needs control of the game to properly navigate the menus, and if you use other windows it may mess up the recording process and make the script get stuck. Ideally, after you run the script you can just leave the program running until it finishes.
- Each replay can be quite large in file size, if recorded in 1080p. Please make sure you have enough space for all of the replays to be saved. If you don't have enough space, the script will not function properly.

If you find any bugs in the script, please open an issue on the Github so that I can fix it as soon as possible.