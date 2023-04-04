winner = {
    "name": "",
    "name_length": 0
}

yes_list = []
no_list = []

while True:
    try:
        name, choice = input().split()
    except ValueError:
        break

    if choice == "YES":
        if name not in yes_list:
            yes_list.append(name)
            if len(name) > winner["name_length"]:
                winner["name"] = name
                winner["name_length"] = len(name)
    else:
        if name not in no_list:
            no_list.append(name)

yes_list.sort()
no_list.sort()

print("\n".join(yes_list))
print("\n".join(no_list))
print("\nAmigo do Habay:\n{}".format(winner["name"]))
