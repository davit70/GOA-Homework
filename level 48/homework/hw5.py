def no_space(x):
    res = ""
    for i in x:
        if i != " ":
            res += i
    return res