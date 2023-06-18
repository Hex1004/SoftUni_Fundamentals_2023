def process_commands(friends, commands):
    blacklisted_count = 0
    lost_count = 0

    for command in commands:
        if command.startswith("Blacklist"):
            _, name = command.split()
            if name in friends:
                friends[friends.index(name)] = "Blacklisted"
                print(f"{name} was blacklisted.")
                blacklisted_count += 1
            else:
                print(f"{name} was not found.")

        elif command.startswith("Error"):
            _, index = command.split()
            index = int(index)
            if 0 <= index < len(friends):
                name = friends[index]
                if name != "Blacklisted" and name != "Lost":
                    friends[index] = "Lost"
                    print(f"{name} was lost due to an error.")
                    lost_count += 1

        elif command.startswith("Change"):
            _, index, new_name = command.split()
            index = int(index)
            if 0 <= index < len(friends):
                current_name = friends[index]
                friends[index] = new_name
                print(f"{current_name} changed his username to {new_name}.")

    print(f"Blacklisted names: {blacklisted_count}")
    print(f"Lost names: {lost_count}")
    print(" ".join(friends))


usernames = input().split(", ")
command_list = []
while True:
    command = input()
    if command == "Report":
        break
    command_list.append(command)

process_commands(usernames, command_list)


def process_commands(friends, commands):
    blacklisted_count = 0
    lost_count = 0

    for command in commands:
        if command.startswith("Blacklist"):
            _, name = command.split()
            if name in friends:
                friends[friends.index(name)] = "Blacklisted"
                print(f"{name} was blacklisted.")
                blacklisted_count += 1
            else:
                print(f"{name} was not found.")

        elif command.startswith("Error"):
            _, index = command.split()
            index = int(index)
            if 0 <= index < len(friends):
                name = friends[index]
                if name != "Blacklisted" and name != "Lost":
                    friends[index] = "Lost"
                    print(f"{name} was lost due to an error.")
                    lost_count += 1

        elif command.startswith("Change"):
            _, index, new_name = command.split()
            index = int(index)
            if 0 <= index < len(friends):
                current_name = friends[index]
                friends[index] = new_name
                print(f"{current_name} changed his username to {new_name}.")

    print(f"Blacklisted names: {blacklisted_count}")
    print(f"Lost names: {lost_count}")
    print(" ".join(friends))


usernames = input().split(", ")
command_list = []
while True:
    command = input()
    if command == "Report":
        break
    command_list.append(command)

process_commands(usernames, command_list)
