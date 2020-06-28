import json, sqlite3, pathlib, csv

parentpath = str(pathlib.Path(__file__).parent)

# determines if input matches available search terms
def parseAliases(input):
    aliasfile = open(parentpath  + "/aliases.json", "r")
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

def readItemCollection():
    collectioncsv = open(parentpath + "/collection.csv", "r")
    collectionreader = csv.reader(collectioncsv)
    items = []
    for item in collectionreader:
        print(item)
        items.append(item)
    return items

print(readItemCollection())

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
