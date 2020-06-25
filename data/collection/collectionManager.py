import json, sqlite3
from textStorage import sorting

# determines if input matches available search terms
def parseAliases(input):
    filereader = open("aliases.json", "r")
    factionAliases = json.load(filereader)["faction"]
    aliases = (factionAliases.keys())
    # print(aliases)
    # print(input in aliases)
    if (input in aliases):
        return input
    for alias in aliases:
        if (input in factionAliases[alias]):
            return alias
    raise Exception(f"{input} not found in aliases")

# print (parseAliases("DE"))
# print (parseAliases("USN"))
# print (parseAliases("burger"))

sorting.sortFaction("DE")
