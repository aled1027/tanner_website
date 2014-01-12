import urllib2
import bs4

def getURLS(AMT_URLS=10):
	url = "http://www.politico.com/pages/elections"
	urls = []
	page = urllib2.urlopen(url).read()
	soup = bs4.BeautifulSoup(page)
	soup.prettify()
	for a in soup.findAll("a", href=True):
		if "story" in a['href']:
			urls.append(a['href'])
	urls = list(set(urls)) # prevents duplicate urls
	urls = urls[:AMT_URLS]

	return urls



