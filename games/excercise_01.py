#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. You have a chessboard with only the Rook on it. The Rook can
move up, down, left or right from your perspective.
Write a function (or a class) that takes a series of movements
and at the end of the sequence of movements prints two numbers:
a. The distance traveled by the Rook
b. How far away the Rook is from its starting point
"""

import argparse


class Rook():
	"""
	This is the rook class that will represent the rook living
	in the infinite chessboard. It will know it's position at everytime
	and can move it according to the commands provided
	"""
	def __init__(self):
		"""
		We define our initial position 0,0
		Also, we define our initial distance traveled as 0
		"""
		self.x_position = 0
		self.y_position = 0
		self.distance = 0

	def movex(self, num: int):
		"""
		We move the rook in the x axis and we add the traveled distance
		"""
		self.x_position = self.x_position + num
		self.distance = self.distance + abs(num)

	def movey(self, num: int):
		"""
		We move the rook in the y axis and we add the traveled distance
		"""
		self.y_position = self.y_position + num
		self.distance = self.distance + abs(num)

	@property
	def distance_from_start(self):
		"""
		We calculate our distance from the starting point by suming the
		absolute values of the current x and y positions
		"""
		return abs(self.x_position) + abs(self.y_position)

	def parse_distance(self, distance):
		"""
		We cast a string into an int. In case it's not a valid int we
		raise an exception
		"""

		try:
			int_distance = int(distance)
			return int_distance
		except ValueError:
			print(str(distance) + " is not a valid integer.")
			return 0

	def execute_command(self, command: str):
		"""
		This method will parse a command from natural human language to
		something usable in code and execute it. It will also record
		the distance traveled by the command
		"""
		# We make the command all lower case and strip any space
		command = command.lower()
		command = command.strip()

		# First we will define the direction of the command: up, down,
		# left or right. Up and down will move in the y axis and
		# left and right move in the x axis. We the parse the rest of
		# the command as an integer representing the distance to be
		# traveled. Down and left are transformed into negative values.

		if command.startswith("up"):
			command = command[len("up"):]
			distance = self.parse_distance(command)
			self.movey(distance)

		elif command.startswith("down"):
			command = command[len("down"):]
			distance = self.parse_distance(command) * -1
			self.movey(distance)

		elif command.startswith("left"):
			command = command[len("left"):]
			distance = self.parse_distance(command) * -1
			self.movex(distance)

		elif command.startswith("right"):
			command = command[len("right"):]
			distance = self.parse_distance(command)
			self.movex(distance)

		else:
			# In case we have an invalid command
			return "I don't know how to " + command

	def execute_commands(self, commands: list):
		"""
		We receive a list of commands to be executed and execute them.
		"""
		for command in commands:
			self.execute_command(command)


def test_happy_path():
	"""
	We have a happy path scenario
	"""
	rook = Rook()
	commands = ["up 1", "left 3", "down 2"]

	rook.execute_commands(commands)
	assert rook.distance == 6 and rook.distance_from_start == 4


def test_invalid_distance():
	"""
	We will pass an invalid distance value and the function should
	rise an exception.
	"""
	# A wrong distance
	rook = Rook()
	command = "down blah"

	rook.execute_command(command)
	# Rook should not move
	assert rook.distance == 0 and rook.distance_from_start == 0


def test_invalid_move():
	"""
	We will try to move in an invalid way
	"""
	rook = Rook()
	command = "diagonal 3"

	result = rook.execute_command(command)

	assert result == "I don't know how to diagonal 3"\
		and rook.distance == 0\
		and rook.distance_from_start == 0


def test_return_to_origin():
	"""
	This test will check that we have a valid traveling distance even
	if we are returning to the origin point
	"""

	rook = Rook()

	commands = ["up 1000", "left 1000", "down 1000", "right 1000"]

	rook.execute_commands(commands)

	assert rook.distance_from_start == 0 and rook.distance == 4000


def main():
	"""
	Our main function
	"""
	parser = argparse.ArgumentParser(
		description="This program recieves a series of commands to move a sole\
	rook living alone in an infinite chessboard. The program will move\
	the rook according to all the commands and at the end will display\
	the distance traveled by the rook and how far it is from the\
	starting point.\n \
	Commands should be given in the format : [Direction] [Distance].\n \
	For example:\n \
	\"up 10\"\n \
	\"down 20\"\n \
	\"left 10\"\n \
	\"right 15\"")

	parser.add_argument("commands", nargs="+",
						help="The list of commands to be executed by the rook")

	args = parser.parse_args()
	# We create our rook
	rook = Rook()
	# and send it our commands
	rook.execute_commands(args.commands)

	# Now we print the distance traveled
	print("Distance traveled: " + str(rook.distance))
	# And we print the distance from the beggining
	print("Distance from the starting point: " +
		  str(rook.distance_from_start))

	return 0


if __name__ == '__main__':
	import sys
	sys.exit(main())
