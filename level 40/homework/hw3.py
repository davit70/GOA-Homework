def count_sheeps(sheep):
    count = 0
    for item in sheep:
        if item is True:
            count += 1
    return count
