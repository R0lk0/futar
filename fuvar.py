class Fuvar:
    def __init__(self, taxiAzon, iIdo, idotartam, tavolsag, viteldij, borravalo, fizetesmod):
        self.taxiAzon = taxiAzon
        self.iIdo = iIdo
        self.idotartam = idotartam
        self.tavolsag = tavolsag
        self.viteldij = viteldij
        self.borravalo = borravalo 
        self.fizetesmod = fizetesmod

def negyesfeladat():
    fuvarokSzama = 0
    bevetel = 0
    for sor in f:
        if Fuvar(sor[0]) == 6185:
            fuvarokSzama += 1
            bevetel += Fuvar(sor[5])

fuvarok = []
f = open('fuvar.csv', 'rt', encoding = 'utf-8')
for sor in f:
    f.readline()
    sor = sor.strip()
    sor = sor.split(';')
    fuvarok.append(Fuvar(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5], sor[6]))

print('3. feladat:', , 'fuvar')
print('4. feladat: ')