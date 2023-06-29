# my solution:
names = ["Jannick", "", "Marc", "Lisa", "", "Marie"]

for name in names:
    if name == "":
        names.remove(name)
print(names)

# original solution:
names_two = ["Jannick", "", "Marc", "Lisa", "", "Marie"]
cleaned_list = list(filter(None, names_two))
print(cleaned_list)
