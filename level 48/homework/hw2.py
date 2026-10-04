def longest(a1, a2):
    result = []
    for i in a1 + a2:
        if i not in result:
            result.append(i)
    result.sort()
    return "".join(result)