
def duplicate_elements(m, n):
    res = False
    
    for i in m:
        if i in n:
            res = True
            
    return res