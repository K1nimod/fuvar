class fuvar:
    def __init__(self,azon,indul,ido,tav,dij,borra,mod):
        self.azon = azon
        self.indul = indul
        self.ido = ido
        self.tav = tav
        self.dij = float(dij.replace(',', '.'))
        self.borra = float(borra.replace(',', '.'))
        self.mod = mod
        
    def __str__(self):
        return f"{self.azon},{self.indul},{self.ido},{self.tav},{self.dij},{self.borra},{self.mod}"

f = open("fuvar.csv", "rt", encoding="UTf-8")
f.readline

lista = []

for sor in f:
    sor = sor.strip().split(";")
    lista.append(fuvar(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5],sor[6]))

print(f"3.feladat: {len(lista)- 1} fuvar")

db = 0 
bevetel = 0
for sor in lista:
    if sor.azon == '6185':
        db += 1
        bevetel += sor.dij
        bevetel += sor.borra

print(f"{db} fuvar alatt: {str(bevetel).replace('.',',')}$")

