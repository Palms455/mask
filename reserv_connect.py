import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import json
import time
import csv
from random import choice, randint
from fake_useragent import UserAgent
from ip_read import get_proxy_ip


ua = UserAgent()


def get_html(url):
	headers = {
	'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'cookie': '__cfduid=d3e953c1c16bab30aa7a99d46eb99956f1585210471; tval=top_buy_none; city_ufa_areas=; pharm_type=pharm; city=ufa; text=; _ga=GA1.2.616775817.1585210492; _gid=GA1.2.683288620.1585210492; _ym_uid=1585210492209663619; _ym_d=1585210492; test=1; _ym_visorc_24215119=w; __utma=265944989.616775817.1585210492.1585210493.1585210493.1; __utmc=265944989; __utmz=265944989.1585210493.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; tmr_lvid=1864951ad57915a00afe8960898f0fa4; tmr_lvidTS=1585210493994; _ym_isad=2; top100_id=t1.4469532.2009364880.1585210495863; _PricesInPharm_session=BAh7DEkiD3Nlc3Npb25faWQGOgZFVEkiJTE4ZGY0YWI1YTBiOGFmYmI0ZmM4YzU5YTlmYjc4MTJlBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWsyU0NrYm1MQ20yTEpXbXB1YitDY0FtSHRDZlNCV1cxREJKSXd4Ri9rM3c9BjsARkkiB3N0BjsARkkiDzE1ODUyMTA1MjIGOwBGSSIHY3QGOwBGSSIPMTU4NTIxMDUyMgY7AEZJIgZxBjsARkkiBjAGOwBGSSIHcWEGOwBGSSIGMAY7AEZJIgZhBjsARkkiB1tdBjsAVA%3D%3D--59cefb3415b13c461ac32ec4827d470656a85539; _gat_gtag_UA_48328690_1=1; __utmb=265944989.5.10.1585210493; last_visit=1585192555618::1585210555618; tmr_detect=0%7C1585210559814; tmr_reqNum=16',
	'origin': 'https://cenyvaptekah.ru',
	'pragma': 'no-cache',
	'referer': 'https://cenyvaptekah.ru/ufa/',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	#'user-agent': ua.random,
	#'x-csrf-token': 'hev5isie5ANSX51IE4YRVpJeYIZK1jbTYrnZCqp9M1k=',
	#'x-requested-with': 'XMLHttpRequest',
	}

	p = get_proxy_ip('ip_request.txt')
	proxy = { 'https' : p}
	print(proxy)
	#user_agent = { 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}
	try:
		r = requests.get(url, proxies=proxy, headers=headers)
		print(r.status_code)
	except:
		print('bad request. retrying')
		return get_html(url)
	if r.status_code == 200:
		print('ok')
		return r.text
	else: get_html(url)
