def sum_array(arr):
    #your code here

    if not arr or len(arr) < 3:
        return 0
    
    total = 0
    highest = arr[0]
    lowest = arr[0]
    
    for i in arr:
        total += i
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i
            
    return total - highest - lowest