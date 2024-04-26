class Fuvar:
    def __init__(self, azon, iIdo, idotartam, tavolsag, fizetseg, borravalo, fizetesmod) -> None:
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
for line in f:
    line = line.strip().split(';')
    fuvarlista.append(Fuvar(line[0],line[1],line[2],line[3],line[4],line[5],line[6]))
f.close()

print("3. feladat: ",len(fuvarlista) "fuvar")

fuvarszam = 0
bevetel = 0
for fuvar in fuvarlista:
    if fuvar.azon == 6185:
        fuvarszam += 1
        bevetel += fuvar.price + fuvar.tip
print(f"4. feladat: {fuvar} fuvar alatt: {str(bevetel).replace('.',',')}$")
