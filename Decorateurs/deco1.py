def deco(fonction):
    # La fonction doit y être sinon le décorateur démarre automatiquement avec @deco.
    def wrapper():
        print("*********")
        return fonction()
    return wrapper
@deco
def ditBonjour():
    print("Bonjour")

ditBonjour()

