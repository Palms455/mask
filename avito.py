from bs4 import BeautifulSoup
from write import write_csv
import dateparser
from datetime import datetime
from connect import get_html
#from reserv_connect import get_html

	
def from_avito(key, page=None):
	if not page:
		page = 1
	url = f'https://avito.ru/{key[0]}?s=104&q={key[1]}&p={page}'
	html = get_html(url)
	if html is None:
		print('no html')
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


