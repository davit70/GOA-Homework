# 5) მომხმარებელს შემოატანინეთ ელფოსტის მისამართი და გადაამოწმეთ შეიცავს თუ არა '@' სიმბოლოს, შედეგი კი დაბეჭდეთ  პატარა ასოებით
gmail = 'Davit@example.com'
if '@' in gmail:
    print(gmail.lower())
else:
    print('wrong e-mail')