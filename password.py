from re import search

mdp = input("Veuillez entrer votre mot de passe : ")
if len(mdp) <= 8: # len = longueur de la chaine de caractère
    print("Le mot de passe doit contenir au minimum 8 caracteres")

if not search('[A-Z]', mdp): 
    # parcours et cherche une majuscule
    print("Le mot de passe doit contenir au moins une lettre majuscule.")

if not search('[a-z]', mdp): 
    # parcours et cherche une miniscule
    print("Le mot de passe doit contenir au moins un lettre miniscule.")

if not search('[0-9]', mdp):
    # parcours et cherche un chiffre
    print("Le mot de passe doit contenir au moins un chiffre.")

if not search('[!,@,#,$,%,^,&,*]', mdp):
    # parcours et cherche un caractère spécial
    print('Le mot de passe doit contenir au moins un caractère special.')

else:
    print('Le mot de passe est valide')
    