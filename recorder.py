#! /usr/bin/python3
import decoeventhandler
import time
import pickle
import pyautogui as pag

last_click_time = None
clicks = []

right_record_key_combination = input("Key combination to record right click: ")
left_record_key_combination = input("Key combination to record left click: ")
quit_key_combination = input("Key combination to quit: ")

def record_click(button):
	global clicks
	global last_click_time
	if not last_click_time:
		last_click_time = time.time()

	dt = time.time() - last_click_time
	last_click_time = time.time()
	x, y = pag.position()
	clicks.append(((x,y), button, dt))


keyboard = decoeventhandler.handler()

@keyboard.on_event(*right_record_key_combination.split("+"))
def record_right_click():
	print("Right click recorded")
	record_click("right")

@keyboard.on_event(*left_record_key_combination.split("+"))
def record_left_click():
	print("Left click recorded")
	record_click("left")


@keyboard.on_event(*quit_key_combination.split("+"))
def quit():
	filename = input("Save as: ")
	with open(filename, "wb") as f:
		f.write(pickle.dumps(clicks))
	exit()

keyboard.loop(0.1)
