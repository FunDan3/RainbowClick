# handles events such as key presses and mouse clicks through easy decorator layer
import keyboard
import pyautogui as pag
import time

class Exceptions:
	class DecoratedFunctionCallException(Exception):
		pass

class handler:
	events = None
	def __init__(self):
		self.events = {}

	def on_event(self, event):
		def decorator(function):
			self.events[event] = {"callback": function, "active": False}
			def raise_err(*args, **kwargs):
				raise DecoratedFunctionCallException
			return raise_err
		return decorator

	def resolve_one_event(self, event):
		return keyboard.is_pressed(event)

	def one_time_loop(self):
		for event in self.events.keys():
			if self.resolve_one_event(event):
				if not self.events[event]["active"]:
					self.events[event]["callback"]()
				self.events[event]["active"] = True
			else:
				self.events[event]["active"] = False

	def loop(self, delay = 0):
		while True:
			time.sleep(delay)
			self.one_time_loop()
