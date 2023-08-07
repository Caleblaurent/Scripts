"""
  Programme:
  ==========
    Verification d'un nombre harshad.

  Description:
  ============
    # Ce programme permet de verifier si une chaîne de
    caractère est un nombre harshad.
    # Ce programme contient un fonction qui prend en
    arguments le nombre, verifie s'il est harshad et
    revoie vrai ou faux.

  NOTE:
    Un nombre harshad est un nombre qui est divisible par
    la somme de ses chiffres.

    Exemple:
    ========
    18 est un nombre harshad car 1 + 8 = 9 et 18 est
    divisible par 9.

"""
__Auteurs__ = ("Laurent Caleb")
__Contacts__ = ("laurentcaleb@gmail.com")
__Version__ = "1.0"
__Date__ = "Le 02/03/2020"
__Codage__ = "UTF-8"
#___________________

# Recuperation des donnees.
nombre = input("Entrer le nombre ici => ")   # Demande d'entre le nombre.
# Creation d'une fonction pour verifier le nombre est harshad.
def harshad_verifier(nombre_arg):
  """
    Description:
    ===========
      Cette fontion prend en argument le nombre et
      verifie si c'est un nombre harshad ou pas.
    
    Arguments:
    ==========
      nombre_arg(integer): contient un nombre entier.
      return (integer): retourne un nombre entier.
  """
  # Trouver les chiffres compris dans le nombre.
  chiffres_liste = []   # Variable pour inserer les chiffres compris du nombre.
  for chiffres in nombre_arg:   # Boucle sur le nombre pour recuperer les chiffres.
    chiffres_liste.append(int(chiffres))   # A chaque boucle ajouter le chiffres 
    # a la variable 'chiffres'.
  # Enregistre la somme des chiffres du nombre.
  somme_chiffres = sum(chiffres_liste)
  # Verifier si la somme des chiffres du nombre est un diviseur.
  diviseur_verifier = divmod(int(nombre_arg), somme_chiffres)
  return diviseur_verifier[-1]   # Retour le quotient de la division.

print(harshad_verifier(nombre))   # Affiche la sortie de la fonction.