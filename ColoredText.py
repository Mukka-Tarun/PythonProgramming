#Python Program to Print Colored Text to the Terminal

#Example 1: Using ANSI escape sequences
print('\x1b[38;2;5;86;243m' + 'Mukka Tarun' + '\x1b[0m')

#Example 2: Using python module termcolor
from termcolor import colored

print(colored('Tarun', 'blue'))