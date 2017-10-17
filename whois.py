import os

def whois(url):
	command="whois "+url
	process=os.popen(command)
	results=str(process.read())
	return results




