# a wrapper class for single password file entries
# takes an input string like "2-7 p: pbhhzpmppb"
# and performs validation on it
class Password:
    def __init__(self, raw_password_line):
        self.raw_line = raw_password_line

        self.allowed_count, self.letter, self.password = self.raw_line.split()
        self.min_allowed, self.max_allowed = [int(i) for i in self.allowed_count.split('-')]
        self.letter = self.letter.strip(':')

    @property
    def is_valid(self):
        count_of_letter_in_password = self.password.count(self.letter)

        print(self.password)
        print(self.letter)
        print(count_of_letter_in_password)
        print()

        if count_of_letter_in_password >= self.min_allowed and count_of_letter_in_password <= self.max_allowed:
            return True
        else:
            return False

    def __repr__(self):
        return self.raw_line


# actual code execution starts here
with open("2.data") as datafile:
    raw_password_data = datafile.readlines()

valid_password_count = [Password(line).is_valid for line in raw_password_data].count(True)

print(valid_password_count)
