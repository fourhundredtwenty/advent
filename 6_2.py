with open("6.data") as datafile:
    raw_forms = datafile.read()

groups_of_forms = raw_forms.split("\n\n")

groups_of_people = [[person for person in group.split('\n') if person] for group in groups_of_forms]

print(sum(
    [len(set("".join(
        ["".join(
            [letter for letter in person
             if all(letter in other_person for other_person in group)]
        ) for person in group]
    ))) for group in groups_of_people]
))
