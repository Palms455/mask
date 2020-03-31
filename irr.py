import requests
from bs4 import BeautifulSoup
from datetime import datetime
import dateparser
from write import write_csv
from ip_read import get_proxy_ip



def get_html(url):
	headers = {
	#'user-agent': ua.random,
	}
	p = get_proxy_ip('ip_request.txt')
	proxy = { 'https' : p}
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


def from_irr(key, url=None):
	file = 'IRR ' + key[0]
	check = None 
	if url is None:

		url = f'https://{key[0]}.irr.ru/searchads/search/keywords={key[1]}/'
	html = get_html(url)
	if html is None:
		return
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('div', class_='js-listingContainer')
	items = table.find_all('div', class_='listing__item')
	for item in items:
		url = item.find('a', class_='listing__itemTitle').get('href')
		title = item.find('div', class_='js-productListingProductName').text
		row_date = item.find('div', class_='updateProduct').text.split()[-2::]
		date = row_date[0] + ' ' + row_date[1]
		if  (datetime.now() - dateparser.parse(date)).days <= 3:
			data = {'title': title, 'date': date, 'url': url}
			write_csv(data, file)
	try:
		page = soup.find('div', class_='page-list').find(a).get('href')
	except: 
		return
	if page and check:
		from_irr(key, page)
	return

