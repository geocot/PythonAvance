class SysSolaire:
    def __init__(self, planetes):
        self._planetes = planetes

    def __len__(self):
        return len(self._planetes)

voieLactee = SysSolaire(['Mercure', 'Vénus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune'])

print(len(voieLactee))




