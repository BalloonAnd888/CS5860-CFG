def separateBracket(lines: list) -> list:
    result = []
    for s in lines:
        current = ''
        for char in s:
            if char == '{' or char == '}':
                if current.strip():
                    result.append(current.strip())
                    current = ''
                result.append(char)
            else:
                current += char
        if current.strip():
            result.append(current.strip())
    
    # print("After separating brackets:", result)

    return result
