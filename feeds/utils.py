import urllib2


class HeadRequest(urllib2.Request):
	def get_method(self):
		return "HEAD"


def get_headers(url):
	response = urllib2.urlopen(HeadRequest(url))
	return response.info()
