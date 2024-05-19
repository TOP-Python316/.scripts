class A:
    attr = 'атрибут класса A'


class B:
    def __init__(self, instance: A):
        self.associated = instance


a = A()
d = A()
b = B(instance=a)

c = B(isinstance=a)
e = B(instance=d)


a
# >>>: <__main__.A object at 0x7fcf310b73a0>
a.attr
# >>>: 'атрибут класса A'
b
# >>>: <__main__.B object at 0x7fcf310b7310>
b.associated
# >>>: <__main__.A object at 0x7fcf310b73a0>
b.associated.attr
# >>>: 'атрибут класса A'
a.__dict__
# >>>: {}
a.value = 316
a.__dict__
# >>>: {'value': 316}
b.associated.__dict__
# >>>: {'value': 316}
b.associated.value
# >>>: 316
