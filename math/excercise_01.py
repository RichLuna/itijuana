#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
1. Write a function that takes two integers (x and y) and returns
a list of numbers between x and y that are divisible by 5 but not by 7
"""
import argparse


def divisible_by_5_not_7(x_value: int, y_value: int):
	"""
	This function receives to integers and returns a list of numbers
	between x and y that are divisible by 5 but not by 7
	"""

	# First we verify both varuables are integers
	if not isinstance(x_value, int):
		return -1
	if not isinstance(y_value, int):
		return -1

	# Now we determine the lower and higher values
	if x_value <= y_value:
		lower = x_value
		higher = y_value
	else:
		lower = y_value
		higher = x_value

	result = []

	# Now we iterate over the spread
	for num in range(lower, higher):
		if num % 5 == 0 and num % 7 != 0:
			result.append(num)

	return result


def test_happy_path():
	"""
	We test an easy example
	"""
	# We create 2 lists for each tupe of error
	# One for numbers not divisible by 5
	# And one for numbers divisible by 7

	not_divisible_by_5 = []
	divisibly_by_7 = []

	# We call our function
	result = divisible_by_5_not_7(1, 100)

	# We iterate over each element
	for num in result:
		# If it's not divisible by 5 we add to the corresponding list
		if num % 5 != 0:
			not_divisible_by_5.append(num)
		# If it's divisible by 7 we add to the correspinding list
		if num % 7 == 0:
			divisibly_by_7.append(num)

	# We report errors
	assert not not_divisible_by_5 and not divisibly_by_7, \
		"\nThese values are not divisible by 5: " + str(not_divisible_by_5) \
		+ "\n" \
		"These values are divisible by 7: " + str(divisibly_by_7)


def test_same_numbers():
	"""We test if the function works with equal numbers"""

	# We call our function
	results = divisible_by_5_not_7(50, 50)

	assert not results


def test_negative_range():
	"""We test if the function works with a range in the negative side"""

	results = divisible_by_5_not_7(-100, -1)

	not_divisible_by_5 = []
	divisibly_by_7 = []

	# We iterate over each element
	for num in results:
		# If it's not divisible by 5 we add to the corresponding list
		if num % 5 != 0:
			not_divisible_by_5.append(num)
		# If it's divisible by 7 we add to the correspinding list
		if num % 7 == 0:
			divisibly_by_7.append(num)

	# We report errors
	assert not not_divisible_by_5 and not divisibly_by_7, \
		"\nThese values are not divisible by 5: " + str(not_divisible_by_5) \
		+ "\n" \
		"These values are divisible by 7: " + str(divisibly_by_7)


def test_positive_and_negative():
	"""
	We test if this function works in a range with both negative and
	positive numbers
	"""
	#We test if the function works with a range in the negative side

	results = divisible_by_5_not_7(-100, 100)

	not_divisible_by_5 = []
	divisibly_by_7 = []

	# We iterate over each element
	for num in results:
		# If it's not divisible by 5 we add to the corresponding list
		if num % 5 != 0:
			not_divisible_by_5.append(num)
		# If it's divisible by 7 we add to the correspinding list
		if num % 7 == 0:
			divisibly_by_7.append(num)

	# We report errors
	assert not not_divisible_by_5 and not divisibly_by_7, \
		"\nThese values are not divisible by 5: " + str(not_divisible_by_5) \
		+ "\n" \
		"These values are divisible by 7: " + str(divisibly_by_7)


def test_non_integer_values():
	"""
	We test if the function accepts non-int values. It should
	automatically return a -1 value
	"""

	result1 = divisible_by_5_not_7("a", 1)
	result2 = divisible_by_5_not_7(1, "1")

	assert result1 == -1 and result2 == -1


def main():
	"""Our main function"""
	# Using argsparse we parse the arguments provided

	parser = argparse.ArgumentParser(
		description="This program receives 2 integers as parameters and will return a\
	list of all the numbers betweem then that are divisible by 5 but\
	not divisible by 7")

	parser.add_argument("first_integer", type=int,
						help="The first integer in the range")

	parser.add_argument("second_integer", type=int,
						help="The second integer in the range")

	args = parser.parse_args()

	results = divisible_by_5_not_7(args.first_integer,
								   args.second_integer)

	return results


if __name__ == '__main__':
	import sys
	sys.exit(main())
