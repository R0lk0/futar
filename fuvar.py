class Fuvar:
    def __init__(self, taxiAzon, iIdo, idotartam, tavolsag, viteldij, borravalo, fizetesmod):
        self.taxiAzon = taxiAzon
        self.iIdo = iIdo
        self.idotartam = idotartam
        self.tavolsag = tavolsag
        self.viteldij = viteldij
        self.borravalo = borravalo 
        self.fizetesmod = fizetesmod

fuvarok = []
f = open('fuvar.csv', 'rt', encoding = 'utf-8')
for sor in f:
    fuvarok.append(sor)

print('3. feladat:', len(fuvarok) -1, 'fuvar')
