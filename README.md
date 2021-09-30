# Excercises for iTijuana

This is the set of excercises requested by iTijuana in it's hiring process

## Description

This set includes the following excercises:
* Math Questions / Excercises 1
* O.O. Questions / Excercises 1
* Games / Excercises 1
* File Questions / Excercises 1

## Getting Started

### Dependencies

* Python3.9
* Pytest (for unit testing)

### Installing

* Just download this repo. No specific installation is required

### Executing

####file/excercise_01.py

```
usage: excercise_01.py [-h] phrase filepath

This program receives two parameters: a phrase and a filepath. If the phrase exists in the file it will return a valid status, otherwise it will fail.

positional arguments:
  phrase      The phrase to be searched in the file
  filepath    The path to the file to be used

optional arguments:
  -h, --help  show this help message and exit

```

Example:

```
python3 file/excercise_01.py "Saludos" file/ejemplo.txt
```

####games/excercise_01.py

```
usage: excercise_01.py [-h] commands [commands ...]

This program recieves a series of commands to move a sole rook living alone in an infinite chessboard. The program will move the rook according to all the commands and at the end will display the distance
traveled by the rook and how far it is from the starting point. Commands should be given in the format : [Direction] [Distance]. For example: "up 10" "down 20" "left 10" "right 15"

positional arguments:
  commands    The list of commands to be executed by the rook

optional arguments:
  -h, --help  show this help message and exit

```

Example:

```
python3 games/excercise_01.py "up 1" "left 3" "down 2"
```

####math/excercise_01.py

```
usage: excercise_01.py [-h] first_integer second_integer

This program receives 2 integers as parameters and will return a list of all the numbers betweem then that are divisible by 5 but not divisible by 7

positional arguments:
  first_integer   The first integer in the range
  second_integer  The second integer in the range

optional arguments:
  -h, --help      show this help message and exit


```

Example:

```
python3 math/excercise_01.py 1 100
```

####oo/excercise_01.py

```
usage: excercise_01.py [-h] value

This program receives an integer n and returns all the perfect squares less than n

positional arguments:
  value       The integer to generate the list

optional arguments:
  -h, --help  show this help message and exit
```

Example:

```
python3 oo/excercise_01.py 30

```

### Testing
Each file contains a set of unit test that can be executed using pytest.

Example:

```

pytest oo/excercise_01.py

```

## Authors
*  Ricardo Luna - [rglruiz@gmail.com](rglruiz@gmail.com)

## Acknowledgments

* README.md template by [@DomPizzie](https://twitter.com/dompizzie)
