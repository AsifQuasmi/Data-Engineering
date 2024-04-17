string = "Geeks for Geeks"

# print(f"Welcome {name.capitalize()+ ' ' +surname.casefold()} to the {course}")

# # print('Q' in surname)

# # print(name.rindex('S'))
# # print(name.isupper())
# print(name.startswith('S'))
# print(name.endswith('ifS'))

# name = name.split(",")
# print(name)
# surname = "&".join(name)
# print(surname)
# print(name)
# name = name.strip()
# print(name)

# pos = name.find("Asif")
# print(pos)
pos = string.find("")
while pos >=0:
    print(pos)
    pos = string.find("Geeks",pos+1)