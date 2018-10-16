#@/usr/bin
class Lampada(object):
   
    def __init__(self,nome,pgpio,status,numrele,lumi):
        self.nome = nome
        self.pgpio = pgpio
        self.status = status
        self.numrele = numrele
        self.lumi = lumi
    def setNome(self,nome):
        self.nome = nome

    def setPgpio(self,pgpio):
        self.pgpio = pgpio

    def setStatus(self,status):
        self.status = status

    def setNumRele(self,numrele):
        self.numrele = numrele

    def setLumi(self,lumi):
        self.lumi = lumi

    def getNome(self):
        return self.nome
    def getPgpio(self):
        return self.pgpio
    def getStatus(self):
        return self.status
    def getNumRele(self):
        return self.numrele
    def getLumi(self):
        return self.lumi
