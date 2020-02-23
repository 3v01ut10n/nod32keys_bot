import requests
import os
import datetime
from bs4 import BeautifulSoup


FILENAME = 'nod32keys.html'
URL = 'https://8fornod.net/keys-nod-32-4/'
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
ABOUT_KEYS_MESSAGE = '''
1. *[EAV]* ESET NOD32 Antivirus 9-12: *all keys.*
2. *[ESS]* ESET Smart Security 9-12: *ESS; EIS; ESSP.*
3. *[EIS]* ESET Internet Security 10-12: *EIS; ESSP.*
4. *[ESSP]* ESET Smart Security Premium 10-12: *only ESSP.*
'''


def read_file(filename):
    text = ''
    try:
        with open(filename) as f:
            text = f.read()
    except:
        print('Error in read_file()')

    return text


def update_keys():
    try:
        # Download HTML
        page = requests.get(URL, headers=HEADERS).text
        with open(FILENAME, 'w', encoding='utf-8') as output_file:
            output_file.write(page)
        # Beatiful Soup, write to file
        soup = BeautifulSoup(read_file(FILENAME), 'lxml')
        params_search = soup.findAll('td', attrs={'class': 'password'})
        list_keys = [element.text for element in params_search]
        with open('new_keys.txt', 'w') as sort_list:  # Write to file and line break
            for keys in list_keys[10:]:  # Remove logins from capture
                sort_list.write("%s\n" % keys)
        # Delete empty lines
        with open('new_keys.txt', 'r') as original, open('clean_keys.txt', 'w') as clean:
            for line in original:
                if line.strip():
                    clean.write(line)
        os.rename('clean_keys.txt', 'new_keys.txt')
    except:
        print('Error in update_keys()')


def format_key():
    """Key list formatting to prepare for sending"""
    try:
        with open("new_keys.txt") as f:
            descr = f.readlines()

        today = 'New keys for ' + datetime.datetime.today().strftime('%d.%m.%Y %H.%M') + ':\n\n'
        descr.insert(0, today)
        descr.insert(1, '*> [ESS] Smart Security 9-12*\n')
        descr.insert(8, '\n*> [EAV] NOD32 Antivirus 9-12*\n')
        descr.insert(15, '\n*> [EIS] Internet Security 10-12*\n')
        descr.insert(21, '\n*> [ESSP] Smart Security Premium 10-12*\n')

        file = open('new_keys.txt', 'w')
        descr = ''.join(descr)
        file.write(descr)
        file.close()
    except:
        print('Error in format_key()')


def send_keys():
    """Sending keys"""
    clipboard = ''
    try:
        with open("new_keys.txt") as f:
            clipboard = f.read()
    except:
        print('Error in send_keys()')

    return clipboard
