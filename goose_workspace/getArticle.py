import urllib2
from BeautifulSoup import BeautifulSoup
import bs4
from goose import Goose

def getArticle(url):
	g = Goose()
	article = g.extract(url=url)
	print article.title
	print ""
	print article.meta_description
	print ""
	print article.meta_keywords
	print ""
	print article.tags
	print ""
	print article.top_node
	print ""
	print article.additional_data
	print ""
	print article.domain
	# print article.author

def getURLS(url):
	urls = []
	page = urllib2.urlopen(url).read()
	soup = bs4.BeautifulSoup(page)
	#print_link = soup.findAll('a')[0].get('href')
	#print print_link
	print ""

	soup.prettify()
	res1 = soup.findAll("a", href=True)
	res2 = []
	for a in res1:
		if "story" in a['href']:
			res2.append(a)
	for a in res2:
		print a['href']
	print len(res2)



url = "http://www.politico.com/pages/elections"
getURLS(url)
