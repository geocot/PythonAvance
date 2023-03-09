from dataclasses import dataclass, field

@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False, default=3) #Pas besoin d'initialiser

    #def __post_init__(self): #Méthode magique appelée après __init___()
    #    self.c = self.a + self.b

ic = C(12,34)
print(ic)

