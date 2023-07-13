class Passage_riv:
    def __init__ (self):
        self.etatI="cflo;"
        self.etatF=";cflo"
        self.la=[]
        self.le=[]
    def afficher_passager(self,a):
        if(a=="c"):
            print("chevre")
        if(a=="l"):
            print("loup")
        if(a=="f"):
            print("fermier")
        if(a=="o"):
            print("chou")
    def afficher_etat(self,etat):
        x=etat.find(";")
        if(x>0):
            print("les passagers qui se trouvent dans la rive gauche")
            for i in range(0,x):
                self.afficher_passager(etat[i])
        if(x<len(etat)-1):
            print("les passagers qui se trouvent dans la rive droite")
            for i in range(x,len(etat)):
                self.afficher_passager(etat[i])
    def admissible(self,etat):
        x=etat.find(";")
        if ("l" in etat[:x] and "c" in etat[:x] and  "f" not in etat[:x]) or ("c" in etat[x:] and "l" in etat[x:] and  "f" not in etat[x:]):
            return False
        if ("o" in etat[:x] and "c" in etat[:x] and  "f" not in etat[:x]) or ("c" in etat[x:] and "o" in etat[x:] and  "f" not in etat[x:]):
            return False
        else:
            return True
    def action(self,etat,passager,direction):
        etat=str.replace(etat,passager,"")
        etat=str.replace(etat,"f","")
        if direction=="gd":
            if passager!="f": 
               etat=etat+passager+"f"
            else:
               etat=etat+"f"
        else:
            if passager!="f":
                etat="f"+passager+etat
            else:
                etat="f"+etat
        y=etat.find(";")
        etat=''.join(sorted(etat[:y]))+";"+''.join(sorted(etat[y+1:]))
        return etat
    def successeur (self , etat):
        s=[]
        x=etat.index("f")
        y=etat.index(";")
        self.le.append(etat)
        if x<y:
            sens="gd"
            for i in range(y):
                new_etat=self.action(etat,etat[i],sens)
                if (self.verif_etat(new_etat)==True)and(self.admissible(new_etat)==True):
                    s.append(new_etat)
                    self.la.append(new_etat)
        else :
            sens="dg"
            for i in range(y+1,len(etat)):
                new_etat=self.action(etat,etat[i],sens)
                if (self.verif_etat(new_etat)==True)and(self.admissible(new_etat)==True):
                    s.append(new_etat)
                    self.la.append(new_etat)
        return s[0]
    def verif_etat(self,etat):
        if (etat in self.la) or (etat in self.le):
            return False
        else:
            return True
class Pile:
    etats=[]
    def __initialisationpile__(self):
        self.etats = []
    def empiler(self, etat):
            self.etats.append(etat)
    def depiler(self):
    	if self.etat:
    	    return self.etats.pop()
    def estVide(self):
	    return self.etats == []
    def afficher(self):
    	print("\nEtat de la pile:\n")
    	for x in self.etats:
    	    print("|\t" + str(x) + "\t|" + "\n")


    def profondeur(self):
        l=[]
        p=self.pile()
        p.empiler(self.etatI)
        while(not p.pile_vide()):
            node=p.depiler()
            print(node)
            if(node==self.etatF):
                return True
            self.explores.append(node)
            l=self.successeur(node)
            for i in range(len(l)):
                p.empiler(l[i])
        return False

    def largeur(self):
        l=[]
        f=self.file()
        f.emfiler(self.etatI)
        while(not f.file_vide()):
            node=f.defiler()
            print(node)
            if(node==self.etatF):
                return True
            self.explores.append(node)
            l=self.successeur(node)
            for i in range(len(l)):
                f.emfiler(l[i])
        return False            
            
             

p=passage_riv()
chaine=input("donner l etat ")
p.affiche_etat(chaine)
if(p.admissible(chaine)):
    print("etat admissble")
else:
    print("etat non admissble")
p.action(chaine,"gd","f")
print(p.successeurs(chaine))
p.profondeur()

p.largeur()
