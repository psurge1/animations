from msilib import sequence
from loading_bar import *
from sequence_one_d import *

def main():
    # loading bar
    loader = loading_bar(char="█", size=10, delay=0.1, percentage=True, percentage_sep=" ", percentage_ndigits=1)
    loader.display()

    # one dimensional sequence
    spinner = sequence_one_d(sequence="\\-/|", steps=12, delay=0.1, percentage=True, percentage_sep=" ", percentage_ndigits=1)
    spinner.display()

if __name__ == '__main__':
    main()