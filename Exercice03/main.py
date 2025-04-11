words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
voyelles = {"a", "e", "i", "o", "u", "y"}

liste_finale = [
    (word, sum(1 for letter in word if letter in voyelles)) for word in words
]

print(liste_finale)

sans_comprehension_de_liste = []
for word in words:
    nb_voyelle = 0
    for letter in word:
        if letter in voyelles:
            nb_voyelle += 1
    sans_comprehension_de_liste.append((word, nb_voyelle))

print(sans_comprehension_de_liste)
