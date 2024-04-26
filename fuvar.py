class fuvar:
    def __init__(self,azon,indul,ido,tav,dij,borra,mod):
        self.azon = azon
        self.indul = indul
        self.ido = ido
        self.tav = tav
        self.dij = dij
        self.borra = borra
        self.mod = mod
        
    def __str__(self):
        return f"{self.azon},{self.indul},{self.ido},{self.tav},{self.dij},{self.borra},{self.mod}"






f = open("fuvar.csv", "rt", encoding="UTf-8")