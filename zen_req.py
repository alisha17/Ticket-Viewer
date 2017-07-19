import requests
import tabulate
from urllib.request import urlopen
import json
import pprint
from prettytable import PrettyTable
from operator import itemgetter
import pydoc


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
		new_dict = dict()
		lis1 = list();
		url = "https://alisha9355.zendesk.com/api/v2/tickets.json"
		r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
		pp = pprint.PrettyPrinter(indent=4)
		new_dict = json.loads(r.text)
		#pp.pprint(new_dict)
		for k,v in new_dict.items():
    			if k == "tickets":
    					lis1 = v
		#header = lis1[0].keys()
        
		keys = {"created_at", "assignee_id", "subject"}
		l = {}
		l = list(map(lambda x: {k:v for k, v in x.items() if k in keys}, lis1))
		headers = l[0].keys()
		rows =  [x.values() for x in l]

		if len(l) <= 25:
    			print (tabulate.tabulate(rows, headers, tablefmt="grid"))
		else:
    			print(pydoc.pager(tabulate.tabulate(rows, headers, tablefmt="grid")))		

	except Exception as e:
		print (e)

def get_tickets_id():
	try:
		id = 5
		url = "https://alisha9355.zendesk.com/api/v2/tickets/{}.json".format(id)
		r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
		pp = pprint.PrettyPrinter(indent=4)
		new_dict = json.loads(r.text)
		for k,v in new_dict.items():
    			if k == "ticket":
    					new_dict = v
		l = dict((key,value) for key, value in new_dict.items() if key in ("created_at", "assignee_id", "subject"))
		data = sorted([(k,v) for k,v in l.items()]) 
		print(tabulate.tabulate(data, tablefmt="grid"))
	except Exception as e:
		print (e)

def main():
    	print("			WELCOME TO ZENDESK TICKET VIEWER         ")

if __name__== "__main__":
	main()