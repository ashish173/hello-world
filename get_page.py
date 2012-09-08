#!usr/bin/python
import re
import urllib2

def get_page(url):
	f = urllib2.urlopen(url) # page handler
	content = f.read()   # reading the source code of webpage.
	return content
	

def main():
	# print 'hello world!!'
	# removing junk....
	url = raw_input("enter the url")
	content =  get_page(url)
	

if __name__ == "__main__":
	main()
