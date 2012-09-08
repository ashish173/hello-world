#!usr/bin/python
import os
import re
import urllib2

def get_page(url):
	f = urllib2.urlopen(url) # page handler
	content = f.read()   # reading the source code of webpage.
	return content
	
def links(content):
	match = r'[\w.]+@[\w.]+'
	list_link = re.findall(match , content)
	print list_link


def main():
	# print 'hello world!!'
	# removing junk....
	url = raw_input("enter the url")
	content =  get_page(url)
	links(content)

if __name__ == "__main__":
	main()
