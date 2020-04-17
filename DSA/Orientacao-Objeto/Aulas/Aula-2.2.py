class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def list_func(self):
        print(f'O nome do funcionario é {self.nome} e o seu salário {self.salario}')

func1 = Funcionarios('Kleber Santos', 2000)
func1.list_func()
print('USANDO ATRIBUTOS'.center(30))

print(hasattr(func1,'nome'))
print(hasattr(func1,'salario'))
print(setattr(func1, 'salario', 4500))
print(hasattr(func1,'salario'))
print(getattr(func1,'salario'))
print(delattr(func1,'salario'))
print(hasattr(func1, 'salario'))