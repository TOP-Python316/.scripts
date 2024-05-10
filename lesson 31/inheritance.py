class Person:
    def can_sleep(self):
        print('I can sleep')

    def can_walk(self):
        print('I can walk')


class Doctor(Person):
    def can_heal(self):
        print('I can heal')
    

class Engineer(Person):
    def can_code(self):
        print('I can code')


class Teacher(Person):
    def can_teach(self):
        print('I can teach')


class Surgeon(Doctor):
    def can_surgery(self):
        print('I can surgery')


d = Doctor()
e = Engineer()
t = Teacher()
s = Surgeon()

d.can_heal()
e.can_code()
t.can_teach()

d.can_sleep()
e.can_sleep()
t.can_sleep()

d.can_walk()
e.can_walk()
t.can_walk()

print('----------------')
s.can_walk()
s.can_sleep()
s.can_heal()
s.can_surgery()