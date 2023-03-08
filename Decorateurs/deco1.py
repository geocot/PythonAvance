
def deco(fonction):
    def wrapper(): #La fonction doit y être sinon le décorateur démarre automatiquement.
        print("*********")
        return fonction()
    return wrapper

@deco
def ditBonjour():
    print("Bonjour")

ditBonjour()