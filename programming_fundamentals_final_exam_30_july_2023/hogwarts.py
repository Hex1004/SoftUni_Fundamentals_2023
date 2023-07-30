spell_deciphered = [input()]

class Hogwarts:
    def __init__(self, index, letter, first_substring, second_substring, substring):
        self.letter = letter
        self.first = first_substring
        self.second = second_substring
        self.substring = substring
        self.valid_index = index

    def check_index(self):
        if 0 <= self.valid_index < len(spell_deciphered[0]):
            return True
        print("The spell was too weak.")

    def abjuration(self):
        spell_deciphered[0] = spell_deciphered[0].upper()
        print(spell_deciphered[0])

    def necromancy(self):
        spell_deciphered[0] = spell_deciphered[0].lower()
        print(spell_deciphered[0])

    def illusion(self, index, letter):
        self.valid_index = index
        self.letter = letter
        if self.check_index():
            spell_deciphered[0] = spell_deciphered[0][:self.valid_index] + self.letter + spell_deciphered[0][self.valid_index + 1:]
            print("Done!")

    def divination(self, first_substring, second_substring):
        self.first = first_substring
        self.second = second_substring
        if self.first in spell_deciphered[0]:
            spell_deciphered[0] = spell_deciphered[0].replace(self.first, self.second)
            print(spell_deciphered[0])

    def alteration(self, substring):
        self.substring = substring
        if self.substring in spell_deciphered[0]:
            spell_deciphered[0] = spell_deciphered[0].replace(self.substring, "", 1)
            print(spell_deciphered[0])

allowed_commands = ["Abracadabra", "Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]

command = input()

while command.lower() != "abracadabra":
    command_type = command.split()
    if command_type[0] not in allowed_commands:
        print("The spell did not work!")
    else:
        hogwarts = Hogwarts(0, "", "", "", "")
        if command_type[0] == "Abjuration":
            hogwarts.abjuration()
        elif command_type[0] == "Necromancy":
            hogwarts.necromancy()
        elif command_type[0] == "Illusion":
            hogwarts.illusion(int(command_type[1]), command_type[2])
        elif command_type[0] == "Divination":
            hogwarts.divination(command_type[1], command_type[2])
        elif command_type[0] == "Alteration":
            hogwarts.alteration(command_type[1])
    command = input()
