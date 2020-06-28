import json, sqlite3, pathlib, csv

parentpath = str(pathlib.Path(__file__).parent)

# determines if input matches available search terms
def parseAliases(input, aliasGroup):
    aliasfile = open(parentpath  + "/aliases.json", "r")
    factionAliases = json.load(aliasfile)[aliasGroup]
    aliases = (factionAliases.keys())
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
        items.append(item)
    return items

# database constants
databasePath = (parentpath + "/popBot.db")

def createFactionTable():
    # database connection
    database = sqlite3.connect(databasePath)
    cursor = database.cursor()

    # create table if not exists
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS shipgirl_items("
            "name text UNIQUE,"
            "faction text,"
            "shiptype text,"
            "currentuser text,"
            "uses int"
        ")"
    )

    # add items to database
    collection = readItemCollection()
    for item in collection:
        try:
            cursor.execute(
                "INSERT INTO shipgirl_items VALUES (?, ?, ?, '', 0)",
                (item[0], item[1], item[2])
            )
        except sqlite3.IntegrityError as error:
            error

    # close database connection
    database.commit()
    database.close()
