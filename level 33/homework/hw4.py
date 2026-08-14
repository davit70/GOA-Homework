def find_multiples(integer, limit):
    # Your code here!
    res = []
    i = 1
    
    while integer * i <= limit:
        res.append(integer * i)
        i += 1  
        
    return res