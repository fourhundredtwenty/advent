class Passport(dict):
    REQUIRED_FIELDS = set([
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid',
    ])

    def validate(self):
        return self.REQUIRED_FIELDS.issubset(set(self.keys()))


with open("4.data") as datafile:
    raw_passports = datafile.read()

# every element in this list is a string containing the unparsed raw data for one single passport
separated_passports = raw_passports.split("\n\n")

# this is a list of lists. each list is a passport, and each element in the list is a string representing a key-value pair for this passport
# e.g.
# [
#   ["byr:1", "iyr:2", "eyr:3"],
#   ["byr:5", "iyr:7", "eyr:9"],
# ]
separated_and_formatted_passports = [passport.replace('\n', ' ').split() for passport in separated_passports]

# this is gonna be a list of Passport objects -- they're just dicts
# [
#   {
#     'byr': 1,
#     'iyr': 2,
#     'eyr': 3,
#   }
#   {
#     'byr': 5,
#     'iyr': 7,
#     'eyr': 9,
#   }
# ]
passports = []
for passport_string in separated_and_formatted_passports:
    passports.append(Passport(dict([passport.split(':') for passport in passport_string])))

print([passport.validate() for passport in passports].count(True))

