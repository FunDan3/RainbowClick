# handles events such as key presses through easy decorator layer
import keyboard
import time

class Exceptions:
	class DecoratedFunctionCallException(Exception):
		pass

class handler:
	events = None
	def __init__(self):
		self.events = {}

	def on_event(self, *events):
		def decorator(function):
			self.events[events] = {"callback": function, "active": False}
			def raise_err(*args, **kwargs):
				raise DecoratedFunctionCallException
			return raise_err
		return decorator

	def resolve_all_events(self, events):
		for event in events:
			if not keyboard.is_pressed(event):
				return False
		return True

	def one_time_loop(self):
		for event in self.events.keys():
			if self.resolve_all_events(event):
				if not self.events[event]["active"]:
					self.events[event]["callback"]()
				self.events[event]["active"] = True
			else:
				self.events[event]["active"] = False

	def loop(self, delay = 0):
		while True:
			time.sleep(delay)
			self.one_time_loop()
