import time
from tools import *

class loading_bar:
    def __init__(self, char, size, delay=1.0, percentage=False, percentage_sep=" ", percentage_ndigits=1):
        self.char = char
        self.size = size
        self.delay = delay
        self.percentage = percentage
        self.percentage_sep = percentage_sep
        self.percentage_ndigits = percentage_ndigits

    def display_loading_bar(self):
        ending = ""
        self.percentage_ndigits = None if self.percentage_ndigits == 0 else self.percentage_ndigits
        for i in range(self.size+1):
            msg = f"{set_digits(str(round(i/self.size*100, self.percentage_ndigits)), self.percentage_ndigits)}%" if self.percentage else ""
            if i < self.size:
                ending = "\r"
            else:
                ending = "\n"
            print(self.char*i, msg, sep=self.percentage_sep, end=ending)
            time.sleep(self.delay)

if __name__ == '__main__':
    loader = loading_bar(char="█", size=10, delay=0.1, percentage=True, percentage_sep=" ", percentage_ndigits=1)
    loader.display_loading_bar()