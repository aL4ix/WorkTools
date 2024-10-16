#!/usr/bin/env python3

import re
import time
import webbrowser

import pyperclip


HOST = ''
LIST_OF_PROJECTS = ['BE', 'FE']


def main():
    if HOST == '':
        print('Please define a HOST')
        return

    print('Watching for jira links')
    projects = '|'.join(LIST_OF_PROJECTS)
    while True:
        clipboard = pyperclip.paste()
        if re.match(r'('+projects+r')-\d+(\r\n)?$', clipboard):
            print(clipboard)
            pyperclip.copy('')
            webbrowser.open(
                f'https://{HOST}.atlassian.net/browse/{clipboard}')
        time.sleep(1)


if __name__ == '__main__':
    main()
