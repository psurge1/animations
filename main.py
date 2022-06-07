from loading_bar import *

def main():
    loader = loading_bar(char="█", size=10, delay=0.1, percentage=True, percentage_sep=" ", percentage_ndigits=1)
    loader.display_loading_bar()

if __name__ == '__main__':
    main()