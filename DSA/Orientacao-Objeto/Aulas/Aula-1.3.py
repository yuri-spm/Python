class Cachorro():
    def __init__(self, raca):
        self.raca = raca
        print("Contrutor chamado para cirar um ojeto desta classe")

rex = Cachorro(raca='Labrador')
golias = Cachorro(raca="Huskie")

print(rex.raca)
print(golias.raca)
