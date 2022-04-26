import random
import os

magenta = "\033[0;35m"
yellow  = "\033[0;33m"
green   = "\033[0;32m"
cyan    = "\033[0;36m"
red     = "\033[0;31m"
white   = "\033[0;37m"

global length 
global res

os.system("cls")
try:
    length = int(input(red + "(" + cyan + "Password length" + red + ")" + magenta + "$ "))
except ValueError as ve:
    print(red + f"You need to enter a string!\n{ve}")

numbers = "1234567890"
lowers  = "abcdefghijklmnopqrstuvwxyz"
uppers  = "ABVDEFGHIJKLMNOPQRSTUVWXYZ"
special = "§$%&/()=}[{]?!_.,;:" 
mixer   = numbers + lowers + uppers + special

try:
    res     = random.sample(mixer, length)
except ValueError as ve:
    print(red + f"You need to enter a string!\n{ve}")

finalp  = ''.join(res)
print(green + "\nYour generated password: " + f"{finalp}\n" + white)
input(cyan  + "Press any key to continue" )
