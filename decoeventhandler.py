# handles events such as key presses and mouse clicks through easy decorator layer
import keyboard
import pyautogui as pag

class Exceptions:
	class DecoratedFunctionCallException(Exception):
		pass

class handler:
	events = None
	def __init__(self):
		events = {}

	def on_event(self, event):
		def decorator(function):
			self.events[event] = {"callback": function, "active": False}
			def raise_err(*args, **kwargs):
				raise DecoratedFunctionCallException
			return raise_err
		return decorator

	def one_time_loop(self):
		pass
