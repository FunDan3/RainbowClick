#! /usr/bin/python3
import decoeventhandler
import time
import pickle
import pyautogui

filename = input("open: ")
with open(filename, "rb") as f:
	clicks = pickle.loads(f.read())

start_key_combination = input("Key combination to start clicking: ")
quit_key_combination = input("Key combination to quit: ")
delay = int(input("Delay in seconds: "))

keyboard = decoeventhandler.handler()

def execute_click(click):
	position, button, delay = click
	x, y = position
	print(f"({x}, {y}), {button}, {round(delay, 2)}")
	pyautogui.moveTo(x, y)
	time.sleep(delay)
	pyautogui.click(button = button)

@keyboard.on_event(*start_key_combination.split("+"))
def start():
	while True:
		for click in clicks:
			execute_click(click)
	time.sleep(delay)
@keyboard.on_event(*quit_key_combination.split("+"))
def quit():
	filename = input("Save as: ")
	with open(filename, "wb") as f:
		f.write(pickle.dumps(clicks))
	exit()

keyboard.loop(0.1)
