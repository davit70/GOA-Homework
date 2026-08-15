# 7) მომხმარებელს შემოატანინეთ სიტყვა და შეამოწმეთ, არის თუ არა იგი დიდი ასოებით, თუ კი — დაბეჭდე "სიტყვა უკვე დიდია!", თუ არა — გადააქციე და დაბეჭდე.


word = input('any word ')

if word == word.upper():
    print('this word is already written in uppercase letters')
else:
    print(word.upper())