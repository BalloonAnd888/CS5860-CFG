from separateBracket import separateBracket

def parseLines(filename: str) -> list:
    lines = []
    inMultilineComment = False
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if "/*" in line:
                inMultilineComment = True
            if "*/" in line:
                inMultilineComment = False
                continue  

            if line and not line.startswith("//") and not inMultilineComment:
                lines.append(line)

    # print("Before separating brackets:", lines)

    lines = separateBracket(lines)

    return lines
