import urllib
def get_page(url):
	words = ''
	fhand = urllib.urlopen(url)
	for line in fhand:
		for word in line.split():
			words = words + word + ' '
	return words
print get_page('http://www.py4inf.com/code/romeo.txt').split()