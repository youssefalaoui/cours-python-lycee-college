##
## https://www.youtube.com/channel/UC-HeY9T6K3t9r9SyDHjKasA
##
#while

#### code simple pour affichier le double pour chaque nombre de 1 a 5
nombre1 = 1
nombre2 = 2
nombre3 = 3
nombre4 = 4
nombre5 = 5
print("Le double de ", nombre1, ' est: ', nombre1 *2 )
print("Le double de ", nombre2, ' est: ', nombre2 *2 )
print("Le double de ", nombre3, ' est: ', nombre3 *2 )
print("Le double de ", nombre4, ' est: ', nombre4 *2 )
print("Le double de ", nombre5, ' est: ', nombre5 *2 )

#### code ameliore avec while
nombre = 1
while nombre <=5:
    print("Le double de ", nombre, ' est: ', nombre *2 )
    nombre = nombre + 1
else:
    print("plus de double a calculer !")

#### code avec while calculant le double jusqu'a 3 (inclu)
nombre = 1
while nombre <=5:
    print("Le double de ", nombre, ' est: ', nombre *2 )
    nombre = nombre + 1
    if nombre ==4:
        break

#### code sautant le nombre 4
nombre= 0
while nombre < 5:
    nombre = nombre + 1
    if nombre == 4:
        continue
    print("Le double de ", nombre, ' est: ', nombre *2)
    print(".....>>><<<....")


# For
# code avec while
nombre = 1
while nombre <=5:
    print("Le double de ", nombre, ' est: ', nombre *2 )
    nombre = nombre + 1
# code avec for
for nombre in range(1, 6):
    print("Le double de ", nombre, ' est: ', nombre * 2)

# boucle
voitures =  ['BMW', 'Ferrari', 'McLaren']
for voiture in voitures:
    print(voiture)

# boucle avec else
for nombre in range(1, 6):
    print(nombre)
else:
    print("plus de nombre !")

# boucle s'arretant a PSA (exclue)
voitures =  ['BMW', 'Ferrari', 'McLaren', 'PSA', 'Renault']
for voiture in voitures:
    if voiture == 'PSA':
        break
    print(voiture)

# boucle sautant la valeur Ferrari
voitures =  ['BMW', 'Ferrari', 'McLaren', 'PSA', 'Renault']
for voiture in voitures:
    if voiture == 'Ferrari':
        continue
    print(voiture)

# boucle imbriquees
models_voitures = [
            ['BMW I8', 'BMW X3', 'BMW X1'],
            ['Ferrari 812', 'Ferrari F8', 'Ferrari GTC4'],
            ['McLaren 570S', 'McLaren 570GT', 'McLaren 720S']
]

for marque in models_voitures:
    for modele in marque:
        print(modele)


# For tuple
personnes = ('Jean', 'Karim', 'Nathalie')
for personne in personnes:
    print(personne)

# for dictionnaire
personnes = {'Jean', 'Karim', 'Nathalie'}
for personne in personnes:
    print(personne)

# boucle serie de dictionnaires
etudiants = [
    {
        'nom': 'Marie',
        'age': 23,
        'sexe': 'F'
    },
    {
        'nom': 'Karim',
        'age': 26,
        'sexe': 'M'
    }
]

for etudiant in etudiants:
    print(etudiant['nom'])