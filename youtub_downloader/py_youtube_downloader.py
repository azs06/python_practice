import os
import sys
import pyperclip
import time
import re


def main():
    print("hello world")
    cliboard_url = pyperclip.paste()
    youtubeUrlRegEx = re.compile(r'\d{3}')

if __name__ == '__main__':
    main()