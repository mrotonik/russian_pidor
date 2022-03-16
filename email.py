import urllib,re
import urllib.request
sites = ['https://kzd.rzd.ru']

for site in sites:
	f = urllib.request.urlopen(site)
	s = f.read().decode('utf-8')
	emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
	newemails = list(set(emails))
	print (newemails)