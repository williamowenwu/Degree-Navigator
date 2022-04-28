class Student:
    #* Class variables
    attending_at = "Rutgers University"
    
    # only can be one init function
    def __init__(self, name: str, year: str, age: int, fulltime: bool = False, major: str = 'Undecided', minor: str = 'Undecided'):
        self.name = name
        self.fulltime = fulltime
        self.year = year
        self.major = major
        self.minor = minor
        self.age = age
        
    @classmethod
    def set_university(cls, university):
        cls.attending_at = university
    
    @classmethod #alternative constructor
    def from_string(cls, string):
        name, year, age, fulltime, major, minor = string.split(" ")
        return cls(name, year, age, fulltime, major, minor)

    @staticmethod #does not have instance or class 
    def has_free_time(grade):
        if grade == 'A' or grade == 'B':
            return 'Yes'
        return 'No'
    
    def __repr__(self):
        return "Student('{}''{}''{}''{}''{}')".format(self.name, self.year, self.age, self.fulltime, self.major)
    
    def __str__(self):
        return "Name: {} year: {} Major: {}".format(self.name, self.year, self.major) 
    
class LA(Student): #argument is the parent class -> inheritance
    def __init__(self,name: str, year: str, age: int, pay, fulltime: bool = False, major: str = 'Undecided', minor: str = 'Undecided', students: list = None):
        super().__init__(name,year, age, fulltime, major, minor) #* Super referes to the base class (same thing as saying Student class)
        self.pay = pay
        if students is None:
            self.students = []
        else:
            self.students = students
            
    def add_students(self, student):
        if student not in self.students:
            self.students.append(student)
    
    def remove_students(self, student):
        if student in self.students:
            self.students.remove(student)
            
    def show_students(self):
        if not self.students:
            print(self.students)
        else:
            for student in self.students:
                print(student.name)
                


random_data = "Mike sophomore 20 False CompSci Undecided"
mike = Student.from_string(random_data)
william = LA('William Wu', 'Sopohmore', 20, 25, True)

Student.set_university('Drexel')

william.show_students()
print(mike)
print(vars(william))
print(dict.fromkeys(['bruh', 'heh']))

# print(william)
# print(Student.has_free_time('C'))
# print(william.pay)
# print(mike.major)