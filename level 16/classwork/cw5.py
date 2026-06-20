get_highets = [90,81,100,23,3,98,142,90,75]



print(max(get_highets))
max_numbers=get_highets[0]
for number in get_highets:
    if number > max_numbers:
        max_numbers=number
print(max_numbers)
