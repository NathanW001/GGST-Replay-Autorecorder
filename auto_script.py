import pyautogui
import keyboard
import pydirectinput
from os import listdir, remove, path
from time import sleep
from moviepy.editor import VideoFileClip, CompositeVideoClip

def begin_record():
	pydirectinput.press(',')

def end_record():
	pydirectinput.press('.')

def close_replay():
	pydirectinput.press('u')

def move_down():
	pydirectinput.press('s')

def open_replay():
	pydirectinput.press('u')
	sleep(0.5)
	pydirectinput.press('u')
	sleep(3)

def render_video():
	clips = []
	for file in listdir("./temp"):
		clips.append(VideoFileClip("./temp/" + file).subclip(0, -2.2))
	clips[0].start = 0
	for i in range(1, len(clips)):
		clips[i] = clips[i].set_start(clips[i-1].duration + clips[i-1].start - 0.3).crossfadein(0.3)
	for clip in clips:
		print(clip.start)
		print(clip.duration)
	final_clip = CompositeVideoClip(clips)
	final_clip.write_videofile("output.mp4")

# 1 = menu, 2 = loading, 3 = in battle
def run(): 
	reps = int(input("how many recordings?"))
	max_reps = reps
	phase = 1
	sleep(5)
	while reps > 0:
		sleep(0.1)
		if keyboard.is_pressed('e'):
			quit()
		if keyboard.is_pressed('s') == False:
			if phase == 1:
				print("> Looking for menu...")	
				menu_loc = pyautogui.locateOnScreen('replay_theatre.png', confidence=0.8)
				if menu_loc is not None and reps == max_reps:
					open_replay()
					phase += 1
				elif menu_loc is not None:
					move_down()
					sleep(0.2)
					open_replay()
					phase += 1
			if phase == 2:
				print("> Game is loading...")
				if pyautogui.pixel(1700, 0) != (0, 0, 0):
					begin_record()
					phase += 1
			if phase == 3:
				print("> Game in progress, OBS is recording")
				menu_loc = pyautogui.locateOnScreen('replay_menu.png', confidence=0.8)
				if menu_loc is not None:
					end_record()
					close_replay()
					phase += 1
			if phase == 4:
				reps -= 1
				phase = 1
				sleep(5)
	
	render_video()

if __name__ == '__main__':
	run()
