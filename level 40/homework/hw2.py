def merge_arrays(arr1, arr2):
    pass
    
    combined = sorted(arr1 + arr2)
    result = []
    
    for i in combined:
        if not result or result[-1] != i:
            result.append(i)
            
    return result