import requests
import tabulate
import json
import pydoc

from operator import itemgetter

def get_tickets():
	# Get all tickets
	try:
		new_dict = dict()
		temp_list = list()
		l = dict()

		url = "https://alisha9355.zendesk.com/api/v2/tickets.json"
		r = requests.get(url, auth=('anejaalisha37@gmail.com','Princess@17'))

		if r.status_code == 401:
    			print ("Oops! You are not authorized.")
		elif r.status_code == 404:
    			print ("Oops! API not found.")
		elif r.status_code == 503:
    			print ("Oops! API is unavailable.")
		else:	
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
						print (pydoc.pager(tabulate.tabulate(rows, headers, tablefmt="grid")))
							

	except Exception as e:
		print ("Something is wrong!", e)

def get_tickets_id(id):
    # Get ticket by ticket ID	
	try:
		if id.isnumeric() == True:
				url = "https://alisha9355.zendesk.com/api/v2/tickets/{}.json".format(id)
				r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))

				if r.status_code == 401:
						print ("Oops! You are not authorized.")
				elif r.status_code == 404:
						print ("Oops! API not found.")
				elif r.status_code == 503:
						print ("Oops! API is unavailable.")
				else:
						new_dict = json.loads(r.text)
						for k,v in new_dict.items():
								if k == "ticket":
										new_dict = v
						fields =  ("created_at", "assignee_id", "subject")
						l = dict((key,value) for key, value in new_dict.items() if key in fields)
						
						data = sorted([(k,v) for k,v in l.items()]) 
						print (tabulate.tabulate(data, tablefmt="grid"))
		else:
    			print ("Oops! ID has to be a positive integer value")
    			exit()

	except Exception as e:
		print (e)
