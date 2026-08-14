def abbrev_name(name):

    space = name.find(" ")
    
    letter1 = name[0].upper()
    letter2 = name[space + 1].upper()
    
    return letter1 + "." + letter2