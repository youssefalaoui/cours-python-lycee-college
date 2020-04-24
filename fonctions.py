

####################################
# video Link:
####################################
# Note importante: pour mieux comprendre les exemples suivants (et les executer sans prob !), il est
# important de revoir les videos sur https://www.youtube.com/channel/UC-HeY9T6K3t9r9SyDHjKasA
####################################
####################################
# A quoi ca sert une fonction
####################################
####################################

list1 = [1, 2, 3, 45, 65, 24]
list2 = [3, 56, 34, 67, 109, 10, 46]
list3 = [46, 234, 34, 6, 80, 1093, 45, 90, 34]

somme1 = 0
for i in list1:
    somme1 = somme1 + i
moyenne1 = somme1 / len(list1)
print("la moyenne de la liste ", list1 , " est ", moyenne1)

somme2 = 0
for i in list2:
    somme2 = somme2 + i
moyenne2 = somme2/len(list2)
print("la moyenne est ", moyenne2)


somme3 = 0
for i in list3:
    somme3 = somme3 + i
moyenne3 = somme3/len(list3)
print("la moyenne est ", moyenne3)


# fonction
def calcul_moyenne(list):
    somme = 0
    for i in list:
        somme = somme + i
    moyenne = somme / len(list)
    return moyenne


moyenneList1 = calcul_moyenne(list1)
moyenneList2 = calcul_moyenne(list2)
moyenneList3 = calcul_moyenne(list3)

print("la moyenne de la liste 1 ", moyenneList1)
print("la moyenne de la liste 2", moyenneList2)
print("la moyenne de la liste 3 ", moyenneList3)

####################################
####################################
# Savoir plus sur les fonctions, les arguments, return ...
####################################
####################################
def retourne_moi_plusieurs_valeurs():
    return 10, 34, 3

print(retourne_moi_plusieurs_valeurs())

def imprime_moi_qqch():
    print("je suis la maison, youpi")

imprime_moi_qqch()


def addition(premier_nombre, deuxieme_nombre):
    return premier_nombre + deuxieme_nombre

print(addition(3, 4))

def soustraction(premier_nombre, deuxieme_nombre):
    return deuxieme_nombre - premier_nombre

print(soustraction(6, 3))
print(soustraction(deuxieme_nombre = 6, premier_nombre = 3))


def choisi_un_nombre_a_afficher(nombre = 30):
    print(nombre)
choisi_un_nombre_a_afficher(14)
choisi_un_nombre_a_afficher(24)
choisi_un_nombre_a_afficher(56)
choisi_un_nombre_a_afficher()

def afficher_les_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

def afficher_les_mots(*mots):
    for mot in mots:
        print(mot)

afficher_les_mots("je", "tu", "il/elle")

afficher_les_nombres(3, 45, 65)
afficher_les_nombres(30, 65, 34, 23, 10)

def afficher_cles_valeurs(**arguments):
    for cle, valeur in arguments.items():
        print(cle, " = ", valeur)

afficher_cles_valeurs(prenom = "Jack", nom="Dupont")
afficher_cles_valeurs(prenom = "John", nom="Hillis", age="34", sexe="M")

####################################
####################################
# la portee d'une fonction
####################################
####################################
def afficher_nom():
    nom = "Dupont"
    print("Mon nom de famille est:", nom)

nom = "Kaki"
afficher_nom()





