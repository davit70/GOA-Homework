def to_jaden_case(string):
    words = string.split()
    result = []
    for i in words:
        result.append(i.capitalize())
    return " ".join(result)