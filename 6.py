with open("6.data") as datafile:
    raw_forms = datafile.read()

groups_of_forms = raw_forms.split("\n\n")

yes_count_per_group = [len(set(group.replace('\n', ''))) for group in groups_of_forms]
total_yesses = sum(yes_count_per_group)

print(total_yesses)
