import time
from tools import *

class loading_bar:
    def __init__(self, char, size, delay=1.0, percentage=False, percentage_sep=" ", percentage_ndigits=1, complete_bar=False, complete_symbol="."):
        self.char = char
        self.size = size
        self.delay = delay
        self.percentage = percentage
        self.percentage_sep = percentage_sep
        self.percentage_ndigits = percentage_ndigits
        self.complete_bar = complete_bar
        self.complete_symbol = complete_symbol

    def display(self):
        ending = ""
        self.percentage_ndigits = None if self.percentage_ndigits == 0 else self.percentage_ndigits
        for i in range(self.size+1):
            bar_c = self.complete_symbol*(self.size-i) if self.complete_bar else ""
            msg = f"{set_digits(str(round(i/self.size*100, self.percentage_ndigits)), self.percentage_ndigits)}%" if self.percentage else ""
            if i < self.size:
                ending = "\r"
            else:
                ending = "\n"
            print(self.char*i+bar_c, msg, sep=self.percentage_sep, end=ending)
            time.sleep(self.delay)
