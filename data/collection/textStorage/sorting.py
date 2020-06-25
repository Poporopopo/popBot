import pathlib

# reads txt file and separates items into lines
def parseText(filename):
    output = []
    with open(filename, 'r') as collection:
        line = collection.readline()
        while (line != ""):
            reassembled = reassemble(line, output)
            line = collection.readline()
    return (output)

#takes a string and splits it along spaces
#reassemble phrases and returns an array
def reassemble(string, output):
    # String to be built while assembling
    assembly = ""
    line = string.split(" ")
    for piece in line:
        if ("" != piece):
            assembly += piece + " "
        elif (assembly != ""):
            assembly = assembly[0:-1]
            output.append(assembly)
            assembly = ""
    if (assembly != ""):
        assembly = assembly[0:-2]
        output.append(assembly)
    return

# rewrites text file alphabetically sorted
def rewrite(filename):
    parsed = parseText(filename)
    parsed.sort()
    with open(filename, "w") as writer:
        for line in parsed:
            writer.write(line + "\n")

# finds all factions and sorts them in the text file
def sortAllFactions():
    path = pathlib.Path(__file__).parent
    for child in path.iterdir():
        try:
            if (child.suffixes[0] == ".txt"):
                rewrite(str(child))
        except IndexError as error:
            print(error)

# sorts one faction
# takes in the faction shorthand
def sortFaction(faction):
    file = findPath(faction)
    rewrite(file)

# finds the faction file depending on the faction name
# throws error if file doesn't exist
def findPath(faction):
    path = str(pathlib.Path(__file__).parent)
    file = f"{path}/{faction}.txt"
    return(file)
