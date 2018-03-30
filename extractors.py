from HTMLParser import HTMLParser

htmlparser = HTMLParser()

def get_title(item):
	title = item.find("h2", "s-access-title")
	if title:
		return htmlparser.unescape(title.text.encode("utf-8"))
	else:
		return "<missing product title>"

def get_url(item):
	link = item.find("a", "s-access-detail-page")
	if link:
		return link["href"]
	else:
		return "<missing product url>"

def get_price(item):
	price = item.find("span", "s-price")
	if price:
		return price.text
	return None