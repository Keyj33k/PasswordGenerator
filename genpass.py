#!/usr/bin/env python3

import random
import string
import sys

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @keyj33k                  #
#   Version :   1.0.1                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #


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
        rands = "!§$%&/()=?{}][-_,;.:"
        mixgs = upper + lower + digit + rands
        ssize = self.string_size
        shuffle = random.sample(mixgs, ssize)
        
        print(f"Your password: {''.join(shuffle)}")

if __name__ == "__main__":
    string_size = int(input("Enter the length of your password: "))
    
    if string_size <= 7:
        print(f"{string_size} is too short.")
        sys.exit(1)

    genKey = GenerateKey(
        string_size,
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits
    )
    
    genKey.gen_rand_str()
