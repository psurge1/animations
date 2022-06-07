import time
from tools import *


class sequence_one_d:
    def __init__(self, sequence, steps=4, delay=1.0, percentage=False, percentage_sep=" ", percentage_ndigits=1):
        self.sequence = sequence
        self.steps = steps
        self.delay = delay
        self.percentage = percentage
        self.percentage_sep = percentage_sep
        self.percentage_ndigits = percentage_ndigits

    def display(self):
        ending = ""
        self.percentage_ndigits = None if self.percentage_ndigits == 0 else self.percentage_ndigits
        for i in range(self.steps+1):
            msg = f"{set_digits(str(round(i/self.steps*100, self.percentage_ndigits)), self.percentage_ndigits)}%" if self.percentage else ""
            if i < self.steps:
                ending = "\r"
            else:
                ending = "\n"
            print(self.sequence[i%len(self.sequence)], msg, sep=self.percentage_sep, end=ending)
            time.sleep(self.delay)