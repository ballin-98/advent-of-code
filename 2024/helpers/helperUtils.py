def read_file_to_list_of_ints(filePath):
    with open(filePath, "r") as file:
        try:
            return [int(line.strip()) for line in file]
        except ValueError:
            print("File contains non-integer values.")
            return []

def readFile(filePath):
    with open(filePath, "r") as file:
        try:
            return [line.strip() for line in file]
        except:
            print("Error reading files")
            return []

def readTwoInts(filePath):
    array1 = []
    array2 = []
    with open(filePath, "r") as file:
        for line in file:
            split = line.split()
            array1.append(int(split[0]))
            array2.append(int(split[1]))
    return array1, array2