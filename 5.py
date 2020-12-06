with open("5.data") as datafile:
    other_peoples_tickets = [line.strip() for line in datafile.readlines()]

# ok here's an idea:
# if we convert all F to 0 and all B to 1
# does that get us a correct row number?
# I'd like to eventually see if turning the R into 1 and the L into 0
# and then casting the whole thing to binary if we can just get the whole-ass score
# (maybe we have to reverse it? something about endian-ness)
# there's 3 bits for the seats, which is 8 bits, and if we multiply the row number times 8
# it's basically the same as bit shifting it 3, right? so we can just make it one number
# And for the seats the R to 1 and L to 0 i think
# let's go.
#
# row example:
# FBFBBFF == 0101100 binary == int("0101100", base=2) == 44
# 44 is the same answer as the example heck yea
#
# seat example:
# RLR == 101 == int("101", base=2) == 5
# 🎉
#
# ID number example:
# FBFBBFFRLR 0101100101 = int("0101100101", base=2) = 357
# 🏎️ also correct! yay let's go

tickets_as_zeroes_and_ones = [
    ticket.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
    for ticket in other_peoples_tickets
]

# int() is all that's needed to convert these strings into ticket IDs now
# and we can sort it to find the largest ticket
sorted_ticket_ids = sorted([int(ticket, base=2) for ticket in tickets_as_zeroes_and_ones])
biggest_ticket_id = max(sorted_ticket_ids)

print(biggest_ticket_id)
