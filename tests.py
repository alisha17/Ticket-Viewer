import unittest
import requests

from tickets import get_tickets, get_tickets_id
from connect import connect

class ConnectTestCase(unittest.TestCase):
    """Tests if connection to API getting established"""

    def test_is_connected(self):
        # Established connection to API
        msg = "Connection established successfully!"
        self.assertEqual(msg, connect())

class AuthorizeTestCase(unittest.TestCase):
    """Tests to establish authorization to access API"""

    def test_is_not_authorized(self):
        # In case the user is not authorized
        url = "https://alisha9355.zendesk.com/api/v2/tickets.json"
        r = requests.get(url)
        self.assertEqual(r.status_code, 401)

    def test_is_authorized(self):
         # In case the user is authorized 
         url = "https://alisha9355.zendesk.com/api/v2/tickets.json"
         auth = ('anejaalisha37@gmail.com','Princess@17')
         r = requests.get(url, auth=auth)
         self.assertEqual(r.status_code, 200)

class TicketIdTestCase(unittest.TestCase):
    """Tests the validity of Ticket ID"""

    def test_id_is_valid(self):
        # Valid ticket ID- a positive integer
        id = 6
        url = "https://alisha9355.zendesk.com/api/v2/tickets/{}.json".format(id)
        r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
        self.assertEqual(r.status_code, 200)

    def test_id_is_empty(self):
        # Invalid ticket Id- empty ID
        url = "https://alisha9355.zendesk.com/api/v2/tickets/{}.json".format(id)
        r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
        self.assertEqual(r.status_code, 400) 

    def test_id_is_negative(self):
        # Invalid ticket Id- negative integer ID
        id = -7
        url = "https://alisha9355.zendesk.com/api/v2/tickets/{}.json".format(id)
        r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
        self.assertEqual(r.status_code, 400) 

    def test_id_is_string(self):
        # Invalid ticket Id- string ID
        id = "xyz"
        url = "https://alisha9355.zendesk.com/api/v2/tickets/{}.json".format(id)
        r = requests.get(url ,auth=('anejaalisha37@gmail.com','Princess@17'))
        self.assertEqual(r.status_code, 400) 


if __name__ == '__main__':
    unittest.main()