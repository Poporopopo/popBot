import json, sqlite3, pathlib
from textStorage import sorting

parentpath = str(pathlib.Path(__file__).parent)
# print(path)
aliasfile = open(parentpath  + "/aliases.json", "r")

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

# database constants
database = sqlite3.connect(parentpath + "/popBot.db")

def createFactionTable():
    # create table if not exists
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS shipgirl_items("
            "name text,"
            "faction text,"
            "shiptype text,"
            "currentuser text,"
            "uses int"
        ")"
    )

    # get filenames of faction. ie: "EU"
    factionAliases = json.load(aliasfile)["faction"]
    fileheaders = (factionAliases.keys())
    # print(fileheaders)

    # get paths for factions
    for fileheader in fileheaders:
        # read file factions
        filename = sorting.findPath(fileheader)
        # print (filename)
        filecontent = sorting.parseText(filename)
        # print (filecontent)
        

createFactionTable()
