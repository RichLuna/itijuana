#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Write a generator that takes a number N and returns all perfect squares less than N.
Hint: use yield
Example 1: N=30 then the generator will give 1, 4, 9, 16, 25 sequentially
"""
import argparse

def perfect_squares(n_value: int):
	"""
	This function takes an integer n and returns all the perfect squares
	less than n
	"""
	# First we verify n is an integer
	if not isinstance(n_value, int):
		yield -1
	else:
		# Now we should generate the perfect squares
		for number in range(1, n_value):
			square = number * number
			# If the result is less than n, we return it. Otherwise we end.
			if square < n_value:
				yield square
			else:
				break


def test_happy_path():
	"""
	A happy path for the function
	"""
	results = []

	# We get all the results
	for number in perfect_squares(30):
		results.append(number)

	# Our expected result
	expected = [1, 4, 9, 16, 25]

	test = True

	for index, element in enumerate(results):
		if element != expected[index]:
			test = False

	# Report test
	assert test, "\nExpected results: " + str(expected) + \
		"\nActual results: " + str(results)


def test_negative_value():
	"""
	The function should be able to recive negative values
	but should return an empty iterable since there are no negative
	perfect squares
	"""

	results = []

	# We call our function
	for square in perfect_squares(-100):
		results.append(square)
	assert not results, "The function returned: " + str(results)


def test_strange_types():
	"""
	The function should not accept anything other than integers.
	It should return -1 if something else is passed.
	"""
	results = []

	# We call our function
	for element in perfect_squares("1"):
		results.append(element)

	assert results[0] == -1 and len(results) == 1


def main():
	"""Our main function"""
	# Let's work with our arguments
	parser = argparse.ArgumentParser(
		description="This program receives an integer n and returns all the perfect\
	squares less than n")

	parser.add_argument("value", type=int,
						help="The integer to generate the list")

	args = parser.parse_args()

	# We call our function
	results = []

	for element in perfect_squares(args.value):
		results.append(element)

	return results


if __name__ == '__main__':
	import sys
	sys.exit(main())
