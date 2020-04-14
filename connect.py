import requests
from bs4 import BeautifulSoup
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
	#'user-agent': ua.random,
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

