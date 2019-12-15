import requests
import os
import datetime
import threading
from bs4 import BeautifulSoup

FILENAME = 'nod32keys.html'
URL = 'https://8fornod.net/keys-nod-32-4/'
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
ABOUT_KEYS_MESSAGE = '''
1. *[EAV]* ESET NOD32 Antivirus 9-12: *все ключи.*
2. *[ESS]* ESET Smart Security 9-12: *ESS; EIS; ESSP.*
3. *[EIS]* ESET Internet Security 10-12: *EIS; ESSP.*
4. *[ESSP]* ESET Smart Security Premium 10-12: *только ESSP.*
'''
TIME_NOW = datetime.datetime.today().strftime('[%d.%m.%Y %H:%M:%S] ')


def read_file(filename):
    try:
        with open(filename) as input_file:
            text = input_file.read()
        return text
    except:
        print('Error in read_file()')


def update_keys():
    """Обновление ключей"""
    try:
        # скачивание страницы
        page = requests.get(URL, headers=HEADERS).text
        with open(FILENAME, 'w', encoding='utf-8') as output_file:
            output_file.write(page)
        # Beatiful Soup и запись в файл
        soup = BeautifulSoup(read_file(FILENAME), 'lxml')
        params_search = soup.findAll('td', attrs={'class': 'password'})
        list_keys = [element.text for element in params_search]
        with open('new_keys.txt', 'w') as sort_list:  # запись в файл и разбиение по строкам
            for keys in list_keys[10:]:  # убираем логины из захвата
                sort_list.write("%s\n" % keys)
        # удаляем пустые строки
        with open('new_keys.txt', 'r') as original, open('clean_keys.txt', 'w') as clean:
            for line in original:
                if line.strip():
                    clean.write(line)
        os.rename('clean_keys.txt', 'new_keys.txt')
    except:
        print('Error in update_keys()')


def format_key():
    """Форматирование списка ключей"""
    try:
        file = open('new_keys.txt', 'r')
        descr = file.readlines()
        file.close()

        today = 'Свежие ключи от ' + datetime.datetime.today().strftime('%d.%m.%Y %H:%M') + ':\n\n'
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


def autoupdate_key():
    """Автообновление ключей каждые 8 часов"""
    try:
        update_keys()
        format_key()
        print(TIME_NOW + 'Auto-update key successful')
        threading.Timer(28800, autoupdate_key).start()
    except:
        print('Error in autoupdate_key()')


def send_keys():
    """Отправка ключей"""
    try:
        file = open('new_keys.txt', 'r')  # открыть файл в режиме чтения
        clipboard = file.read()  # скопировать текст в переменную
        file.close()
        print(TIME_NOW + 'Keys sent')
        return clipboard
    except:
        print('Error in send_keys()')
