from bs4 import BeautifulSoup
from write import write_csv
import dateparser
from datetime import datetime
from connect import get_html




def from_youla(key, url = None):
	print(key)
	file = 'Юла ' + key[0]
	check = None
	if url is None:
		url = f'https://youla.ru/{key[0]}?attributes[sort_field]=date_published&q={key[1]}'
	html = get_html(url)
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('ul', class_='product_list')
	try:
		items = table.find_all('li')
	except:
		return
	for item in items:
		url = 'https://youla.ru' + item.find('a').get('href')
		print(url)
		title = item.find('div', class_='product_item__title').text
		date = item.find('span', class_='visible-xs').text
		if (datetime.now() - dateparser.parse(date)).days <= 3:
			data = {'url': url,'date': date, 'title': title}
			check = 1
			write_csv(data, file)
	page_url = soup.find('div', class_='pagination__button').find('a').get('href')
	if page_url and check:
		from_youla(key, page_url)
	return
