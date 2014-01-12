from goose import Goose

def getArticle(url):
	g = Goose()
	article = g.extract(url=url)
	return article




