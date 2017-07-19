from urllib.request import urlopen

import requests
import tabulate

def connect():
    	# Check if connection with API established
	try:
		urlopen('https://alisha9355.zendesk.com/', timeout=1)
		print ("Connection established successfully!")

	except Exception as err:
		print (":( Oh uh, connection not established due to:", err)