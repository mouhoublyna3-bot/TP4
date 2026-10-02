
class Noeud:
    def __init__(self, valeur, enfants=None):
        self.valeur = valeur
        self.enfants = enfants if enfants is not None else []

    def ajouter_enfant(self, noeud):
        self.enfants.append(noeud)

    def afficher(self):

        if len(self.enfants) == 0:
            return str(self.valeur)

        morceaux = [str(self.valeur)]
        for e in self.enfants:
            morceaux.append(e.afficher())

        return " ".join(morceaux)


# exp(add(2, y))
racine1 = Noeud("exp")
add = Noeud("+")
add.ajouter_enfant(Noeud(2))
add.ajouter_enfant(Noeud("y"))
racine1.ajouter_enfant(add)

print("Arbre 1 :", racine1.afficher())


# mul(3, sin(x))

racine2 = Noeud("*")        # opérateur racine

# Premier enfant : la constante 3
racine2.ajouter_enfant(Noeud(3))

# Deuxième enfant : sin(x)
sinx = Noeud("sin")         # opérateur sin
sinx.ajouter_enfant(Noeud("x"))   # sin a un enfant : x

racine2.ajouter_enfant(sinx)

print("Arbre 2 :", racine2.afficher())

# Sub(mul(3, sin(x)), exp(add(2,Y)))

racine3 = Noeud("-")
racine3.ajouter_enfant(racine2)
racine3.ajouter_enfant(racine1)

print("Arbre 3:", racine3.afficher())