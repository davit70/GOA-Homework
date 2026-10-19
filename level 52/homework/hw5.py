def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg > 0:
        if fuel_left * mpg >= distance_to_pump:
            return True
        else:
            return False
    return False