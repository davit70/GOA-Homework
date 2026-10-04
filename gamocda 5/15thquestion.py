# 14)შექმენით ფუნქცია სახელად celsius_to_fahrenheit, რომელიც იღებს ტემპერატურას ცელსიუსში (C) და გადაჰყავს 
# ფარენჰეიტში (F). ფორმულა: F = (C \times 1.8) + 32

def cels(temperature):
    temp = temperature * 1.8 + 32
    return temp
print(cels(25))