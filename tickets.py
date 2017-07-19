import requests
import tabulate
from urllib.request import urlopen
import json
from operator import itemgetter
import pydoc


def check_connection():
	# Check if the API is getting connected
	try:
		urlopen('https://alisha9355.zendesk.com/', timeout=1)
		print ("Connection established successfully!")

	except Exception as err:
		print (":( Oh uh, connection not established due to:", err)

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

def main():
		print ("			WELCOME TO ZENDESK TICKET VIEWER         ")
		print ("Select option to proceed")
		print ("   * Press 1 to check if connection established with the account")
		print ("   * Press 2 to view all tickets")
		print ("   * Press 3 to view a ticket")
		print ("   * Press 9 to quit\n")
		option = input("Enter no. to proceed ")
		
		if option == "1":
				check_connection()
		elif option == "2":
				get_tickets()
		elif option == "3":
				ticket_no = input("Enter ticket number:")
				get_tickets_id(ticket_no)		
		elif option == "9":
    			print ("Bye! Have a good day!")
    			exit()		
		else:
			    print ("Oh uh wrong option")

if __name__== "__main__":
	main()