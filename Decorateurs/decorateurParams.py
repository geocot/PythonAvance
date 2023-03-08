#Il faut mettre le décorateur dans une autre fonction
def verificationUtilisateur(nomUsager):
    def decorateur(fonction):
        def wrapper():
            if nomUsager == "Martin":
                return fonction()
            else:
                print("Mauvais usagé")
        return wrapper
    return decorateur

@verificationUtilisateur("Martin")
def connexion():
    print("Connexion avec Martin")

connexion()


