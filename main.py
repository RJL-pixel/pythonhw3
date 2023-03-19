class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._area = a*b


    def __add__(self, other):
        return self._area + other._area


    def __sub__(self, other):
        return self._area - other._area



    def __eq__(self, other):
        return self._area == other._area

    def __ne__(self, other):
        return self._area == other._area

    def __lt__(self, other):
        return self._area < other._area
    def __gt__(self, other):
        return self._area > other._area

    def __len__(self):
        return self.a + self.b





class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Cinderella(Human):
    __count = 0
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count+=1

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        print(cls.__count)


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size


    def find_cinderella(self, cinderellas:list[Cinderella]):
        for cinderella in cinderellas:
            if cinderella.foot_size == self.shoe_size:
                return cinderella
            else:
                return 'NotFound'



cinderellas_list:list[Cinderella] = [

    Cinderella('Dima', 16, 285),
    Cinderella('Dimu', 16, 26),
    Cinderella('Dimi', 17, 27),
    Cinderella('Dimo', 158, 28),
    Cinderella('Dimp', 159, 29),
]


prince = Prince('Max', 20, 27)
print(prince.find_cinderella(cinderellas_list))

Cinderella.get_count()


#3



from abc import ABC, abstractmethod



class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)
class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)

class Main:
    printable_list:list[Book|Magazine] = []

    @classmethod
    def add(cls, item:Book|Magazine):
        if isinstance(item, (Book, Magazine)):
           cls.printable_list.append(item)
    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()




Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()