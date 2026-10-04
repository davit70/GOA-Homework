#11)მომხმარებელს შემოატანინეთ ელფოსტის მისამართი და გადაამოწმეთ შეიცავს თუ არა '@'
#  სიმბოლოს, შედეგი კი დაბეჭდეთ დიდი ასოებით

gmail = input("enter your e-mail")


if "@"  in gmail:
    print(gmail.upper())

else:
    print("wrong e-mail try again")
