class Fuvar:
    def __init__(self, azon, iIdo, idotartam, tavolsag, fizetseg, borravalo, fizetesmod):
        self.azon = int(azon)
        self.iIdo = iIdo
        self.idotartam = idotartam
        self.tavolsag = tavolsag
        self.fizetseg = float(fizetseg.replace(',', '.'))
        self.borravalo = float(borravalo.replace(',', '.'))
        self.fizetesmod = fizetesmod

fuvarlista = []
f = open('fuvar.csv', 'rt', encoding='utf-8')
f.readline()
for sor in f:
    sor = sor.strip().split(';')
    fuvarlista.append(Fuvar(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5],sor[6]))
f.close()

print("3. feladat: ",len(fuvarlista), "fuvar")

fuvarszam = 0
bevetel = 0
for fuvar in fuvarlista:
    if fuvar.azon == 6185:
        fuvarszam += 1
        bevetel += fuvar.fizetseg + fuvar.borravalo
print(f"4. feladat: {fuvarszam} fuvar alatt: {str(bevetel).replace('.', ',')}$")

fizetesimodok = {}
for fuvar in fuvarlista:
    if fuvar.fizetesmod in fizetesimodok.keys():
        fizetesimodok[fuvar.fizetesmod] += 1
    else:
        fizetesimodok[fuvar.fizetesmod] = 1
print("5. feladat: ")
for k, v in fizetesimodok.items():
    print(f'\t{k}: {v} fuvar')