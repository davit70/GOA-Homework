def sum_digits(number):
    pass
    if number < 0:
        number = number * -1
        
    res = 0 
    
    for i in str(number):
        res = res + int(i)
        
    return res