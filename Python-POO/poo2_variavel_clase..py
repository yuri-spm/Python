class A:
    vc = 123 #variavel de classe

    def __init__(self):
        self.vc = 321


a1 = A()
a2 = A()

#A.vc = 321 #alterando a variavel de classe
#a1.vc = 321

print(a1.__dict__)
print(a2.__dict__)

print(a1.vc)
print(a2.vc)
print(A.vc)
