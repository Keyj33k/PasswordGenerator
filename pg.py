#!/usr/bin/env python3
import random, string

class GenerateKey:

    def __init__(self, string_size: int, string_upper: str, string_lower: str, string_digits: str):
        self.string_digits = string_digits
        self.string_lower = string_lower
        self.string_upper = string_upper
        self.string_size = string_size

    def gen_rand_str(self):
        upper   = self.string_upper
        lower   = self.string_lower
        digit   = self.string_digits
        rands   = "!§$%&/()=?{}][-_,;.:"
        mixgs   = upper + lower + digit + rands
        ssize   = self.string_size
        shuffle = random.sample(mixgs, ssize)
        print("".join(shuffle))

if __name__ == "__main__":
    genKey = GenerateKey(
        24,
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits
    )
    genKey.gen_rand_str()

