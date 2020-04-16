class cachorro():
    def __init__(self, raca):
        self.raca = raca
        print("Contrutor chamado para cirar um ojeto desta classe")

rex = cachorro(raca='Labrador')
golias = cachorro(raca="Huskie")

print(rex.raca)
print(golias.raca)
