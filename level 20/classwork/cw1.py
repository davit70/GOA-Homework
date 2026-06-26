# 1) მომხმარებელს შემოატანინე თავისი სახელი. შენი დავალებაა დაბეჭდო სახელი ყველა პატარა ასოთი.

# 2) მომხმარებელს შემოატანინე თავისი საყვარელი ფერის დასახელება. შენი დავალებაა დაბეჭდო ეს ფერი ყველა დიდი ასოთი.

# 3) მომხმარებელს შემოატანინე ქალაქის სახელი რომელშიც ცხოვრობს. 
#  შენი დავალებაა დაბეჭდო სახელი მხოლოდ პირველი ასო დიდი ასოთი და დანარჩენი პატარა ასოებით.

# 4) მოცემულია ელ.ფოსტა:
# email = "student@university.ge". 
# იპოვე და დაბეჭდე "@" სიმბოლოს ზუსტი პოზიცია (index).

# 5) ტექსტში -->
# word = "Programming" 
# იპოვე, მერამდენე ინდექსზეა პირველი ასო "r".

# 6) მოცემულია ტექსტი: 
# sentence = "მე მიყვარს ვაშლი და მსხალი.". 
# გამოიყენე find(), რათა შეამოწმო, მოიძებნება თუ არა მასში სიტყვა "ბანანი".

# 7) შეტყობინებაში:
# info = "Error 404: Page not found" 
# იპოვე სიტყვა "404"-ის საწყისი ინდექსი find()-ის გამოყენებით და დაბეჭდე ის.

# 8) შეამოწმე, იწყება თუ არა ვებ-გვერდის მისამართი -->
# url = "https://www.google.com" 
# სწორი და უსაფრთხო პრეფიქსით "https://".

# 9) მოცემულია ტელეფონის ნომერი:
# phone = "+995555123456". 
# შეამოწმე startswith()-ით, ეკუთვნის თუ არა ეს ნომერი საქართველოს საერთაშორისო კოდს ("+995").

# 10) პროგრამას მიეწოდება ფაილის სახელი: 
# filename = "document.pdf". 
# შეამოწმე, ნამდვილად მთავრდება თუ არა იგი ".pdf" გაფართოებით.

# 11) მომხმარებელს შემოაქვს წინადადება. შეამოწმე, სვამს თუ არა ის კითხვას (ანუ მთავრდება თუ არა წინადადება კითხვის ნიშნით "?").

# 12) სიტყვაში --> 
# word = "abracadabra" 
# დათვალე, სულ რამდენჯერ გვხვდება ასო "a".

# 13) მოცემულია რიცხვების მიმდევრობა სტრიქონის სახით 
# data = "100110101011". 
# დათვალე და დაბეჭდე, რამდენჯერ მეორდება მასში ციფრი "1".

# 14) გაქვს მძიმეებით გამოყოფილი პროდუქტების სია სტრიქონად: 
# products = "პური,რძე,კვერცხი,ყველი". 
# გარდაქმენი ის Python-ის სიად (list) split() მეთოდით (გამყოფად გამოიყენე მძიმე).

# 15) მოცემული გაქვს სიტყვა:
# "hello world"
# გამოითავლე სულ რამდენი სიმბოლოსგან შედგება ეს წინადადება.


name = input('enter your name ')
print(name.lower())

color = input('enter ur fav color ')
print (color.upper())

city = input('enter the city you live in ')
print(city.capitalize())


email = "student@university.ge"
print(email.index('@'))


word = "Programming" 
print(word.find('r'))


sentence = "მე მიყვარს ვაშლი და მსხალი."
print(sentence.find('ბანანი'))


info = "Error 404: Page not found"
print(info.find('404'))


url = "https://www.google.com" 
print(url.startswith('https://'))


phone = "+995555123456"
print(phone.startswith('+995'))


filename = "document.pdf"
print(filename.endswith('.pdf'))


sentence2 = input('enter any sentence ')
print(sentence2.endswith('?'))


word = "abracadabra"
print(word.count('a'))


data = "100110101011"
print(data.count('1'))


products = "პური,რძე,კვერცხი,ყველი"
print(products.split(','))


sentence3 = 'hello world'
print(len('hello world'))