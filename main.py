from tickets import get_tickets, get_tickets_id
from connect import connect

def main(): 
        print ("			WELCOME TO ZENDESK TICKET VIEWER         ")
        flag = True

        while flag == True:   
            print ("\n Select option to proceed")
            print ("   * Press 1 to establish connection with the account")
            print ("   * Press 2 to view all tickets")
            print ("   * Press 3 to view a ticket")
            print ("   * Press 9 to quit\n")
            option = input("Enter no. to proceed ")
            if option == "1":
                    msg = connect()
                    print ("\n",msg)
            elif option == "2":
                    get_tickets()
            elif option == "3":
                    ticket_no = input("Enter ticket number: ")
                    get_tickets_id(ticket_no)		
            elif option == "9":
                    print ("Bye! Have a good day!")
                    exit()		
            else:
                    print ("Oh uh wrong option")

if __name__== "__main__":
    main()