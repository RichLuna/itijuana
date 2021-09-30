#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Write a function that takes a phrase and a text file as inputs.
The function returns True if the phrase is found in the document and
returns False otherwise. Note: Newline characters will not
be included in the phrase.
"""


import argparse
from os.path import exists

def verify_phrase(phrase:str, file_path:str):
	"""
	This function will open the file "file_path" and will verify
	if the phrase appears there. If it does it will return True,
	otherwise it will return False
	"""

	#We verify bnoth parameters are strings
	if not isinstance(phrase, str):
		print ("Phrase must be a string")
		return -1
	if not isinstance(file_path, str):
		print ("Filepath must be a string")
		return -1

	#We verify the path exists
	if not exists(file_path):
		print("Filepath must exist")
		return -1

	#We open and read the file
	with open(file_path, encoding="utf-8") as f_doc:
		file_text = f_doc.read()

	return phrase in file_text

def test_happy_path():
	"""
	A happy path for the function
	"""

	result = verify_phrase("Hola", "ejemplo.txt")

	assert result

def test_negative_scenario():
	"""
	Test what happens if the phrase is not in the file
	"""

	result = verify_phrase("Saludos", "ejemplo.txt")
	assert not result

def test_bad_filepath():
	"""
	Test what happes if the filepath is bad
	"""

	result = verify_phrase("Hola", "archivo.txt")
	assert result == -1

def test_bad_phrase():
	"""
	We check what happens if we sent a phrase that is not a string
	"""

	result = verify_phrase(1, "ejemplo.txt")
	assert result == -1

def test_bad_path():
	"""
	Verify what happens if we sent a filepath that is not a string
	"""

	result = verify_phrase("Hola", 1)
	assert result == -1

def main():
	"""
	This is our main function.
	"""

	#Let's work with our arguments
	parser = argparse.ArgumentParser(description = \
	"This program receives two parameters: a phrase and a filepath. \
	If the phrase exists in the file it will return a valid status,\
	otherwise it will fail.")

	parser.add_argument("phrase", type=str, \
	help="The phrase to be searched in the file")

	parser.add_argument("filepath", type=str, \
	help="The path to the file to be used")

	args = parser.parse_args()

	result = verify_phrase(args.phrase, args.filepath)

	return result

if __name__ == '__main__':
	import sys
	sys.exit(main())
