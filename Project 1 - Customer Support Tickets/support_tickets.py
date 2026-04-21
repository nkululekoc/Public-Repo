
#list of tickets

tickets = [
    {
        "customer_name": "Jannet Jones",
        "issue_type": "billing",
        "priority": "high",
        "status": "open",
    }, {
        "customer_name": "Linda Jameson",
        "issue_type": "technical",
        "priority": "medium",
        "status": "closed",       
    }, {
        "customer_name": "Stuart Whites",
        "issue_type": "returns",
        "priority": "high",
        "status": "open",       
    }, {
        "customer_name": "Mark Ein",
        "issue_type": "complaints",
        "priority": "low",
        "status": "open",       
    }, {
        "customer_name": "Jeniffer Sparks",
        "issue_type": "technical",
        "priority": "medium",
        "status": "closed",       
    }
]

#This creates an unformatted list

# for ticket in tickets:
#     print(ticket)

#This creates a formatted list
print("----- All Tickets -----".center(60))
print("")
for index in range(len(tickets)):
    print(f"       -- Ticket {index + 1} --                    ")
    print("")
    print(f'Customer Name: {tickets[index]["customer_name"]}')
    print(f'Issue Type   : {tickets[index]["issue_type"]}')
    print(f'Priority     : {tickets[index]["priority"]}')
    print(f'Status       : {tickets[index]["status"]}')
    print("")

def ticket_type(ticket_type, key, value):
    print(ticket_type.center(60))
    print("")
    for ticket in tickets:
        if ticket[key] == value:
                print(f'Customer Name: {ticket["customer_name"]}')
                print(f'Issue Type   : {ticket["issue_type"]}')
                print(f'Priority     : {ticket["priority"]}')
                print(f'Status       : {ticket["status"]}')
                print("")


ticket_type("----- High Priority Tickets -----", "priority", "high")