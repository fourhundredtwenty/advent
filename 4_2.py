class Passport(dict):
    def validate(self):
        self.validator_functions = {
            'byr': self.validate_byr,
            'iyr': self.validate_iyr,
            'eyr': self.validate_eyr,
            'hgt': self.validate_hgt,
            'hcl': self.validate_hcl,
            'ecl': self.validate_ecl,
            'pid': self.validate_pid,
            'cid': self.validate_cid,
        }

        print()
        print(self)

        has_the_right_fields = set([i for i in self.validator_functions.keys() if not i =='cid']).issubset(set(self.keys()))
        fields_all_look_good = all([self.validator_functions[field_name](field_value) for field_name,field_value in self.items()])

        print(f"good fields: {has_the_right_fields}")
        print(f"fields  valid : {fields_all_look_good}")
        return has_the_right_fields and fields_all_look_good

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    def validate_byr(self, field_value):
        print(f"byr: {field_value} -> {2002 > int(field_value) > 1920}")
        if field_value.isdigit():
            return 2002 >= int(field_value) >= 1920
        else:
            return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    def validate_iyr(self, field_value):
        print(f"iyr: {field_value} -> {2020 >= int(field_value) >= 2010}")
        if field_value.isdigit():
            return 2020 >= int(field_value) >= 2010
        else:
            return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    def validate_eyr(self, field_value):
        print(f"eyr: {field_value} -> {2030 > int(field_value) > 2020}")
        if field_value.isdigit():
            return 2030 >= int(field_value) >= 2020
        else:
            return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    def validate_hgt(self, field_value):
        height_is_all_cool = False
        try:
            unit = field_value[-2:]
            value = int(field_value[:-2])
        except (ValueError, IndexError):
            height_is_all_cool = False

        if unit == "cm":
            height_is_all_cool = 193 >= value >= 150
        elif unit == "in":
            height_is_all_cool = 76 >= value >= 59

        print(f"hgt: {field_value} -> {height_is_all_cool}")
        return height_is_all_cool

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    def validate_hcl(self, field_value):
        print(f"hcl: {field_value} -> {field_value.startswith('#') and set(field_value).issubset('#0123456789abcdef')}")

        return field_value.startswith('#') and set(field_value).issubset("#0123456789abcdef")

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    def validate_ecl(self, field_value):
        print(f"ecl: {field_value} -> {field_value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']}")

        return field_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    def validate_pid(self, field_value):
        print(f"pid: {field_value} -> {field_value.isdigit() and len(field_value) == 9}")

        return field_value.isdigit() and len(field_value) == 9

    # cid (Country ID) - ignored, missing or not.
    def validate_cid(self, field_value):
        return True





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

# print(passports[0].validate())
print([passport.validate() for passport in passports].count(True))

