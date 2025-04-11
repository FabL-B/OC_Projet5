## Écrivez votre code ici !
def square(nombre):
    if not isinstance(nombre, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    else:
        return nombre ** 2
