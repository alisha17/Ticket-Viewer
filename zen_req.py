import requests
from urllib.request import urlopen
import json
import pprint

def check_connection():
	# Check if the API is getting connected
	try:
		urlopen('https://alisha9355.zendesk.com/', timeout=1)
		print (True)
	except urllib.request.URLError as err:
		print (False)

def get_tickets():
	# Get all tickets
	try:
		url = "https://alisha9355.zendesk.com/api/v2/tickets.json"
		r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
		# print (json.loads(r.text))
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(json.loads(r.text))
	except Exception as e:
		print (e)

# check_connection()

get_tickets()
