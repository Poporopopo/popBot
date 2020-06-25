import json, sqlite3, pathlib
from textStorage import sorting

path = str(pathlib.Path(__file__).parent) + "/aliases.json"
print(path)
aliasfile = open(path, "r")

# determines if input matches available search terms
def parseAliases(input):
    factionAliases = json.load(aliasfile)["faction"]
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
# sorting.sortFaction("DE")

def createDataBaseFromFiles():
    # get filenames of faction. ie: "EU"
    factionAliases = json.load(aliasfile)["faction"]
    fileheaders = (factionAliases.keys())
    # print(fileheaders)


# createDataBaseFromFiles()
