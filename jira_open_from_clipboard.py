import re
import time
import webbrowser

import pyperclip


HOST = 'https://YOUR_SITE_HERE.atlassian.net'
LIST_OF_PROJECTS = ['BE', 'FE']

def main():
    print('Watching for jira links')
    while True:
        clipboard = pyperclip.paste()
        projects = '|'.join(LIST_OF_PROJECTS)
        if re.match(r'('+projects+r')-\d+(\r\n)?$', clipboard):
            pyperclip.copy('')
            webbrowser.open(
                f'{HOST}/browse/{clipboard}')
        time.sleep(1)


if __name__ == '__main__':
    main()
