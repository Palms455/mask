import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from ip_read import get_proxy_ip
from write import write_csv
import dateparser
from datetime import datetime
from random import choice
from fake_useragent import UserAgent

ua = UserAgent()

def get_proxy():
	html = requests.get('https://free-proxy-list.net/').text
	proxies = []
	soup = BeautifulSoup(html, 'lxml')
	trs = soup.find('table', id= 'proxylisttable').find('tbody').find_all('tr')[:12]
	for tr in trs:
		tds = tr.find_all('td')
		adress = tds[0].text.strip()
		port = tds[1].text.strip()
		schema = 'https' if 'yes' in tds[6].text.strip() else 'http'
		proxy = {'schema': schema, 'adress': adress + ':' + port}

		proxies.append(proxy)
	return choice(proxies) #функция берет на вход список эелемнтов и возвращает рандомное значение из него


def get_html(url):

	headers = {
	'user-agent': ua.random,
	}
	p = get_proxy() #{'schema': '' , 'adress': ''}
	proxy = {p['schema']: p['adress']}
	print(proxy)
	try:
		r = requests.get(url, proxies=proxy, headers=headers)
		print(r.status_code)
	except:
		print('bad request. retrying')
		return get_html(url)
	if r.status_code == 200:
		print('ok')
		return r.text
	if r.status_code == 404:
		return 
	else: get_html(url)



	
def from_avito(key, page=None):
	if not page:
		page = 1
	url = f'https://avito.ru/{key[0]}?s=104&q={key[1]}&p={page}'
	html = get_html(url)
	if html is None:
		return
	check = None
	file = 'Aвито ' + key[0]
	soup = BeautifulSoup(html, 'lxml')
	items = soup.find_all('div', class_='item__line')
	for i in items:
		item = i.find('h3', class_='snippet-title').find('a', class_='snippet-link')
		url = 'https://www.avito.ru' + item.get("href")
		title = item.text

		date = i.find('div', class_='snippet-date-info').get('data-tooltip')
		if (datetime.now() - dateparser.parse(date)).days <= 3:
			data = {'url': url,'date': date, 'title': title}
			check = 1
			write_csv(data, file)
	try:
		page_count = soup.find('span', {"data-marker" : "pagination-button/next"}).find_previous_sibling('span').text
	except:
		return
	if page_count and (page < int(page_count)) and check:
		page += 1
		return from_avito(key, page)

from_avito(['ufa', 'маска'])