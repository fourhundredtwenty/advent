with open("5.data") as datafile:
    other_peoples_tickets = [line.strip() for line in datafile.readlines()]

tickets_as_zeroes_and_ones = [
    ticket.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
    for ticket in other_peoples_tickets
]

sorted_ticket_ids = sorted(
    [int(ticket, base=2) for ticket in tickets_as_zeroes_and_ones]
)

# yea ok

print([ticket_pair[0] + 1 for ticket_pair in zip(sorted_ticket_ids, sorted_ticket_ids[1:]) if ticket_pair[1] - ticket_pair[0] == 2][0])
