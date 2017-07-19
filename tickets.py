import requests
import tabulate
import json
import pydoc

from operator import itemgetter

# Invalid response
# authentication error
# readme
# requirements

def get_tickets():
	# Get all tickets
	try:
		new_dict = dict()
		temp_list = list()
		l = dict()
		url = "https://alisha9355.zendesk.com/api/v2/tickets.json"
		r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
		new_dict = json.loads(r.text)
		for k,v in new_dict.items():
    			if k == "tickets":
    					temp_list = v

		keys = {"created_at", "assignee_id", "subject"}
		l = list(map(lambda x: {k:v for k, v in x.items() if k in keys}, temp_list))
		headers = l[0].keys()
		rows =  [x.values() for x in l]

		if len(l) <= 25:
    			print (tabulate.tabulate(rows, headers, tablefmt="grid"))
		else:
    			print(pydoc.pager(tabulate.tabulate(rows, headers, tablefmt="grid")))		

	except Exception as e:
		print ("The tickets couldn't be fetched due to:", e)

def get_tickets_id(id):
    # Get ticket by ticket number	
	try:
		url = "https://alisha9355.zendesk.com/api/v2/tickets/{}.json".format(id)
		r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
		new_dict = json.loads(r.text)
		for k,v in new_dict.items():
    			if k == "ticket":
    					new_dict = v
		l = dict((key,value) for key, value in new_dict.items() if key in ("created_at", "assignee_id", "subject"))
		data = sorted([(k,v) for k,v in l.items()]) 
		print (tabulate.tabulate(data, tablefmt="grid"))

	except Exception as e:
		print (e)
