import requests
from lxml import etree
import datetime
import time

username = '' #Ваш юзернейм лолз без @, например мой ctohkc
times = 60 #Промежуток между обновлениями в секундах, ставим не ниже 5-10. Так как лолз подумает что ты дудосер)))

cookies = {
    'xf_is_not_mobile': '',
    '_ga': '',
    'G_ENABLED_IDPS': '',
    'xf_tfa_trust': '',
    'xf_user': '',
    'xf_logged_in': '',
    'xf_market_search_bar': '',
    'xf_viewedContestsHidden': '',
    'xf_feed_custom_order': '',
    'sfwefwe': '',
    'xf_session': '',
    '_ga_J7RS527GFK': '',
}

headers = {
    'authority': 'zelenka.guru',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://zelenka.guru',
    'referer': 'https://zelenka.guru',
    'sec-ch-ua': '"Chromium";v="108", "Opera";v="94", "Not)A;Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
    'x-ajax-referer': f'https://zelenka.guru/{username}/',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get(f'https://zelenka.guru/{username}/', cookies=cookies, headers=headers)
html = response.text
htmlparser = etree.HTMLParser()
tree = etree.XML(html,htmlparser)
check = tree.xpath(f'//html/body/script[1]/text()')[0]
token_pars = check.split('_csrfToken: "')[1]
token_pars_step_two = token_pars.split('",')[0] #Мне похуй на 14 февраля, я люблю тебя каждый день! (Посвящается Анечке)
print(token_pars_step_two)

while True:
    try:
        now = datetime.datetime.today()
        NY = datetime.datetime(2024, 1, 1)
        d = NY-now  
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        data = {
        'custom_title': f'До 2024: {d.days} дней, {hh} часов, {mm} минут',
        '_xfRequestUri': f'/{username}/',
        '_xfNoRedirect': '1',
        '_xfToken': f'{token_pars_step_two}',
        '_xfResponseType': 'json',
        }
        status_update = requests.post(f'https://zelenka.guru/account/status-update', cookies=cookies, headers=headers, data=data) 
        time.sleep(times)
    except:
        continue