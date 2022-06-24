from loading_bar import *
from sequence_one_d import *
from sequence_two_d import *

def main():
    # loading bar
    loader = loading_bar(char="█", size=10, delay=0.1, percentage=True, percentage_sep=" ", percentage_ndigits=1, complete_bar=True, complete_symbol=".")
    loader.display()

    # one dimensional sequence
    spinner = sequence_one_d(sequence="\\-/|", steps=12, delay=0.1, percentage=True, percentage_sep=" ", percentage_ndigits=1)
    spinner.display()

    # two dimensional sequence
    matrix_sequence = [
        [
        " 0000 ",
        "00  00",
        "00  00",
        "00  00",
        " 0000 "
        ],
        [
        "1111  ",
        "  11  ",
        "  11  ",
        "  11  ",
        "111111"
        ],
        [
        " 2222 ",
        "22  22",
        "   22 ",
        "  22  ",
        "222222"
        ],
        [
        " 3333 ",
        "33  33",
        "   333",
        "33  33",
        " 3333 "
        ],
        [
        "44  44",
        "44  44",
        "444444",
        "    44",
        "    44"
        ],
        [
        "555555",
        "55    ",
        "55555 ",
        "    55",
        "55555 "
        ],
        [
        " 6666 ",
        "66    ",
        "66666 ",
        "66  66",
        " 6666 "
        ],
        [
        "777777",
        "   77 ",
        "  77  ",
        " 77   ",
        "77    "
        ],
        [
        " 8888 ",
        "88  88",
        " 8888 ",
        "88  88",
        " 8888 "
        ],
        [
        " 9999 ",
        "99  99",
        " 99999",
        "    99",
        " 9999 "
        ]
    ]
    counter = sequence_two_d(sequence=matrix_sequence, steps=9, delay=0.1, percentage=True, percentage_sep=" ", percentage_ndigits=1)
    counter.display()

if __name__ == '__main__':
    main()