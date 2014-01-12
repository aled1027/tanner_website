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



#url = 'http://globalpublicsquare.blogs.cnn.com/2014/01/11/why-iraq-is-in-turmoil/?hpt=wo_c2'
url = "http://www.politico.com/story/2014/01/chris-christie-bridgegate-questions-102066.html?hp=t1"
getArticle(url)
