class Person:  # Parent - родительский

    def can_walk(self):
        print('I can walk')

    def can_breathe(self):
        print('I can breathe')


class Doctor(Person):  # subclass

    def can_cure(self):
        print('I can treat')


class Ortoped(Doctor):
    pass


class Arhitect(Person):  # subclass

    def can_build(self):
        print('I can building')


b = Doctor()
a = Arhitect()
print(issubclass(Doctor, Person))
e = Ortoped()
e.can_cure()


