class Duck:
    def swim_quack(self):
        print('Я утка и я умею плавать и крякать')


class RobotBird:
    def swim_quack(self):
        print('Я робоптица и я умею плавать и крякать')


def duck_test(animal):
    animal.swim_quack()


d = Duck()
r = RobotBird()

duck_test(d)
duck_test(r)