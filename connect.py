from urllib.request import urlopen

import requests
import tabulate

def connect():
    	# Check if connection with API established
	try:
		urlopen('https://alisha9355.zendesk.com/', timeout=1)
		return ("Connection established successfully!")

	except Exception as err:
		return (":( Oh uh, connection not established due to:", err)