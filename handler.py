from avito import from_avito 
from youla import from_youla
from irr import from_irr
from multiprocessing import Pool



keywords = {
	'Арбидол',
	'ферон', 
	'Кагоцел', 
	'маски медицинские', 
	'антисептичес', 
	'хлоргексидин', 
	'плаквенил'
	}

regions = {
	'avito': {'ufa',
		'bashkortostan', 
		'ekaterinburg', 
		'sverdlovskaya_oblast', 
		'tyumen', 
		'tyumenskaya_oblast', 
		'chelyabinskaya_oblast', 
		'chelyabinsk', 
		'moskva_i_mo'
		},
	'youla' : {
		'ufa',
		'ekaterinburg',
		'tyumen', 
		'chelyabinsk',
		'moskva'
		},

	'irr' : {
		'ufa',
		'bashkortostan-resp',
		'ekaterinburg',
		'sverdlovskaya-obl',
		'tyumen',
		'tyumenskaya-obl',
		'chelyabinsk',
		'chelyabinskaya-obl',
		'moscow'
		}
	}



def data_prepare(keywords, regions, key):
	data = []
	for region in regions[key]:
		for keys in keywords:
			data.append([region, keys])
	return data



avito = data_prepare(keywords, regions, 'avito')
irr = data_prepare(keywords, regions, 'irr')
youla = data_prepare(keywords, regions, 'youla')


#for item in avito:
#	from_avito(item)

if __name__ == '__main__':
	with Pool(5) as p:
		results1 = p.map(from_avito, avito)
		results2 = p.map(from_youla, youla)
		results3 = p.map(from_irr, irr)



