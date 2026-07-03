# 7) შემქნით ცარიელი სია, სადაც 3-ჯერ input-ის სახით მომხმარებელს შეაყვანინებთ სამი სტუდენტის სახელს და დაამატებთ სიაში append() ფუნქციით.
#  შემდეგ კი ჩასვით "Teacher" სიის თავში, წაშალეთ ბოლო სტუდენტი და დაბეჭდეთ სიის სიგრძე, ასვეე საბოლოო სია.
students = []
name = input('enter name ')
name2 = input('enter name ')
name3 = input('enter name ')
students.append(name)
students.append(name2)
students.append(name3)
students.insert(0, 'teacher')
students.pop()
print(len(students))
print(students)