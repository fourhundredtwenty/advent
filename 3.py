import itertools

with open("3.data") as datafile:
    forest = [itertools.cycle(line.strip()) for line in datafile.readlines()]

positions_we_hit = []

for row_number, forest_row in enumerate(forest):
    column_number = row_number*3
    position = list(itertools.islice(forest_row, column_number, column_number+1))[0]
    positions_we_hit.append(position)

print(positions_we_hit.count("#"))
