#!/usr/bin/env python3

import re
import time
import webbrowser

import pyperclip


HOST = ''
LIST_OF_PROJECTS = ['BE', 'FE']


def main():
    print('Watching for jira links')
    while True:
        clipboard = pyperclip.paste()
        projects = '|'.join(LIST_OF_PROJECTS)
        if re.match(r'('+projects+r')-\d+(\r\n)?$', clipboard):
            pyperclip.copy('')
            webbrowser.open(
                f'https://{HOST}.atlassian.net/browse/{clipboard}')
        time.sleep(1)


if __name__ == '__main__':
    main()
