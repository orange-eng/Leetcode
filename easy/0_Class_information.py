import datetime



# -----------------------继承关系
class Person:
    def __init__(self,name,sex,birthday,ident):
        self._name = name
        self._sex = sex
        self._birthday = birthday
        self._id = ident
   
    def id(self):
        return self._id
    def sex(self):
        return self._sex


class Student(Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return year

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self,name,sex,birthday,Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._name = name

    def name(self):
        return self._name

person1 = Person("123","male",12,2)
print(person1.id())

person2 = Student("李阳",'male',44,"A4")
print(person2.name())
        