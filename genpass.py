#!/usr/bin/env python3

from pyfiglet import figlet_format
from time import sleep
from sys import exit
import random
import string

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @keyj33k                  #
#   Version :   1.0.2                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

g = "\033[0;32m"
c = "\033[0;36m"
y = "\033[0;93m"
w = "\033[0;37m"


class GenerateKey:

    def __init__(
            self,
            string_size: int,
            string_upper: str,
            string_lower: str,
            string_digits: str
    ):
        self.string_digits = string_digits
        self.string_lower = string_lower
        self.string_upper = string_upper
        self.string_size = string_size

    def gen_rand_str(self):
        upper = self.string_upper
        lower = self.string_lower
        digit = self.string_digits
        rands = "!$%&/()?{}][-_"
        mixgs = upper + lower + digit + rands
        ssize = self.string_size
        shuffle = random.sample(mixgs, ssize)

        sleep(0.75)

        print("=" * 50)
        print(f"{w}[{g}+{w}] Your password: {''.join(shuffle)}")
        print("=" * 50)


if __name__ == "__main__":
    print(figlet_format("Password\nGenerator\n") + "=" * 50)

    try:
        string_size_ = int(input(f"{w}[{c}*{w}] Enter the length of your password: "))
        if string_size_ <= 7:
            print(f"{w}[{y}-{w}] {string_size_} is too short.")
            exit(1)

        genKey = GenerateKey(
            string_size_,
            string.ascii_uppercase,
            string.ascii_lowercase,
            string.digits
        )

        genKey.gen_rand_str()
    except ValueError:
        print(f"{w}[{y}-{w}] You need to enter a integer value!")
        exit(1)
    except KeyboardInterrupt:
        print(f"\n{w}[{r}-{w}] Ctrl+C pressed, Exit Password-Generator.")
        exit(1)

    sleep(0.75)
    print(f"{w}[{c}*{w}] Done.")
    exit(0)
