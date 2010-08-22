import re, StringIO
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from random import randrange
import mechanize, cookielib
import html2text
from tidylib import tidy_document
from time import strftime, localtime


def encodeToAscii(text, ls = True):
	if ls == True: #The text is a list
		return map(lambda x: x.encode('ascii'),text)
	else:
		return text.encode('ascii')

def getAllLinks(htmlpage, reg = False):
	links = []

	if reg == False:
		soup = BeautifulSoup(htmlpage)
		for item in soup.fetch('a'):
			links.append(item['href'])
		return encodeToAscii(links)
	else:
	
		linksList = re.findall('<a href=(.*?)>.*?</a>',str(htmlpage))
		for link in linksList:
			links.append(link)
		return links

def isHtmlLink(link):
	"Checks whether a link ends with .html and returns a match obj if true"
	return re.search(r'^http(.*?)\.s?html$', link)

def isProperLink(link):
	return re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link)

def isGoogleLink(link):
	return re.search(r'http://www.google.(.*?)', link)


def parse(text, *atrs):
	"Returns the result of parsing atrs using BeautifulSoup"
	soup= BeautifulSoup(text)
	body = soup.find(*atrs)
	return body

def parseAll(text, *atrs):
	"Returns all the results of parsing atrs using BeautifulSoup"
	text = text.encode('utf-8')
	soup= BeautifulSoup(text)
	body = soup.findAll(*atrs)
	return body

def getHtml(url):

    class NoHistory(object):
        def add(self, *a, **k): pass
        def clear(self): pass

    br = mechanize.Browser(history = NoHistory())
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    r = br.open(url,  timeout = 200)
    html = r.read()
    
    document, errors = tidy_document(html, options={'numeric-entities':1}) #use tidy to clean the html	
    return document

def matchOnce(text,pattern):
	obj = re.compile(pattern)
	res = obj.search(text)
	return str(res.groups(1))

def matchAll(text, pattern):
	res = re.compile(pattern, re.DOTALL)
	return res.findall(text)

def getTitle(text, bs = True):
	"Returns the Html Title of the page, given a html document as input"
	if(bs == True):
		soup = BeautifulSoup(text)
		titletag = soup.html.head.title
		return titletag.string.encode('ascii')
	else:
		return matchOnce(text, r'<title>(.*?)</title>')

def getSearchLinks(text):
	"Returns all the links from scraping a google custom search page, given a html document as input"
	soup = BeautifulSoup(text)
	allLinks = soup.findAll('h2', {"class":"r"}) #gets all the h2 tags search urls
	allLinks = map(str, allLinks)

	fsoup = BeautifulSoup(''.join(allLinks))
	links = [] #start with an empty list
	for item in fsoup.fetch('a'):
		  links.append(item['href']) #iterate over all the href elements and append to the links list

	links =  map(lambda x: x.encode('ascii'),links) #BeautifulSoup returns unicode strings, hence converting to ascii
	return links



def stripHtml(in_text):
	"""Description: Removes all HTML/XML-like tags from the input text.
	Inputs: s --> string of text
	Outputs: text string without the tags

	# doctest unit testing framework

	>>> test_text = "Keep this Text <remove><me /> KEEP </remove> 123"
	>>> strip_ml_tags(test_text)
	'Keep this Text  KEEP  123'
	"""
	# convert in_text to a mutable object (e.g. list)
	s_list = list(in_text)
	i,j = 0,0

	while i < len(s_list):
		# iterate until a left-angle bracket is found
		if s_list[i] == '<':
			while s_list[i] != '>':
				# pop everything from the the left-angle bracket until the right-angle bracket
				s_list.pop(i)

			# pops the right-angle bracket, too
			s_list.pop(i)
		else:
			i=i+1

	# convert the list back into text
	join_char=''
	return join_char.join(s_list)



def randElement(lst):
	ind = len(lst)- 1
	randint = randrange(0, ind)
	return lst[randint]

#Returns a sequence that consists only of uniques , i.e removes duplicates
def uniquer(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result






#Time utils

def getTime():
	return strftime("%d %b %Y %I:%M %p", localtime())


#ls = ["a", "a", "b"]
#print uniquer(ls)
