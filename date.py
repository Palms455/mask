from datetime import datetime
import dateparser


a = '26 марта'
f = 'сегодня, 12:30'
b = '30.03.2020'
print(dateparser.parse(f))
c = datetime.strptime('30/03/09 16:31:32.123', '%d/%m/%y %H:%M:%S.%f')
d = datetime.strptime('30.03.09', '%d.%m.%y')
f = datetime.now()
j = (f- d).days
if j == 4018:
	print('ok')
print(f - d)
x = datetime.strptime(a, u'%d %M')
print(x)