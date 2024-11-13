my_list = [1, 2, 3]

print(len(my_list))

class Sample():
    pass

my_sample = Sample()

print(my_sample)


class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}, it has {self.pages} pages!' 
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted!")


b = Book("Python Rocks", "Jose Portilla", 715)


class Students():

    def __init__(self, name, surname, student_id, course, year):
        self.name = name
        self.surname = surname 
        self.student_id = student_id
        self.course = course
        self.year = year

    def __str__(self):
        return f"Hello {self.name} {self.surname}, with student id:{self.student_id}, we want to welcome you to {self.course} course at {self.year} year!\nBest regards!"
    

adam = Students("Adam", "Rodriges", "st000111333", "Cybersecurity", 3)

print(adam)

print(len(b))

print(b)

del b
print(b)
