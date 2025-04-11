def main():
     liste_etudiants = {
     'Alice': {
          'Mathematiques': 90,
          'Francais': 80,
          'Histoire': 95
     },
     'Bob': {
          'Mathematiques': 75,
          'Francais': 85,
          'Histoire': 70
     },
     'Charlie': {
          'Mathematiques': 88,
          'Francais': 92,
          'Histoire': 78
          }
     }
     nom = input("Entrez le nom de l’étudiant :  ")
     if nom in liste_etudiants:
          etudiant = liste_etudiants[nom]
          total_notes = 0
          print(f"Notes de {nom} :  ")
          for matiere in etudiant:
               note = etudiant[matiere]
               print(f"{matiere} : {note} ")
               total_notes += note
          moyenne = total_notes / len(etudiant)
          print(f"Moyenne de {nom} : {moyenne:.2f}")
     else:
          print(f"L'étudiant {nom} n'existe pas dans la liste.")


if __name__ == "__main__":
    main()
