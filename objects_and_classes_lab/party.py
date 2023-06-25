class Party:
    def __init__(self):
        self.people = []

party = Party()

name_of_people = input()

while name_of_people != "End":
    party.people.append(name_of_people)
    name_of_people = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
