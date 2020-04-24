# exercice:
# Trouvez le nombre magique !
# C’est un nombre aléatoire de 1 à 20 choisi par l’ordinateur
# 3 essais au maximum
# Guider l’utilisateur si le nombre est plus grand ou plus petit que le nombre magique
# Féliciter si le nombre est correct (sinon ce n’est pas grave)

# note: le code est simple et ne verfie pas si la valeur entree est uniquement numerique
import random
nombreMagique = random.randint(1, 20)

for i in range(0, 3):
    print("Essai #", i+1)
    nombreEntre = input("Merci de deviner un nombre: ")
    nombreEntre = int(nombreEntre)
    if nombreEntre > nombreMagique:
        print("Votre nombre est superieur au nombre magique.")
    if nombreEntre < nombreMagique:
        print("Votre nombre est inferieur au nombre magique.")
    if nombreEntre == nombreMagique:
        print("Bravo vous l'avez trouve ! il s'agit bien de ", nombreMagique)
        break
else:
    print("Ce n'est pas grave, essayez encore une fois ? le nombre magique etait: "
          , nombreMagique)