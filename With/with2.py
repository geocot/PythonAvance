import sqlite3
class GestionBD:
    def __init__(self, nomBD):
        self._nomBD = nomBD

    def __enter__(self):
        self._BDConnexion =  sqlite3.connect(self._nomBD)
        self.cursor = self._BDConnexion.cursor()
        return self

    def ajoutTable(self, nomTable, champs):
        self.cursor.execute(f""" CREATE TABLE {nomTable} (
                            {champs}
                            ); """)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._BDConnexion:
            self._BDConnexion.close()

with GestionBD("maBD.db") as gBD:
    gBD.ajoutTable('Table1', "nom CHAR(25) NOT NULL")


