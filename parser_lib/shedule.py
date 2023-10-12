import requests
from bs4 import BeautifulSoup
from random import choice

link = 'http://www.osu.ru/pages/schedule/'
users = open('Internet+Explorer.txt').read().split("\n")

def is_header(row):
    return row.get('id') == 'tableheader' or row.get('style') == 'page-break-before:always;'

def get_shedule(object_type, faculty, departament, teacher):
    params = {
        'who': str(object_type),
        'facult': str(faculty),
        'kafedra': str(departament),
        'prep': str(teacher),
        'what': '1',
        'mode': 'full',
    }

    userAgent = choice(users)
    header = {
        "user-agent": userAgent
    }

    session = requests.Session()
    website = session.get(link, params=params, headers=header)

    html = BeautifulSoup(website.content, 'lxml')

    table = html.find('table')
    rows = table.find_all('tr')

    shedule = {}

    for row in rows:
        if is_header(row):
            continue

        columns = row.find_all('td')

        date = None
        array = []

        for column in columns:
            if date == None:
                date = column.text
                continue
            cell_content = column.find_all('span')
            if cell_content == []:
                array.append(None)
                continue
            content = []
            for item in cell_content:
                content.append(item.text)
            array.append(content)

        tmp_dict = {date: array}
        shedule.update(tmp_dict)

    return shedule
